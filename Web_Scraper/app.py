from bs4 import BeautifulSoup
import requests
try:
    url = requests.get(
        'https://www.techlandbd.com/pc-components/graphics-card?limit=100')
    url.raise_for_status()
    soup = BeautifulSoup(url.text, 'html.parser')
    cards = soup.find(
        'div', class_='main-products product-grid').find_all('div', class_='product-layout has-extra-button')
    for card in cards:
        title = card.find('div', class_='name').a.text
        price = card.find('div', class_='price').span.text
        print(title, price)
except Exception as e:
    print(e)
