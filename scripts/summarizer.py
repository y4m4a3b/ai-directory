import json
import os
import re

# 要約を作る簡易関数（AIなし版）
def simple_summarize(text, max_sentences=2):
    """文章から冒頭の数文を抜き出して簡易要約を作る"""
    text = re.sub(r'<[^>]+>', '', text)  # HTMLタグ除去
    sentences = re.split(r'(?<=[。.!?])\s*', text)
    summary = ' '.join(sentences[:max_sentences]).strip()
    return summary if summary else text[:200]  # 文字数が短い場合の補正

# JSONファイルの読み込み
input_file = "data/resources.json"
output_file = "data/resources_summarized.json"

if not os.path.exists(input_file):
    print("❌ resources.json が見つかりません。まず scraper.py を実行してください。")
    exit(1)

with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# 各エントリに summary_short フィールドを追加
for item in data:
    item["summary_short"] = simple_summarize(item.get("summary", ""))

# 新しいファイルとして保存
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ 要約付きデータを保存しました: {output_file}")

