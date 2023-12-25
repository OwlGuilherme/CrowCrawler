from utils.db_act import criar_tabela
from utils.config import SITE_RULES
from scrapy.crawler import CrawlerProcess
from crowler.spiders.mercadoLivre import MercadolivreSpider
from crowler.spiders.amazon import AmazonSpider


criar_tabela()

def choose_site():
    print("Escolha o site que deseja raspar:")
    print("1. Amazon")
    print("2. Mercado Livre")
    '''print("3. Netshoes")
    print("4. Centauro")'''

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

def main():
    site_key = choose_site()
    site_rules = SITE_RULES.get(site_key)

    if site_rules:
        process = CrawlerProcess(settings={
            'DOWNLOAD_DELAY': 3
        })

        if site_key == 'amazon':
            process.crawl(AmazonSpider, rules=site_rules)
        elif site_key == 'mercadolivre':
            process.crawl(MercadolivreSpider, rules=site_rules)

        process.start()

        print("Dados salvos no banco de dados com sucesso.")
    else:
        print(f"Regras não encontradas para o site: {site_key}")

if __name__ == "__main__":
    main()

