import scrapy


class NetshoesSpider(scrapy.Spider):
    name = "netshoes"
    start_urls = ["https://www.netshoes.com.br/running/tenis-performance?marca=olympikus"]

    def parse(self, response, **kwargs):
        pass
