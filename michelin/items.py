# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class michelinItem(Item):
    # define the fields for your item here like:
    # main_image=Field()
    # other_image_1=Field()
    # other_image_2=Field()
    # prodcut_description=Field()
    # material_description=Field()
    price=Field()
    product_name=Field()
    website=Field()
    description=Field()
    distinction=Field()
    classification=Field()
