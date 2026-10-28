from bs4 import BeautifulSoup
import requests
import csv

url = 'https://books.toscrape.com/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

title = soup.find("title")
print(title.get_text(separator='', strip=True))

books = soup.find_all('article', class_='product_pod')

for book in books:
    titlebook = book.h3.a['title']
    pricebook = book.find(class_='price_color').get_text(strip=True)

    print(f'{titlebook} - {pricebook}')

with open('books.csv', 'w', newline='', encoding='utf-8') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow([

        'Titulo', 'Preço'

                ])
    for book in books:
        titlebook = book.h3.a['title']
        pricebook = book.find(class_='price_color').get_text(strip=True)
        writer.writerow([f'{titlebook} - {pricebook}'])