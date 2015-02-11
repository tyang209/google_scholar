from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.spider import Spider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy import Selector
from google_scholar.items import GoogleScholarItem
import re

class scholarSpider(Spider):
	name = "scholar"
	allowed_domains = ["google.com"]
	start_urls=["https://scholar.google.com/scholar?as_q=&as_epq=Kyoto+University&as_oq=&as_eq=&as_occt=any&as_sauthors=&as_publication=&as_ylo=2000&as_yhi=&btnG=&hl=en&as_sdt=0%2C33"
	]

	rules = (Rule ())
	def parse(self, response):
		items = []
		hxs = Selector(text=response.body,type="html")
		for div in hxs.xpath("//div[contains(@class,'gs_ri')]"):
			
			item = GoogleScholarItem()

			item['Title']=div.xpath("h3/a/text()").extract()
			item['ArticleURL'] = div.xpath("h3/a/@href").extract()
			identifiers = div.xpath("div[contains(@class,'gs_a')]/descendant-or-self::text()")

			names = ""
			for text in identifiers:
				names += text.extract()
			item['AuthorNames'] = names.split('-')[0]
			#journal year may not contain journal so it's either
			#Nature, 2001 or just 2001
			#split on comma and use length to determine value
			print names.split('-')
			journal_year = names.split('-')[1]

			if len(journal_year.split(',')) ==1:
				item['Year'] = journal_year.split(',')[0]
			else:
				item['Journal'] = journal_year.split(',')[0]
				item['Year'] = journal_year.split(',')[1]

			item['Source'] = names.split('-')[2]
			cites_block = div.xpath("div[contains(@class,'gs_fl')]//a")[0]
			cites_link = cites_block.xpath("@href").extract()[0]
			item['CitesURL'] = cites_link
			cites = cites_block.xpath("text()").extract()[0]

			if cites =="Cite":
				cites_num = 0
			else:
				cites_num = int(cites.replace("Cited by ",""))
			item['Cites'] = cites_num

			pattern= re.compile(r"cites=(\d+)")
			item['ClusterID'] = re.search(pattern,cites_link).group(1)

			items.append(item)
		return items

