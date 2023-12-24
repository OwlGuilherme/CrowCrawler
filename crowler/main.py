import json
from utils.db_act import criar_tabela, salvar_dados
from utils.webscrap import scrape_site
from utils.config import SITE_RULES

criar_tabela()

def load_urls_from_json(file_path='urls.json'):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data.get('urls', [])

def choose_site():
    print("Escolha o site que deseja raspar:")
    print("1. Amazon")
    print("2. Mercado Livre")
    print("3. Netshoes")
    print("4. Centauro")

    choice = input("Digite o número correspondente ao site desejado: ")

    if choice == '1':
        return 'amazon'
    elif choice == '2':
        return 'mercadolivre'
    elif choice == '3':
        return 'netshoes'
    elif choice == '4':
        return 'centauro'
    else:
        print("Escolha inválida. Por favor, escolha 1, 2, 3 ou 4.")
        return choose_site()

def filter_urls_by_site(urls, site_key):
    return [url for url in urls if site_key in url]

def main():
    site_key = choose_site()
    site_rules = SITE_RULES.get(site_key)

    if site_rules:
        # Lista de URLs a serem raspadas
        urls = load_urls_from_json()
        filtered_urls = filter_urls_by_site(urls, site_key)

        if not filtered_urls:
            print(f"Não há URLs para o site {site_key}. Encerrando.")
            return

        for site_url in filtered_urls:
            data = scrape_site(site_url, site_rules)
            print(data)

            nome_produto = data.get('name', 'Nome não encontrado')
            preco_atual = data.get('price', 'Preço não encontrado')

            if 'R$' in preco_atual:
                preco_atual = preco_atual.replace('R$', '').strip()

            # Substituir vírgulas por pontos no preço
            preco_atual = preco_atual.replace(',', '.')

            salvar_dados(nome_produto, preco_atual)
            print("Dados salvos no banco de dados com sucesso para", site_url)
    else:
        print(f"Regras não encontradas para o site: {site_key}")

if __name__ == "__main__":
    main()
