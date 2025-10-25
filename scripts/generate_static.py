import json, os, re

# 入力ファイルと出力ディレクトリ
input_file = "data/resources_summarized.json"
html_dir = "docs"
articles_dir = os.path.join(html_dir, "articles")

# フォルダ準備
os.makedirs(articles_dir, exist_ok=True)

# JSON読み込み
if not os.path.exists(input_file):
    print("❌ resources_summarized.json が見つかりません。")
    exit(1)

with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# URL用スラッグ生成
def slugify(title):
    return re.sub(r'[^a-zA-Z0-9]+', '-', title.lower()).strip('-')[:50]

# 各記事を個別HTML化
for i, d in enumerate(data, start=1):
    title = d.get("title", "No Title")
    link = d.get("link", "#")
    summary = d.get("summary_short", "")
    slug = f"{i:03d}-{slugify(title)}"
    html_path = os.path.join(articles_dir, f"{slug}.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(f"""<html><head><meta charset='utf-8'><title>{title}</title></head>
<body>
<h1>{title}</h1>
<p>{summary}</p>
<p><a href="{link}" target="_blank">オリジナル記事を読む</a></p>
</body></html>""")

# トップページ生成
index_html = os.path.join(html_dir, "index.html")
html_body = "".join(
    f"<li><a href='articles/{i+1:03d}-{slugify(d['title'])}.html'>{d['title']}</a></li>"
    for i, d in enumerate(data)
)
html = f"<html><head><meta charset='utf-8'><title>AI Directory</title></head><body><h1>AI Directory</h1><ul>{html_body}</ul></body></html>"

with open(index_html, "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ {len(data)} 件の記事を docs に出力しました。")
