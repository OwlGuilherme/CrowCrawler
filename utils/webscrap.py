# webscrap.py
from bs4 import BeautifulSoup
import requests
from utils.config import SITE_RULES

def scrape_site(site_url, rules):
    response = requests.get(site_url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    # Verifica se o seletor do nome está presente
    name_element = soup.select_one(rules.name_selector)
    name = name_element.text.strip() if name_element else "Nome não encontrado"

    # Verifica se o seletor do preço está presente
    price_element = soup.select_one(rules.price_selector)
    price = price_element.get('content').strip() if price_element else "Preço não encontrado"

    return {'name': name, 'price': price}
