import json
import os
import re
from datetime import datetime

# 入力ファイルと出力先設定
input_file = "data/resources_summarized.json"
content_dir = "nextjs_app/content"
html_dir = "public"

os.makedirs(content_dir, exist_ok=True)
os.makedirs(html_dir, exist_ok=True)

# データを読み込み
if not os.path.exists(input_file):
    print("❌ resources_summarized.json が見つかりません。")
    exit(1)

with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# スラッグ（URLに使える英数字名）を生成する関数
def slugify(title):
    slug = re.sub(r'[^a-zA-Z0-9]+', '-', title.lower()).strip('-')
    return slug[:50]

# 各記事をMarkdown化
for i, item in enumerate(data, start=1):
    title = item.get("title", "No Title")
    link = item.get("link", "")
    summary = item.get("summary_short", "")
    source = item.get("source", "")
    published = item.get("published", "")
    slug = f"{i:03d}-{slugify(title)}"

    md_content = f"""---
title: "{title}"
date: "{published}"
source: "{source}"
link: "{link}"
---

{summary}
"""

    md_path = os.path.join(content_dir, f"{slug}.md")
    with open(md_path, "w", encoding="utf-8") as md_file:
        md_file.write(md_content)

print(f"✅ {len(data)} 個のMarkdown記事を生成しました: {content_dir}")

# 一覧ページもついでにHTML出力（前と同じ）
index_html = os.path.join(html_dir, "index.html")
html_body = "".join(
    f"<li><a href='../nextjs_app/content/{i+1:03d}-{slugify(d['title'])}.md'>{d['title']}</a></li>"
    for i, d in enumerate(data)
)
html = f"<html><body><h1>AI Directory Index</h1><ul>{html_body}</ul></body></html>"

with open(index_html, "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ 一覧HTMLも生成しました: {index_html}")
