# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
import yt_dlp

class YtscraperPipeline:
    def process_item(self, item, spider):
        return item
class YoutubeDownloadPipeline:
    def __init__(self):
        self.download_dir = "downloads"
        os.makedirs(self.download_dir, exist_ok=True)

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        video_url = adapter.get("video_url")
        title = adapter.get("title").replace("/", "_").replace("\\", "_")

        try:
            ydl_opts = {
                "outtmpl": f"{self.download_dir}/{title}.%(ext)s",
                "quiet": True,
                "format": "mp4",
                "noplaylist": True,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(video_url, download=True)
                adapter["local_path"] = os.path.join(
                    self.download_dir, f"{title}.{info.get('ext', 'mp4')}"
                )
        except Exception as e:
            spider.logger.error(f"Download failed for {video_url}: {e}")
            adapter["local_path"] = None

        return item