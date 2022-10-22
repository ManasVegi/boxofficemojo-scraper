# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    title = scrapy.Field()
    gross = scrapy.Field()
    theatres = scrapy.Field()
    release_date = scrapy.Field()
    distributor = scrapy.Field()
    opening = scrapy.Field()
    budget = scrapy.Field()
    running_time = scrapy.Field()
    mpaa = scrapy.Field()
    genres = scrapy.Field()
