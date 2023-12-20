from bs4 import BeautifulSoup
import requests
from config import SITE_RULES

def scrape_site(site_url, rules):
    response = requests.get(site_url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')
    name = soup.select_one(rules.name_selector).text.strip()
    price = soup.select_one(rules.price_selector).text.strip()

    return {'name': name, 'price': price}