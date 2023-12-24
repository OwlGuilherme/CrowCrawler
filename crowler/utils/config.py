from utils.rules import MercadoLivreRules, NetshoesRules, AmazonRules, CentauroRules

SITE_RULES = {
    'mercadolivre': MercadoLivreRules(),
    'netshoes': NetshoesRules(),
    'amazon' : AmazonRules(),
    'centauro' : CentauroRules()
}