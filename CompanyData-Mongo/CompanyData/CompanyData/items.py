# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CompanydataItem(scrapy.Item):
    # define the fields for your item here like:
    Company_name = scrapy.Field()
    Founders = scrapy.Field()
    Type_Of_Company = scrapy.Field()
