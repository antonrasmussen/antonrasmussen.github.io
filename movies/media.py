import webbrowser

# Movie class as provided by Udacity's Full-Stack Nanodegree
# Movie Trailers Project: https://classroom.udacity.com/nanodegrees/nd004/

""" 
	Module to display movie object, attributes and instances
"""
class Movie():
	"""
	Class object stores movie related information
	"""

	def __init__(self, 
			movie_title, 
			movie_storyline, 
			poster_image, 
			trailer_youtube):
		"""
		Initialize instances of class Movie

		:param movie_title: string
		:param movie_storyline: string
		:param poster_image: string
		:param trailer_youtube: string
		"""
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		"""
		Initializing instance for opening the youtube video

		:return: webbroswser to play trailer
		"""
		webbrowser.open(self.trailer_youtube_url)