import scrapy


class MercadoLivreSpider(scrapy.Spider):
    name = "mercado_livre"
    start_urls = ["https://mercadolivre.com"]

    def parse(self, response, **kawargs):
        pass
