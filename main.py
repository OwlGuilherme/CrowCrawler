from utils.db_act import criar_tabela, salvar_dados, obter_dados
from utils.webscrap import scrape_site
from utils.config import SITE_RULES

criar_tabela()

def main():
    site_url = 'https://www.amazon.com.br/Tranya-Smartwatch-Rel%C3%B3gio-inteligente-Bluetooth/dp/B0BDDHB5Q1/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_i=B0BDDHB5Q1'
    site_rules = SITE_RULES.get('amazon')

    if site_rules:
        data = scrape_site(site_url, site_rules)
        print(data)

        nome_produto = data.get('name', 'Nome não encontrado')
        preco_atual = data.get('price', 'Preço não encontrado')
        if 'R$' in preco_atual:
            preco_atual = preco_atual.replace('R$', '').strip()

        salvar_dados(nome_produto, preco_atual)
        print("Dados salvos no banco de dados com sucesso!")

    else:
        print("Houve um erro e não foi possível salvar os dados.")

if __name__ == "__main__":
    main()
