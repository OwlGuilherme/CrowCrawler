class MercadoLivreRules:
    def __init__(self):
        self.name_selector = 'h1.ui-pdp-title'
        self.price_selector = 'meta[itemprop="price"]'

class NetshoesRules:
    def __init__(self):
        self.name_selector = 'h1[data-productname]'
        self.price_selector = '.default-price span strong'

class AmazonRules:
    def __init__(self):
        self.name_selector = '#productTitle'
        self.price_selector = '.a-offscreen'

class CentauroRules:
    def __init__(self):
        self.name_selector = '//h1[@class="Typographystyled__Subtitle-sc-bdxvrr-2 kiddsr"]/text()'
        self.price_selector = '//p[@class="Typographystyled__Subtitle-sc-bdxvrr-2 erkEgi Price-styled__CurrentPrice-sc-26a42e8a-4 iXVXIv"]/text()'

