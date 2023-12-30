import scrapy


class MagazineluizaSpider(scrapy.Spider):
    name = "magazineLuiza"
    allowed_domains = ["magazineluiza.com.br"]
    start_urls = ["https://magazineluiza.com.br"]

    def parse(self, response):
        pass
