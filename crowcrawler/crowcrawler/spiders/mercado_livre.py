import scrapy
import csv

csv_file_name = "links.csv"


class MercadoLivreSpider(scrapy.Spider):
    name = "mercado_livre"
    start_urls = []

    with open(csv_file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for linha in csv_reader:
            link = linha[0]
            start_urls.append(link)

    def parse(self, response, **kawargs):
        pass
