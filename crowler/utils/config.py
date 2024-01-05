from crowler.rules.rules import (
    AmazonRules,
    CentauroRules,
    DeclathonRules,
    MagazineLuizaRules,
    MercadoLivreRules,
    NetshoesRules,
    ShopeeRules,
)

SITE_RULES = {
    "mercadolivre": MercadoLivreRules(),
    "netshoes": NetshoesRules(),
    "amazon": AmazonRules(),
    "centauro": CentauroRules(),
    "declathon": DeclathonRules(),
    "magazineluiza": MagazineLuizaRules(),
    "shopee": ShopeeRules(),
}
