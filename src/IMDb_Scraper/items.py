# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ImdbScraperItem(Item):
    title = Field()
    category = Field()
    year = Field()
    rating = Field()
    description = Field()
    url = Field()
    image_url = Field()
    
