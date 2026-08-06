#!/usr/bin/env python3
"""Build antonrasmussen.github.io articles from Markdown posts.

Preserves the existing Verdana / text-heavy look via templates/article.html.
Sorts and dates posts by front-matter `date` (original write date), not git time.
"""

from __future__ import annotations

import argparse
import html
import re
import sys
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Any

import markdown
import yaml

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content" / "posts"
ARTICLES_DIR = ROOT / "articles"
TEMPLATE = ROOT / "templates" / "article.html"
ARTICLES_INDEX = ROOT / "articles.html"
FEED_PATH = ROOT / "feed.xml"
SITE_URL = "https://antonrasmussen.com"


@dataclass
class Post:
    path: Path
    title: str
    date: date
    body_md: str
    slug: str
    updated: date | None = None
    source: str = "manual"
    tags: list[str] = field(default_factory=list)
    visibility: str = "public"
    status: str = "published"
    original_url: str = ""
    section: str = "writing"  # writing | research | notes

    @property
    def filename(self) -> str:
        return f"{self.date.isoformat()}-{self.slug}.html"

    @property
    def url_path(self) -> str:
        """Absolute path for RSS / canonical URLs."""
        return f"/articles/{self.filename}"

    @property
    def rel_from_root(self) -> str:
        return f"/articles/{self.filename}"

    @property
    def rel_from_articles(self) -> str:
        return f"/articles/{self.filename}"

    @property
    def dateline(self) -> str:
        parts = [self.date.strftime("%B %-d, %Y") if sys.platform != "win32" else self.date.strftime("%B %d, %Y").replace(" 0", " ")]
        if self.source and self.source != "manual":
            parts.append(f"source: {self.source}")
        if self.updated and self.updated != self.date:
            upd = self.updated.strftime("%B %-d, %Y") if sys.platform != "win32" else self.updated.strftime("%B %d, %Y").replace(" 0", " ")
            parts.append(f"updated {upd}")
        return " · ".join(parts)


def parse_date(value: Any) -> date:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        return date.fromisoformat(value[:10])
    raise ValueError(f"Cannot parse date: {value!r}")


def slugify(text: str) -> str:
    s = text.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")[:80] or "post"


def load_post(path: Path) -> Post | None:
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith("---"):
        print(f"skip (no front matter): {path}", file=sys.stderr)
        return None
    parts = raw.split("---", 2)
    if len(parts) < 3:
        print(f"skip (bad front matter): {path}", file=sys.stderr)
        return None
    meta = yaml.safe_load(parts[1]) or {}
    body = parts[2].lstrip("\n")

    visibility = str(meta.get("visibility", "public")).lower()
    status = str(meta.get("status", "published")).lower()
    if visibility != "public" or status not in {"published", "ready"}:
        # ready posts in content/posts are treated as publishable; draft stays out
        if status == "draft" or visibility == "private":
            print(f"skip (not public): {path.name}", file=sys.stderr)
            return None

    title = str(meta.get("title") or path.stem)
    post_date = parse_date(meta["date"])
    updated = parse_date(meta["updated"]) if meta.get("updated") else None
    tags = meta.get("tags") or []
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(",") if t.strip()]

    # Prefer date+slug from filename when present
    m = re.match(r"^(\d{4}-\d{2}-\d{2})-(.+)$", path.stem)
    slug = m.group(2) if m else slugify(str(meta.get("slug") or title))

    return Post(
        path=path,
        title=title,
        date=post_date,
        body_md=body,
        slug=slug,
        updated=updated,
        source=str(meta.get("source") or "manual"),
        tags=list(tags),
        visibility=visibility,
        status="published" if status == "ready" else status,
        original_url=str(meta.get("original_url") or ""),
        section=str(meta.get("section") or "writing"),
    )


def render_body(md_text: str) -> str:
    return markdown.markdown(
        md_text,
        extensions=["fenced_code", "tables", "smarty", "sane_lists"],
    )


