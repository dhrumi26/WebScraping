import scrapy
from..items import AmitabhItem

class AmitabhMoviesSpider(scrapy.Spider):
    name = 'amitabh_movies'
    # allowed_domains = ['https://www.imdb.com/name/nm0000821/?ref_=fn_nm_nm_1#actor']
    start_urls = ['https://www.imdb.com/name/nm0000821/?ref_=fn_nm_nm_1#actor/']

    def parse(self, response):
        items = AmitabhItem()
        # for film in all_film_row:
        movie_name = response.css('b a').css('::text').extract()
        # movie_name = response.css('b a::text').extract()
        
        # released_in_year = response.css('.year_column::text').extract()


        items['movie_name'] = movie_name
        yield items

