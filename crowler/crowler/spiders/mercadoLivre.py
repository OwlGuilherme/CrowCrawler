import json
import scrapy
from crowler.rules.rules import MercadoLivreRules
from utils.db_act import salvar_dados

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

        self.data = {
            'name': name.strip() if name else 'Nome não encontrado',
            'price': price.strip() if price else 'Preço não encontrado'
        }

        salvar_dados(self.data['name'], self.data['price'])

