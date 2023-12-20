class MercadoLivreRules:
    def __init__(self):
        self.name_selector = 'h1.ui-pdp-title'
        self.price_selector = 'meta[itemprop="price"]'

class NetshoesRules:
    def __init__(self):
        self.name_selector = '//*[@id="content"]/div[2]/section/div[1]/section/h1'
        self.price_selector = '//*[@id="buy-box"]/div[3]/div[2]/div/span[1]/strong'
