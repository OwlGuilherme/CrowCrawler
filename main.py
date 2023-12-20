from utils.db_act import criar_tabela, salvar_dados, obter_dados
from utils.webscrap import scrape_site
from config import SITE_RULES

def main():
    site_url = 'https://www.mercadolivre.com.br/produto-exemplo'
    site_rules = SITE_RULES.get('mercadolivre')

    if site_rules:
        data = scrape_site(site_url, site_rules)
        print(data)
    
    else:
        print("Regras não encontratas para o site.")

if __name__ == "__main__":
    main()


