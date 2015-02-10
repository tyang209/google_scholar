# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field



class GoogleScholarItem(Item):
	AuthorNames= Field()
	Title = Field()
	Year = Field()
	Source= Field()
	Journal = Field()
	ArticleURL = Field()
	CitesURL=Field()
	Cites = Field()
	ClusterID = Field()
