# antonrasmussen.github.io

Personal GitHub Pages site for [antonrasmussen.com](https://antonrasmussen.com).

## Layout

```text
/                       # published Pages root
  index.html            # home
  student.html          # studenting / research interests
  articles.html         # article index (generated)
  feed.xml              # RSS (generated)
  CNAME
  articles/             # generated posts + year indexes
  movies/               # published Pixar trailers page + posters/
  CS462/                # course notes (published, unlisted on home)
  portfolio/            # legacy portfolio page
  css/                  # shared styles for course notes
  cryptography.html     # course notes entry
  libraries.html        # redirect stub → articles/
  newWebsite.html       # redirect stub → articles/
  assets/               # images, resume, misc text
  content/posts/        # Markdown sources
  scripts/              # site build + movies generators
  templates/            # article HTML template
```

## Build articles

```bash
cd ~/repos/antonrasmussen.github.io
pip install -r requirements.txt   # once
python3 scripts/build_site.py
```

Writes `articles/*.html`, regenerates `articles.html`, year indexes, and `feed.xml` from `content/posts/*.md`.

Posts live in `content/posts/YYYY-MM-DD-slug.md` with YAML front matter (`date`, `title`, `source`, `status`, `visibility`, `section`, `tags`). Only `visibility: public` and `status: published|ready` are built.

## Regenerate Pixar trailers page

```bash
cd ~/repos/antonrasmussen.github.io
python3 scripts/movies/entertainment_center.py
```

Writes `movies/fresh_tomatoes.html` (posters stay in `movies/posters/`).

## Private vault

Archive importers and personal exports live in `~/repos/writing_vault` (not part of this Pages deploy).
