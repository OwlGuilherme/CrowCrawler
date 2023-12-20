import json
from utils.db_act import criar_tabela, salvar_dados
from utils.webscrap import scrape_site
from utils.config import SITE_RULES

criar_tabela()

def load_urls_from_json(file_path='urls.json'):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data.get('urls', [])

def main():
    # Lista de URLs a serem raspadas
    urls = load_urls_from_json()

    for site_url in urls:
        # Obtenha as regras do site a partir do mapeamento SITE_RULES
        site_rules_key = None
        for key, rules in SITE_RULES.items():
            if key in site_url:
                site_rules_key = key
                break

        if site_rules_key:
            site_rules = SITE_RULES.get(site_rules_key)
            data = scrape_site(site_url, site_rules)
            print(data)

            nome_produto = data.get('name', 'Nome não encontrado')
            preco_atual = data.get('price', 'Preço não encontrado')

            if 'R$' in preco_atual:
                preco_atual = preco_atual.replace('R$', '').strip()

            # Substituir vírgulas por pontos no preço
            preco_atual = preco_atual.replace(',', '.')

            salvar_dados(nome_produto, preco_atual)
            print("Dados salvos no banco de dados com sucesso")
        else:
            print("Regras não encontradas para o site")

if __name__ == "__main__":
    main()
