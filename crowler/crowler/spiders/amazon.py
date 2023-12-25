import scrapy
from crowler.rules.rules import AmazonRules
import json
from utils.db_act import salvar_dados


class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["amazon.com.br"]
    
    def start_requests(self):
        with open('crowler/rules/amazon.json', 'r') as file:
            data = json.load(file)
            urls = data.get('urls', [])

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    rules = AmazonRules()

    def parse(self, response):
        name = response.css(self.rules.name_selector + '::text').get()
        price = response.css(self.rules.price_selector + '::text').get()

        self.data = {
            'name': name.strip() if name else 'Nome não encontrado',
            'price': price.strip() if price else 'Preço não encontrado'
        }

        salvar_dados(self.data['name'], self.data['price'])

