from typing import Iterable
import scrapy
import logging
from scrapy.http import Request
from crowler.rules.rules import MercadoLivreRules
import json

logging.getLogger('scrapy').setLevel(logging.ERROR)

class MercadolivreSpider(scrapy.Spider):
    name = "mercadoLivre"
    allowed_domains = ["mercadolivre.com.br"]
    
    def start_requests(self):
        with open('crowler/rules/mercadolivre.json', 'r') as file:
            data = json.load(file)
            urls = data.get('urls', [])

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    rules = MercadoLivreRules()

    def parse(self, response):
        name = response.xpath(self.rules.name_selector).get()
        price = response.xpath(self.rules.price_selector).get()

        yield {
            'name': name.strip() if name else 'Nome não encontrado',
            'price': price.strip() if price else 'Preço não encontrado'
        }

