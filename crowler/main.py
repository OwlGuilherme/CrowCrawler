import os
import sys

from scrapy.crawler import CrawlerProcess
from utils.config import SITE_RULES
from utils.db_act import criar_tabela, escolher_produto
from utils.graficos import plotar_historico_precos
from utils.json_act import escolhe_spyder_json

from crowler.spiders.amazon import AmazonSpider
from crowler.spiders.centauro import CentauroSpider
from crowler.spiders.declathon import DeclathonSpider
from crowler.spiders.magazineLuiza import MagazineluizaSpider
from crowler.spiders.mercadoLivre import MercadolivreSpider
from crowler.spiders.netshoes import NetshoesSpider


def show_menu_escolha_site():
    while True:
        print("+-----------------------------------+")
        print("|      Digite o site do produto     |")
        print("+- - - - - - - - - - - - - - - - - -+")
        print("| 1. Amazon                         |")
        print("| 2. Magazine Luiza                 |")
        print("| 3. Inativo                        |")
        print("| 4. Centauro                       |")
        print("| 5. Declathon                      |")
        print("| 6. Voltar                         |")
        print("| 7. Sair                           |")
        print("+-----------------------------------+")

        choose = input("> ")
        if choose == "1":
            site = "Amazon"
        elif choose == "2":
            site = "MagazineLuiza"
        elif choose == "4":
            site = "Centauro"
        elif choose == "5":
            site = "Declathon"
        elif choose == "6":
            os.system("clear")
            show_menu()
        elif choose == "7":
            os.system("clear")
            sys.exit(0)
        else:
            os.system("clear")
            print("Opção inválida, por favor, escolha entre 1, 2, 4, 5, 6 ou 7.")
            continue  # Volta ao início do loop

        produto = escolher_produto(site)

        plotar_historico_precos(produto, site)
        os.system("clear")


def show_menu():
    print("+---------------------------+")
    print("|        CrowCrawler        |")
    print("+---------------------------+")
    print("|    O que desejar fazer?   |")
    print("+- - - - - - - - - - - - - -+")
    print("| 1. WebScrapping           |")
    print("| 2. Adicionar link         |")
    print("| 3. Mostrar gráfico        |")
    print("| 4. Sair                   |")
    print("+---------------------------+")

    choose = input("> ")

    if choose == "1":
        os.system("clear")
        go_scrapping()
    elif choose == "2":
        os.system("clear")
        escolhe_spyder_json()
    elif choose == "3":
        os.system("clear")
        show_menu_escolha_site()
    elif choose == "4":
        os.system("clear")
        sys.exit(0)
    else:
        os.system("clear")
        print("Opção inválida, por favor, escolhe entre 1, 2, 3 ou 4.\n")
        show_menu()


def go_scrapping():
    site_key = choose_site()
    site_rules = SITE_RULES.get(site_key)

    if site_rules:
        process = CrawlerProcess(settings={"DOWNLOAD_DELAY": 3})

        if site_key == "amazon":
            process.crawl(AmazonSpider, rules=site_rules)
        elif site_key == "mercadolivre":
            process.crawl(MercadolivreSpider, rules=site_rules)
        elif site_key == "magazineluiza":
            process.crawl(MagazineluizaSpider, rules=site_rules)
        elif site_key == "centauro":
            process.crawl(CentauroSpider, rules=site_rules)
        elif site_key == "netshoes":
            process.crawl(NetshoesSpider, rules=site_rules)
        elif site_key == "declathon":
            process.crawl(DeclathonSpider, rules=site_rules)

        process.start()

        print("Dados salvos no banco de dados com sucesso.")
        return True
    else:
        print(f"Regras não encontradas para o site: {site_key}")
        return False


def choose_site():
    print("+-----------------------------------+")
    print("|            CrowCrawler            |")
    print("+-----------------------------------+")
    print("| Escolha o site que deseja raspar: |")
    print("+- - - - - - - - - - - - - - - - - -+")
    print("| 1. Amazon                         |")
    print("| 2. Magazine Luiza                 |")
    print("| 3. Mercado Livre                  |")
    print("| 4. Centauro                       |")
    print("| 5. Declathon                      |")
    print("| 6. Voltar                         |")
    print("| 7. Sair                           |")
    print("+-----------------------------------+")

    choice = input("> ")

    if choice == "1":
        return "amazon"
    elif choice == "2":
        return "magazineluiza"
    elif choice == "3":
        return "mercadolivre"
    elif choice == "4":
        return "centauro"
    elif choice == "5":
        return "declathon"
    elif choice == "6":
        os.system("clear")
        show_menu()
    elif choice == "7":
        os.system("clear")
        sys.exit(0)
    else:
        os.system("clear")
        print("Escolha inválida. Por favor, escolha 1, 2, 4, 5 ou 6.\n")
        return choose_site()


def main():
    os.system("clear")

    criar_tabela()

    show_menu()
    go_scrapping()


if __name__ == "__main__":
    main()
