import feedparser
import json
import os

# 保存先ディレクトリを作成
os.makedirs("data", exist_ok=True)

# 収集するRSSフィード一覧
rss_feeds = [
    "https://techcrunch.com/feed/",
    "https://www.theverge.com/rss/index.xml",
    "https://gigazine.net/news/rss_2.0/",
    "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml"
]

all_entries = []

for feed_url in rss_feeds:
    print(f"Fetching: {feed_url}")
    feed = feedparser.parse(feed_url)
    for entry in feed.entries[:10]:  # 各サイトの最新10件
        all_entries.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.get("published", ""),
            "summary": entry.get("summary", ""),
            "source": feed.feed.title if "title" in feed.feed else feed_url
        })

# JSONファイルとして保存
with open("data/resources.json", "w", encoding="utf-8") as f:
    json.dump(all_entries, f, ensure_ascii=False, indent=2)

print(f"\n✅ Done! Collected {len(all_entries)} items.")
print("File saved as: data/resources.json")

