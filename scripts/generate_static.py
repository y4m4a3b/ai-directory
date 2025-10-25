import json, os, re
input_file = "data/resources_summarized.json"
html_dir = "public"
os.makedirs(html_dir, exist_ok=True)
if not os.path.exists(input_file):
    print("❌ resources_summarized.json が見つかりません。")
    exit(1)
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)
def slugify(title):
    return re.sub(r'[^a-zA-Z0-9]+', '-', title.lower()).strip('-')[:50]
index_html = os.path.join(html_dir, "index.html")
html_body = "".join(f"<li><a href='{d.get('link','#')}' target='_blank'>{d.get('title','No Title')}</a><p>{d.get('summary_short','')}</p></li>" for d in data)
html = f"<html><head><meta charset='utf-8'><title>AI Directory</title></head><body><h1>AI Directory</h1><ul>{html_body}</ul></body></html>"
with open(index_html, "w", encoding="utf-8") as f:
    f.write(html)
print("✅ 一覧HTMLを生成しました:", index_html)

