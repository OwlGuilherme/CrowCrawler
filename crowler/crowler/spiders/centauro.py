import scrapy
from crowler.rules.rules import CentauroRules
import json
from utils.db_act import salvar_dados


class CentauroSpider(scrapy.Spider):
    name = "centauro"
    allowed_domains = ["centauro.com.br"]

    def start_requests(self):
        with open('crowler/rules/centauro.json', 'r') as file:
            data = json.load(file)
            urls = data.get('urls', [])

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    rules = CentauroRules()

    def parse(self, response):

        name = response.selector.xpath(self.rules.name_selector).get()
        price = response.selector.xpath(self.rules.price_selector).get()

        self.data = {
            'name': name.strip() if name else 'Nome não encontrado',
            'price': price.strip() if price else 'Preço não encontrado'
        }

        #print(f'Nome: {self.data['name']}')
        #print(f'Preço: {self.data['price']}')

        salvar_dados(self.data['name'], self.data['price'], 'Centauro')

