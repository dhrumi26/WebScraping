import scrapy
from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/'] # urls of the websites that we want to scrap
    # we are not supposed to change this two variables name because scrapy.Spider wants us to keep it same as above

    def parse(self, response):
        # # responce varible contains the source code of the web site that we want to scrap.
        # # Selector : Selector actually a condition using we can extract the data from site
        # # Two types of Selector : CSS, XPath
        # # XPath Exaplt code : response.xpath('//title/text()').extract()
        # # output : ['Quotes to Scrape']
        # title = response.css('title::text').extract()
        # yield {'titletext' : title}
        # # We are using yield instead of return because yield is usually used with the generateor 
        # # And this generator is being used by the scrapy behind the scenes

        items = QuotetutorialItem()   # storing data in this container
        # crawling the whole quote section with all details 
        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items

# Combination of theo selectors 
# response.css("li.next a").xpath("@href").extract()    here condition is that look for li tagname,next classname which contains a tag
# and xpath selector is saying that we want the href value 
# output : ['/page/2/']


# If you want to save output in json,xml or csv file 
# use command : scarpy crawl quotes -o items.csv for csv file 
# items.json for json file and same for xml
