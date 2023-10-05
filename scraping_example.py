import requests
from bs4 import BeautifulSoup

# ページのデータの取得: アクセスしたページからHTMLやXMLデータを取得します。
URL = 'http://books.toscrape.com/'
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

# 各書籍の情報が<article class="product_pod">内にあるので、それを取得
books = soup.find_all('article', class_='product_pod')

for book in books:
    # タイトルの取得
    title = book.find('h3').find('a').get('title')
    # 価格の取得
    price = book.find('p', class_='price_color').text
    print(f"Title: {title}, Price: {price}")
