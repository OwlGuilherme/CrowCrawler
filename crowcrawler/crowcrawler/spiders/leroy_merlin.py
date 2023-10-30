import manipul_db
import scrapy


class LeroyMerlinSpider(scrapy.Spider):
    name = "leroy_merlin"
    allowed_domains = ["leroymerlin.com.br"]
    start_urls = ["https://leroymerlin.com.br"]

    def parse(self, response):
        pass
