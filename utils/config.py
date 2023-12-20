from utils.rules import MercadoLivreRules, NetshoesRules, AmazonRules

SITE_RULES = {
    'mercadolivre': MercadoLivreRules(),
    'netshoes': NetshoesRules(),
    'amazon' : AmazonRules()
}