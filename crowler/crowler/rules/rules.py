class MercadoLivreRules:
    def __init__(self):
        self.name_selector = "///h1[@class='ui-pdp-title']/text()"
        self.price_selector = "//meta[@itemprop='price']/@content"


class NetshoesRules:
    def __init__(self):
        self.name_selector = "//h1[@data-productname]/text()"
        self.price_selector = '//div[@class="default-price"]/span/strong/text()'


class AmazonRules:
    def __init__(self):
        self.name_selector = "#productTitle"
        self.price_selector = ".a-offscreen"


class CentauroRules:
    def __init__(self):
        self.name_selector = '//h1[@data-testid="product-title"]/text()'
        self.price_selector = '//p[@data-testid="price-current"]/text()'


class DeclathonRules:
    def __init__(self):
        self.name_selector = '//h1[@class="desktop-body-regular-text1 text-restructure-primary mb-0"]/text()'
        self.price_selector = (
            '//h2[@class="desktop-heading-title5 text-restructure-primary"]/text()'
        )


class MagazineLuizaRules:
    def __init__(self):
        self.name_selector = "//h1[@data-testid='heading-product-title' and @class='sc-kpDqfm gXZPqL']/text()"
        self.price_selector = "//p[@data-testid='price-value' and @class='sc-kpDqfm eCPtRw sc-hoLEA kXWuGr']/text()"


class ShopeeRules:
    def __init__(self):
        self.name_selector = "//div[@class='_44qnta']//span/text()"
        self.price_selector = "//div[@class='flex items-center nmrSND']//div[@class='flex items-center']//div[@class='pqTWkA']/text()"
