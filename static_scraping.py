"""
2. 静的なWebページのスクレイピング
必要な知識:
requestsを用いたWebページの取得方法
BeautifulSoupを使ったHTMLの解析とデータの抽出

問題:
以下の架空のWebページを考えます。

<!-- saved_page.html -->
<html>
    <head><title>Sample Page</title></head>
    <body>
        <h1>Welcome to the Sample Page</h1>
        <ul>
            <li><a href="/page1">Page 1</a></li>
            <li><a href="/page2">Page 2</a></li>
            <li><a href="/page3">Page 3</a></li>
        </ul>
    </body>
</html>

このsaved_page.htmlから、次の情報を抽出するPythonプログラムを書いてください。

<h1>タグのテキスト内容
<a>タグのテキストとhref属性の値のリスト
"""

import requests
from bs4 import BeautifulSoup

html_content = """
<html>
    <head><title>Sample Page</title></head>
    <body>
        <h1>Welcome to the Sample Page</h1>
        <ul>
            <li><a href="/page1">Page 1</a></li>
            <li><a href="/page2">Page 2</a></li>
            <li><a href="/page3">Page 3</a></li>
        </ul>
    </body>
</html>
"""

# HTMLをパースする
soup = BeautifulSoup(html_content, 'html.parser')

# 1. <h1>タグのテキスト内容
one = soup.h1.text
print(one)

# 2. <a>タグのテキストとhref属性の値のリスト
all_a = soup.find_all('a')
for a in all_a:
	print(f"Text: {a.text}, href: {a['href']}")
