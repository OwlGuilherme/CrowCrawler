from typing import Iterable
import scrapy
from scrapy.http import Request
from crowler.rules.rules import MagazineLuizaRules
import json
from utils.db_act import salvar_dados, obter_ultimo_preco, preprocessar_preco


class MagazineluizaSpider(scrapy.Spider):
    name = "magazineLuiza"
    allowed_domains = ["magazineluiza.com.br"]

    def start_requests(self):
        with open ('crowler/rules/magazineluiza.json', 'r') as file:
            data = json.load(file)
            urls = data.get('urls', [])

            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)

    rules = MagazineLuizaRules()
                       

    def parse(self, response):

        name = response.selector.xpath(self.rules.name_selector).get().strip()
        price = response.selector.xpath(self.rules.price_selector).get()

        price = preprocessar_preco(price)

         # Verificar mudança de preço antes de salvar
        if self.verificar_mudanca_de_preco(name, float(price), 'MagazineLuiza'):
            salvar_dados(name, float(price), 'MagazineLuiza')

    def verificar_mudanca_de_preco(self, name, novo_preco, site, margem_tolerancia=0.05):
        ultimo_preco = obter_ultimo_preco(name, site)

        if ultimo_preco is None:
            return True

        diferenca_percentual = abs((novo_preco - ultimo_preco) / ultimo_preco)
        return diferenca_percentual > margem_tolerancia

