# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class SainsburysItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = Field()
    product_name = Field()
    product_image = Field()
    price_per_unit = Field()
    unit = Field()
    rating = Field()
    product_reviews = Field()
    item_code = Field()
    # nutritions = Field()
    product_origin = Field()
    energy = Field()
    energy_kj = Field()
    kcal = Field()
    fibre_g = Field()
    carbohydrates_g = Field()
    of_which_sugars = Field()
    pass
