import webbrowser
import os
import re


#All of the following code was provided by Udacity for this project.




# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Pixar Movies: A Compilation</title>

    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.4.1/dist/css/bootstrap.min.css">
    <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@3.4.1/dist/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
            font-family: verdana, sans-serif;
            background: #fafafa;
        }
        #site-nav {
            font-size: small;
            margin: 12px auto 0;
            max-width: 1140px;
            padding: 0 15px;
        }
        #site-nav a { color: #00e; }
        #trailer .modal-dialog {
            margin-top: 80px;
            width: 640px;
            max-width: 95%;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
            font-size: 28px;
            line-height: 1;
            color: #fff;
            text-decoration: none;
            text-shadow: 0 0 4px #000;
            background: #333;
            border-radius: 50%;
            width: 32px;
            height: 32px;
            text-align: center;
        }
        #trailer-video { width: 100%; height: 100%; }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
            min-height: 420px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .movie-tile img {
            width: 220px;
            height: 342px;
            object-fit: cover;
            background: #ddd;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function () {
            $("#trailer-video-container").empty();
        });
        $(document).on('click', '.movie-tile[data-trailer-youtube-id]', function () {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id');
            if (!trailerYouTubeId || trailerYouTubeId === 'None') { return; }
            var sourceUrl = 'https://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&rel=0';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'src': sourceUrl,
              'allow': 'autoplay; encrypted-media',
              'allowfullscreen': true,
              'frameborder': 0
            }));
        });
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).nextAll(".movie-tile").first().show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-label="Close">&times;</a>
          <div class="scale-media" id="trailer-video-container"></div>
        </div>
      </div>
    </div>

    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <a class="navbar-brand" href="/movies/fresh_tomatoes.html">Pixar Movies: A Compilation</a>
        </div>
      </div>
    </div>

    <div id="site-nav">
      <p><a href="/index.html">antonrasmussen.github.io:</a> &gt;
         <a href="/articles.html">Articles</a> &gt; Pixar Trailers</p>
    </div>

    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="/movies/{poster_image_url}" alt="{movie_title} poster" width="220" height="342" referrerpolicy="no-referrer">
    <h2>{movie_title}</h2>
</div>
'''


def create_movie_tiles_content(movies):
    content = ''
    for movie in movies:
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url or '')
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url or '')
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else '')
        if not trailer_youtube_id:
            continue

        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    output_path = os.path.join(os.path.dirname(__file__), 'fresh_tomatoes.html')
    with open(output_path, 'w', encoding='utf-8') as output_file:
        rendered_content = main_page_content.format(
            movie_tiles=create_movie_tiles_content(movies))
        output_file.write(main_page_head + rendered_content)

    url = os.path.abspath(output_path)
    webbrowser.open('file://' + url, new=2)
