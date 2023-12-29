import json
import os

def salva_link_json(arquivo, novo_link):

    with open(arquivo, 'r') as f:
        dados_json = json.load(f)

    if 'urls' in dados_json and isinstance(dados_json['urls'], list):
        dados_json['urls'].append(novo_link)
    else:
        print("Erro na verificação da chave 'urls'")

    with open(arquivo, 'w') as f:
        json.dump(dados_json, f, indent=2)

def escolhe_spyder_json():

    print("+-----------------------------------+")
    print("|             CrowCrawler           |")
    print("+-----------------------------------+")
    print("| Escolha a spyder que deseja       |")
    print("| acrescentar links:                |")
    print("+- - - - - - - - - - - - - - - - - -+")
    print("| 1. Amazon                         |")
    print("| 2. Inativo                        |")
    print("| 3. Inativo                        |")
    print("| 4. Centauro                       |")
    print("| 5. Declathon                      |")    
    print("+-----------------------------------+")

    nome_arquivo = input("> ")

    if nome_arquivo == '1':
        arquivo = 'amazon'
    elif nome_arquivo == '4':
        arquivo = 'centauro'
    elif nome_arquivo == '5':
        arquivo = 'declathon'
    else:
        print("Escolha inválida, por favor, escolher 1, 4, ou 5")
        os.system('clear')
        escolhe_spyder_json()

    arquivo = f"CrowCrawler/crowler/crowler/rules/{nome_arquivo}.json"

    novo_link = input("Insira o novo link: ")

    salva_link_json(arquivo, novo_link)  

