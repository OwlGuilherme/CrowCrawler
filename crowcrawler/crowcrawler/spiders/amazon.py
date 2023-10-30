import scrapy


class AmazonSpider(scrapy.Spider):
    name = "amazon"
    start_urls = []

    csv_file_name = "links_amazon.csv"

    with open(csv_file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for linha in csv_reader:
            link = linha[0]
            start_urls.append(link)

    def parse(self, response, **kawargs):
        nome = response.xpath('//span[@id="productTitle"]/text()').get()

        int_preço = response.xpath('//span[@class="a-price-whole"]/text()').get()
        virg_preço = virgula = response.xpath('//span[@class="a-price-decimal"]/text()').get()
        cent_preço = centavos = response.xpath('//span[@class="a-price-fraction"]/text()').get()

        preço = int_preço + virg_preço + int_preço if virg_preço and cent_preço else int_preço


        yield{
                'preço' : preço,
            'nome' : nome
        }

        manipul_db.create_db()
        manipul_db.save_to_DB(nome, preço)
