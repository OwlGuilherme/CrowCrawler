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
        price = xpath('//*[@id="ui-pdp-main-container"]/div[1]/div/div[1]/div[2]/div[3]/div[1]/div[1]/span[1]/span[3]//text()').get()
        title = xpath('//*[@id="ui-pdp-main-container"]/div[1]/div/div[1]/div[2]/div[1]/div/div[2]/h1//text()').get()

        yield{
                'price' : price,
            'title' : title
        }