def render_post(post: Post, template: str) -> str:
    tags_html = ""
    if post.tags:
        joined = ", ".join(html.escape(t) for t in post.tags)
        tags_html = f'<p class="tags">Tags: {joined}</p>'
    return (
        template.replace("{{ title }}", html.escape(post.title))
        .replace("{{ dateline }}", html.escape(post.dateline))
        .replace("{{ body }}", render_body(post.body_md))
        .replace("{{ tags_html }}", tags_html)
    )


def write_articles_index(posts: list[Post]) -> None:
    # Flat chronological list (newest first), including standalone pages.
    # Format: [topic] Title [link], YYYY-MM-DD, Month YYYY.
    entries: list[tuple[date, str, str]] = []  # date, topic, li html

    def topic_li(topic: str, title: str, href: str, when: date) -> str:
        t = html.escape(topic.lower())
        month_year = when.strftime("%B %Y")
        return (
            f'            <li class="article-item" data-topic="{t}">'
            f'<p><a href="#" class="topic-filter" data-topic="{t}">[{t}]</a> '
            f'<b>{html.escape(title)}</b> '
            f'<a href="{html.escape(href)}">[link]</a>, '
            f'{html.escape(month_year)}.</p></li>'
        )

    for p in posts:
        cat = (p.tags[0] if p.tags else p.source or "writing").lower()
        entries.append(
            (p.date, cat, topic_li(cat, p.title, p.rel_from_root, p.date))
        )
    entries.append(
        (
            date(2017, 11, 1),
            "computers",
            topic_li(
                "computers",
                "A Basic Trailer Website",
                "/movies/fresh_tomatoes.html",
                date(2017, 11, 1),
            ),
        )
    )
    entries.sort(key=lambda x: x[0], reverse=True)
    items_html = "\n".join(line for _, _, line in entries)

    topics = sorted({t for _, t, _ in entries})
    topic_filters = ' · '.join(
        f'<a href="#" class="topic-filter" data-topic="{html.escape(t)}">[{html.escape(t)}]</a>'
        for t in topics
    )

    years = sorted({d.year for d, _, _ in entries}, reverse=True)
    year_links = " · ".join(
        f'<a href="/articles/{y}.html">{y}</a>' for y in years
    )

    html_out = f"""<!DOCTYPE html>
<!-- Feel free to use my source! Generated by scripts/build_site.py -->
<html>
<head>
<title>Anton Rasmussen: Articles</title>
<meta charset="utf-8" />
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
</head>

<body>

    <div id="navigator">
        <p><a href="/index.html">antonrasmussen.github.io:</a> > Articles</p>

    </div><!--navigator-->


    <div id="main">

        <h1> Article Index </h1>
        <p>Sorted by original write date. Year archives: {year_links or "(none)"} · <a href="/feed.xml">RSS</a></p>
        <p id="topic-bar">Topics: <a href="#" class="topic-filter" data-topic="">[all]</a> · {topic_filters}</p>

        <ul id="article-list">
{items_html}
        </ul>
        <p id="filter-empty" hidden><i>No articles for this topic.</i></p>
    </div><!--main-->

    <style>

        a {{ color:blue; }}
            a:hover {{ color:red; }}

        h1 {{ font-size:1.1em; text-align:center; }}

        td {{ vertical-align:top; font-size:medium; padding:20px; }}

        ul {{ margin:0; padding:0; }}

        li {{ margin-top:20px; list-style: none; }}

        body {{ font-family:verdana; font-size:medium; text-align:left; }}

            #navigator {{ text-align:left; width:1500px; margin:auto; }}
            #main {{ text-align:left; width:1500px; margin:auto; }}

        .topic-filter.active {{ font-weight: bold; text-decoration: underline; }}

    </style>

    <script>
    (function () {{
      var active = "";
      var items = document.querySelectorAll("#article-list .article-item");
      var empty = document.getElementById("filter-empty");
      var filters = document.querySelectorAll(".topic-filter");

      function apply(topic) {{
        active = topic || "";
        var shown = 0;
        items.forEach(function (li) {{
          var match = !active || li.getAttribute("data-topic") === active;
          li.hidden = !match;
          if (match) shown += 1;
        }});
        empty.hidden = shown > 0;
        filters.forEach(function (a) {{
          var t = a.getAttribute("data-topic") || "";
          a.classList.toggle("active", t === active);
        }});
        if (active) {{
          history.replaceState(null, "", "#topic=" + encodeURIComponent(active));
        }} else {{
          history.replaceState(null, "", location.pathname);
        }}
      }}

      document.addEventListener("click", function (e) {{
        var a = e.target.closest(".topic-filter");
        if (!a) return;
        e.preventDefault();
        var topic = a.getAttribute("data-topic") || "";
        // Clicking the already-active topic clears the filter
        if (topic && topic === active) topic = "";
        apply(topic);
      }});

      var m = location.hash.match(/topic=([^&]+)/);
      if (m) apply(decodeURIComponent(m[1]));
      else apply("");
    }})();
    </script>
</body>
</html>
"""
    ARTICLES_INDEX.write_text(html_out, encoding="utf-8")


