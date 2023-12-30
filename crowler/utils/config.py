from crowler.rules.rules import MercadoLivreRules, NetshoesRules, AmazonRules, CentauroRules, DeclathonRules, MagazineLuizaRules, ShopeeRules

SITE_RULES = {
    'mercadolivre': MercadoLivreRules(),
    'netshoes': NetshoesRules(),
    'amazon' : AmazonRules(),
    'centauro' : CentauroRules(),
    'declathon' : DeclathonRules(),
    'magazineluiza' : MagazineLuizaRules(),
    'shopee': ShopeeRules()
}

