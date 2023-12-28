import scrapy
from crowler.rules.rules import AmazonRules
import json
from utils.db_act import salvar_dados, obter_ultimo_preco, preprocessar_preco

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
        name = response.css(self.rules.name_selector + '::text').get().strip()
        price = response.css(self.rules.price_selector + '::text').get()

        price = preprocessar_preco(price)


        # Verificar mudança de preço antes de salvar
        if self.verificar_mudanca_de_preco(name, float(price), 'Amazon'):
            salvar_dados(name, float(price), 'Amazon')

    def verificar_mudanca_de_preco(self, nome, novo_preco, site, margem_tolerancia=0.05):
        ultimo_preco = obter_ultimo_preco(nome, site)

        if ultimo_preco is None:
            return True

        diferenca_percentual = abs((novo_preco - ultimo_preco) / ultimo_preco)
        return diferenca_percentual > margem_tolerancia
