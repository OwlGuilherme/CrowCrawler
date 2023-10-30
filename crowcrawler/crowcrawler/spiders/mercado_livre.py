import scrapy
import csv

class MercadoLivreSpider(scrapy.Spider):
    name = "mercado_livre"
    start_urls = []

    csv_file_name = "links.csv"

    with open(csv_file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for linha in csv_reader:
            link = linha[0]
            start_urls.append(link)

    def parse(self, response, **kawargs):
        preço = response.xpath('//span[@class="andes-money-amount__fraction"]/text()').get()
        título = response.xpath('//h1[@class="ui-pdp-title"]/text()').get()

        yield{
                'preço' : preço,
            'título' : título
        }