def write_year_indexes(posts: list[Post], template: str) -> None:
    by_year: dict[int, list[Post]] = {}
    for p in posts:
        by_year.setdefault(p.date.year, []).append(p)

    for year, group in by_year.items():
        group = sorted(group, key=lambda x: x.date, reverse=True)
        lis = "\n".join(
            f'            <li><p><b>{html.escape(p.title)}</b> — '
            f'<a href="{p.rel_from_articles}">{p.date.isoformat()}</a></p></li>'
            for p in group
        )
        page = f"""<!DOCTYPE html>
<html>
<head>
<title>Anton Rasmussen: {year}</title>
<meta charset="utf-8" />
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
<style>
    a {{ color:blue; }} a:hover {{ color:red; }}
    body {{ font-family:verdana; font-size:medium; text-align:left; }}
    #navigator, #main {{ width:1000px; margin:auto; text-align:left; }}
    li {{ margin-top:12px; }}
</style>
</head>
<body>
    <div id="navigator">
        <p><a href="/index.html">antonrasmussen.github.io:</a> >
        <a href="/articles.html">Articles</a> > {year}</p>
    </div>
    <div id="main">
        <h1>{year}</h1>
        <ul>
{lis}
        </ul>
    </div>
</body>
</html>
"""
        (ARTICLES_DIR / f"{year}.html").write_text(page, encoding="utf-8")


def write_feed(posts: list[Post]) -> None:
    items = []
    for p in posts[:50]:
        body = render_body(p.body_md)
        items.append(
            f"""    <item>
      <title>{html.escape(p.title)}</title>
      <link>{SITE_URL}{p.url_path}</link>
      <guid isPermaLink="true">{SITE_URL}{p.url_path}</guid>
      <pubDate>{p.date.strftime("%a, %d %b %Y")} 12:00:00 GMT</pubDate>
      <description><![CDATA[{body}]]></description>
    </item>"""
        )
    feed = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>Anton Rasmussen</title>
    <link>{SITE_URL}</link>
    <description>Writing and notes from antonrasmussen.com</description>
{chr(10).join(items)}
  </channel>
</rss>
"""
    FEED_PATH.write_text(feed, encoding="utf-8")


def build() -> int:
    CONTENT.mkdir(parents=True, exist_ok=True)
    ARTICLES_DIR.mkdir(parents=True, exist_ok=True)
    template = TEMPLATE.read_text(encoding="utf-8")

    posts: list[Post] = []
    for path in sorted(CONTENT.glob("*.md")):
        post = load_post(path)
        if post:
            posts.append(post)

    posts.sort(key=lambda p: (p.date, p.slug), reverse=True)

    # Clear previously generated dated article pages (keep year indexes rewritten)
    for old in ARTICLES_DIR.glob("*-*-*-*.html"):
        old.unlink()

    for post in posts:
        out = ARTICLES_DIR / post.filename
        out.write_text(render_post(post, template), encoding="utf-8")
        print(f"wrote {out.relative_to(ROOT)}")

    write_articles_index(posts)
    write_year_indexes(posts, template)
    write_feed(posts)
    print(f"index -> {ARTICLES_INDEX.relative_to(ROOT)} ({len(posts)} posts)")
    print(f"feed  -> {FEED_PATH.relative_to(ROOT)}")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    raise SystemExit(build())


if __name__ == "__main__":
    main()
