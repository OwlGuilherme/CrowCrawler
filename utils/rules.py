class MercadoLivreRules:
    def __init__(self):
        self.name_selector = 'h1.ui-pdp-title'
        self.price_selector = 'meta[itemprop="price"]'

class NetshoesRules:
    def __init__(self):
        self.name_selector = ''
        self.price_selector = ''

class AmazonRules:
    def __init__(self):
        self.name_selector = '#productTitle'
        self.price_selector = '.a-offscreen'
