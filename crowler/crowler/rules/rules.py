class MercadoLivreRules:
    def __init__(self):
        self.name_selector = "///h1[@class='ui-pdp-title']/text()"
        self.price_selector = "//meta[@itemprop='price']/@content"


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
        self.name_selector = 'h1.ui-pdp-title'
        self.price_selector = 'span.andes-money-amount'