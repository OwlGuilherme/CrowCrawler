class MercadoLivreRules:
    def __init__(self):
        self.name_selector = '//*[@id="header"]/div/div[2]/h1'
        self.price_selector = '//*[@id="price"]/div/div[1]/div[1]/span/span/meta'

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