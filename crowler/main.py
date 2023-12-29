#Módulos para manipulação de arquivos
from utils.db_act import criar_tabela
from utils.json_act import escolhe_spyder_json
from utils.config import SITE_RULES
# Spiders
from scrapy.crawler import CrawlerProcess
from crowler.spiders.amazon import AmazonSpider
from crowler.spiders.netshoes import NetshoesSpider
from crowler.spiders.centauro import CentauroSpider
from crowler.spiders.declathon import DeclathonSpider
from crowler.spiders.mercadoLivre import MercadolivreSpider
# Outras bibliotecas
import os


criar_tabela()

def show_menu():
    print("+---------------------------+")
    print("|        CrowCrawler        |")
    print("+---------------------------+")
    print("|    O que desejar fazer?   |")
    print("+- - - - - - - - - - - - - -+")
    print("| 1. WebScrapping           |")
    print("| 2. Adicionar link         |")
    print("| 3. Encerrar execução      |")
    print("+---------------------------+")

    choose = input("> ")

    if choose == '1':
        go_scrapping()
    elif choose == '2':
        os.system("clear")
        escolhe_spyder_json()


def go_scrapping():
    
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
        elif site_key == 'centauro':
            process.crawl(CentauroSpider, rules=site_rules)
        elif site_key == 'netshoes':
            process.crawl(NetshoesSpider, rules=site_rules)
        elif site_key == 'declathon':
            process.crawl(DeclathonSpider, rules=site_rules)

        process.start()

        print("Dados salvos no banco de dados com sucesso.")
    else:
        print(f"Regras não encontradas para o site: {site_key}")


def choose_site():

    print("+-----------------------------------+")
    print("|            CrowCrawler            |")
    print("+-----------------------------------+")
    print("| Escolha o site que deseja raspar: |")
    print("+- - - - - - - - - - - - - - - - - -+")
    print("| 1. Amazon                         |")
    print("| 2. Inativo                        |")
    print("| 3. Inativo                        |")
    print("| 4. Centauro                       |")
    print("| 5. Declathon                      |")    
    print("+-----------------------------------+")

    choice = input("> ")

    if choice == '1':
        return 'amazon'
    #elif choice == '2':
        #return 'mercadolivre'
    #elif choice == '3':
        #return 'netshoes'
    elif choice == '4':
        return 'centauro'
    elif choice == '5':
        return 'declathon'
    else:
        print("Escolha inválida. Por favor, escolha 1 ou 4.")
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
        elif site_key == 'centauro':
            process.crawl(CentauroSpider, rules=site_rules)
        elif site_key == 'netshoes':
            process.crawl(NetshoesSpider, rules=site_rules)
        elif site_key == 'declathon':
            process.crawl(DeclathonSpider, rules=site_rules)

        process.start()

        print("Dados salvos no banco de dados com sucesso.")
    else:
        print(f"Regras não encontradas para o site: {site_key}")

if __name__ == "__main__":
    main()

