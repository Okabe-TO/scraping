"""
3. ページネーションを持つサイトのスクレイピング
必要な知識:

URLのパターンを理解し、次のページや前のページへのリンクを辿る方法
requestsとBeautifulSoupを組み合わせて、複数ページを順にスクレイピングする方法
問題:
以下の架空のページ構造を考えます。2つのページ（Page 1とPage 2）があり、各ページには数件の商品データがあります。

<!-- page1.html -->
<html>
    <body>
        <div class="product">Product A</div>
        <div class="product">Product B</div>
        <a href="page2.html">Next Page</a>
    </body>
</html>

<!-- page2.html -->
<html>
    <body>
        <div class="product">Product C</div>
        <div class="product">Product D</div>
    </body>
</html>
page1.htmlからスタートし、全ての商品データ（Product A, B, C, D）を抽出するPythonプログラムを書いてください。
"""

import requests
from bs4 import BeautifulSoup

# ファイルを開く
with open('page1.html', 'r', encoding='utf-8') as file:
    html_content1 = file.read()

# HTMLをパースする
soup = BeautifulSoup(html_content1, 'html.parser')

all_d = soup.find_all('div')
for d in all_d:
    print(d.text)

# 次のページURL
url = soup.find('a')['href']

# requestsの代わりにファイルを開く
with open(url, 'r', encoding='utf-8') as file:
    html_content2 = file.read()

# HTMLをパースする
soup = BeautifulSoup(html_content2, 'html.parser')

all_d = soup.find_all('div')
for d in all_d:
    print(d.text)