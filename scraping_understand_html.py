"""
1. 基本的なHTMLの理解
必要な知識:

HTMLの基本的な構造（開始タグ、終了タグ、属性など）
代表的なタグ（<div>, <a>, <p>, <img> など）

問題:
以下のHTMLを考えます。
<div>
    <p class="description">This is a description.</p>
    <a href="http://example.com">Visit our site</a>
    <img src="image.jpg" alt="Sample Image">
</div>

1. 上記のHTMLから、<a>タグのhref属性の値を教えてください。
2. <img>タグのsrc属性の値は何ですか？
3. <p>タグにはどのようなクラスが付与されていますか？
"""
from bs4 import BeautifulSoup

# ページのデータの取得: アクセスしたページからHTMLやXMLデータを取得します。
html_content = """
<div>
    <p class="description">This is a description.</p>
    <a href="http://example.com">Visit our site</a>
    <img src="image.jpg" alt="Sample Image">
</div>
"""

# HTMLをパースする
soup = BeautifulSoup(html_content, 'html.parser')

# 1. <a>タグのhref属性の値
one = soup.find('a', href="http://example.com")
print(one['href'])

# 2. <img>タグのsrc属性の値
two = soup.find('img', src="image.jpg")
print(two['src'])

# <p>タグにはどのようなクラスが付与されていますか？
three = soup.find('p', class_="description")
print(three['class'])

