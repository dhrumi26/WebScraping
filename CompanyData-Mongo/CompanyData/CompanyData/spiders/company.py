import scrapy
from..items import CompanydataItem


class CompanySpider(scrapy.Spider):
    name = 'company'
    # allowed_domains = ['https://en.wikipedia.org/wiki/Apple_Inc.']
    start_urls = ['https://en.wikipedia.org/wiki/Apple_Inc./',
                'https://en.wikipedia.org/wiki/Microsoft',
                'https://en.wikipedia.org/wiki/Facebook%2C_Inc.',
                'https://en.wikipedia.org/wiki/Amazon_(company)',
                'https://en.wikipedia.org/wiki/Infosys',
                'https://en.wikipedia.org/wiki/Samsung_Electronics',
                'https://en.wikipedia.org/wiki/Tesla%2C_Inc.',
                'https://en.wikipedia.org/wiki/Oracle_Corporation',
                'https://en.wikipedia.org/wiki/Tata_Consultancy_Services',
                'https://en.wikipedia.org/wiki/OnePlus']

    def parse(self, response):
        items = CompanydataItem()
        Company_name = response.css('.org::text').extract()
        Type_Of_Company = response.css('.category > a::text').extract()
        founder = response.css('.agent li > a:nth-child(1)::text').extract()

        items['Company_name'] = Company_name
        items['Founders'] = founder
        items['Type_Of_Company'] = Type_Of_Company
        yield items
