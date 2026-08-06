# Site build

```bash
cd ~/repos/antonrasmussen.github.io
pip install -r requirements.txt   # once
python3 scripts/build_site.py
```

Writes `articles/*.html`, regenerates `articles.html`, year indexes, and `feed.xml` from `content/posts/*.md`.

# Content

Posts live in `content/posts/YYYY-MM-DD-slug.md` with YAML front matter (`date`, `title`, `source`, `status`, `visibility`, `section`, `tags`). Only `visibility: public` and `status: published|ready` are built.

# Private vault

Archive importers live in `~/repos/writing_vault` (not part of this Pages deploy).
