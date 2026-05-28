#!/usr/bin/env python3
"""
Hacky static blog builder.
Reads _posts/*.md, publishes those whose date <= today to blog/.
"""

import os
import re
from datetime import date

try:
    import markdown
    MD = lambda s: markdown.markdown(s, extensions=['extra'])
except ImportError:
    # Fallback: very basic paragraph wrapping
    def MD(s):
        paras = re.split(r'\n{2,}', s.strip())
        return '\n'.join(f'<p>{p.replace(chr(10), " ")}</p>' for p in paras if p.strip())

MATOMO = """<!-- Matomo -->
<script>
  var _paq = window._paq = window._paq || [];
  _paq.push(['trackPageView']);
  _paq.push(['enableLinkTracking']);
  (function() {
    var u="//matomo.mediavirtuel.com/";
    _paq.push(['setTrackerUrl', u+'matomo.php']);
    _paq.push(['setSiteId', '1']);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
    g.async=true; g.src=u+'matomo.js'; s.parentNode.insertBefore(g,s);
  })();
</script>
<!-- End Matomo Code -->"""

FOOTER = """<address>
  <a href="mailto:eriam@mediavirtuel.com">eriam@mediavirtuel.com</a>
  &middot; <a href="https://github.com/eriam">github.com/eriam</a>
  &middot; <a href="https://linkedin.com/in/eriam">linkedin.com/in/eriam</a>
</address>"""


def parse_post(path):
    with open(path) as f:
        text = f.read()
    if not text.startswith('---'):
        return None
    _, fm_raw, body = text.split('---', 2)
    fm = {}
    for line in fm_raw.strip().splitlines():
        if ':' in line:
            k, v = line.split(':', 1)
            fm[k.strip()] = v.strip()
    return fm, body.strip()


def article_page(title, post_date, body_html):
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>{title} — Eriam Schaffter</title>
{MATOMO}
</head>
<body>

<p><a href="../">← Eriam Schaffter</a> &middot; <a href="./">Articles</a></p>

<h1>{title}</h1>
<p><small>{post_date}</small></p>

<hr>

{body_html}

<hr>

{FOOTER}

</body>
</html>"""


def index_page(posts):
    items = '\n'.join(
        f'  <li><a href="{slug}.html">{title}</a> &mdash; <small>{d}</small></li>'
        for slug, title, d in posts
    )
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Articles — Eriam Schaffter</title>
{MATOMO}
</head>
<body>

<p><a href="../">← Eriam Schaffter</a></p>

<h1>Articles</h1>

<ul>
{items}
</ul>

<hr>

{FOOTER}

</body>
</html>"""


def slug_from_filename(fname):
    # 2026-06-01-mon-article.md → mon-article
    base = os.path.splitext(fname)[0]
    parts = base.split('-', 3)
    return parts[3] if len(parts) == 4 else base


def main():
    today = date.today()
    posts_dir = '_posts'
    blog_dir = 'blog'
    published = []

    for fname in sorted(os.listdir(posts_dir)):
        if not fname.endswith('.md'):
            continue
        parsed = parse_post(os.path.join(posts_dir, fname))
        if parsed is None:
            continue
        fm, body = parsed
        post_date = date.fromisoformat(fm.get('date', '9999-01-01'))
        if post_date > today:
            continue  # not yet

        title = fm.get('title', fname)
        slug = fm.get('slug', slug_from_filename(fname))
        body_html = MD(body)

        out_path = os.path.join(blog_dir, f'{slug}.html')
        with open(out_path, 'w') as f:
            f.write(article_page(title, str(post_date), body_html))

        published.append((slug, title, str(post_date)))
        print(f'  published: {slug}')

    # Sort newest first
    published.sort(key=lambda x: x[2], reverse=True)

    with open(os.path.join(blog_dir, 'index.html'), 'w') as f:
        f.write(index_page(published))
    print(f'index: {len(published)} article(s)')


if __name__ == '__main__':
    main()
