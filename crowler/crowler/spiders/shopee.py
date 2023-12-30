import scrapy
from crowler.rules.rules import ShopeeRules
import json
from utils.db_act import salvar_dados, obter_ultimo_preco, preprocessar_preco


class ShopeeSpider(scrapy.Spider):
    name = "shopee"
    allowed_domains = ["shopee.com.br"]

    def start_requests(self):
        with open('crowler/rules/shopee.json', 'r') as file:
            data = json.load(file)
            urls = data.get('urls', [])

            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)

    rules = ShopeeRules()


    def parse(self, response):

        name = response.selector.xpath(self.rules.name_selector).get()
        price = response.selector.xpath(self.rules.price_selector).get()

        print(f'Nome: {name}')
        print(f'Preço: {price}')

        price = preprocessar_preco(price)


         # Verificar mudança de preço antes de salvar
        if self.verificar_mudanca_de_preco(name, float(price), 'Shopee'):
            salvar_dados(name, float(price), 'Shopee')

    def verificar_mudanca_de_preco(self, name, novo_preco, site, margem_tolerancia=0.05):
        ultimo_preco = obter_ultimo_preco(name, site)

        if ultimo_preco is None:
            return True

        diferenca_percentual = abs((novo_preco - ultimo_preco) / ultimo_preco)
        return diferenca_percentual > margem_tolerancia

