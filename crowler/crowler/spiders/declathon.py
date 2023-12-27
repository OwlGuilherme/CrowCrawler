import scrapy
from crowler.rules.rules import DeclathonRules
import json
from utils.db_act import salvar_dados


class DeclathonSpider(scrapy.Spider):
    name = "declathon"
    allowed_domains = ["declathon.com.br"]
    start_urls = ["https://declathon.com.br"]

    def parse(self, response):
        pass
