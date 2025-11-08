# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YtscraperItem(scrapy.Item):
    title = scrapy.Field()
    channel = scrapy.Field()
    views = scrapy.Field()
    description = scrapy.Field()
    video_url = scrapy.Field()
    local_path = scrapy.Field()

    