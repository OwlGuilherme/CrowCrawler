from utils.db_act import criar_tabela, salvar_dados, obter_dados
from utils.webscrap import scrape_site
from utils.config import SITE_RULES

def main():
    site_url = 'https://produto.mercadolivre.com.br/MLB-3489320777-relogio-smart-esportivo-tranya-s2-resistente-agua-3atm-_JM#polycard_client=recommendations_home_navigation-trend-recommendations&reco_backend=machinalis-homes-pdp-boos&reco_client=home_navigation-trend-recommendations&reco_item_pos=2&reco_backend_type=function&reco_id=2d7a2e3a-dd92-46da-accc-472e7945eaa5'
    site_rules = SITE_RULES.get('mercadolivre')

    if site_rules:
        data = scrape_site(site_url, site_rules)
        print(data)
    
    else:
        print("Regras não encontratas para o site.")

if __name__ == "__main__":
    main()


