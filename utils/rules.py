class MercadoLivreRules:
    def __init__(self):
        self.name_selector = 'h1.ui-pdp-title'
        self.price_selector = 'meta[itemprop="price"]'

class Netshoes:
    def __init__(self):
        self.name_selector = 'h1[data-productname]'
        self.price_selector = 'div.default-price strong'
