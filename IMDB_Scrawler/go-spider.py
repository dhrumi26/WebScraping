from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from Amitabh.spiders.amitabh_movies import AmitabhMoviesSpider

process = CrawlerProcess(get_project_settings())
process.crawl(AmitabhMoviesSpider)
process.start()