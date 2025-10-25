import json
import os
import re
from datetime import datetime

# 入力ファイルと出力先設定
input_file = "data/resources_summarized.json"
articles_dir = "public/articles"
html_dir = "public"

os.makedirs(articles_dir, exist_ok=True)
os.makedirs(html_dir, exist_ok=True)

# データ読み込み
if not os.path.exists(input_file):
    print("❌ resources_summarized.json が見つかりません。")
    exit(1)

with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# スラッグ生成関数
def slugify(title):
    slug = re.sub(r'[^a-zA-Z0-9]+', '-', title.lower()).strip('-')
    return slug[:50]

# 各記事HTMLを生成
for i, item in enumerate(data, start=1):
    title = item.get("title", "No Title")
    link = item.get("link", "")
    summary = item.get("summary_short", "")
    source = item.get("source", "")
    published = item.get("published", "")
    slug = f"{i:03d}-{slugify(title)}"

    article_html = f"""
    <html>
    <head><meta charset='utf-8'><title>{title}</title></head>
    <body>
        <h1>{title}</h1>
        <p><b>Source:</b> {source}</p>
        <p><b>Published:</b> {published}</p>
        <p>{summary}</p>
        <p><a href="{link}" target="_blank">Original article →</a></p>
        <p><a href="../index.html">← Back to list</a></p>
    </body>
    </html>
    """

    html_path = os.path.join(articles_dir, f"{slug}.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(article_html)

print(f"✅ {len(data)} 個の記事HTMLを生成しました: {articles_dir}")

# 一覧ページもHTMLで作る
index_html = os.path.join(html_dir, "index.html")
html_body = "".join(
    f"<li><a href='articles/{i+1:03d}-{slugify(d['title'])}.html'>{d['title']}</a></li>"
    for i, d in enumerate(data)
)
html = f"<html><body><h1>🧠 AI Directory Index</h1><ul>{html_body}</ul></body></html>"

with open(index_html, "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ 一覧HTMLも生成しました: {index_html}")