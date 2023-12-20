# webscrap.py
from bs4 import BeautifulSoup
import requests
from utils.config import SITE_RULES

def scrape_site(site_url, rules):
    response = requests.get(site_url)
    html_content = response.text

    soup = BeautifulSoup(response.content, 'html.parser')

    # Modifique as linhas abaixo para usar o método `select` com XPath
    name_elements = soup.select(rules.name_selector)
    price_elements = soup.select(rules.price_selector)

    # Extrair o texto dos elementos
    name = name_elements[0].text.strip() if name_elements else 'Nome não encontrado'
    price = price_elements[0].text.strip() if price_elements else 'Preço não encontrado'

    return {'name': name, 'price': price}
