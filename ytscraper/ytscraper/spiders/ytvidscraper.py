import scrapy
import re
import json
from ytscraper.items import YtscraperItem

class YtvidscraperSpider(scrapy.Spider):
    name = "youtube_json"

    def __init__(self, keyword="laptop", limit=10, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.keyword = keyword
        self.limit = int(limit)

    def start_requests(self):
        url = f"https://www.youtube.com/results?search_query={self.keyword}"
        yield scrapy.Request(url, callback=self.parse, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        })

    def parse(self, response):
        pattern = re.compile(r"var ytInitialData = ({.*?});</script>", re.DOTALL)
        match = pattern.search(response.text)

        if not match:
            self.logger.error("ytInitialData not found!")
            return

        data = json.loads(match.group(1))
        contents = data["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"]\
                        ["sectionListRenderer"]["contents"]

        count = 0
        for section in contents:
            items = section.get("itemSectionRenderer", {}).get("contents", [])
            for video in items:
                video_data = video.get("videoRenderer")
                if not video_data:
                    continue

                item = YtscraperItem()
                item["title"] = video_data["title"]["runs"][0]["text"]
                item["video_url"] = f"https://www.youtube.com/watch?v={video_data['videoId']}"
                item["channel"] = video_data.get("ownerText", {}).get("runs", [{}])[0].get("text")
                item["views"] = video_data.get("viewCountText", {}).get("simpleText", "")
                item["description"] = video_data.get("detailedMetadataSnippets", [{}])[0]\
                    .get("snippetText", {}).get("runs", [{}])[0].get("text", "")

                yield item
                count += 1

                if count >= self.limit:
                    return
