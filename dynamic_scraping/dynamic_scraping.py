"""
4. JavaScriptを用いた動的なページのスクレイピング
必要な知識:

WebページがJavaScriptによって動的にコンテンツをロードする仕組み
WebDriverを使用してブラウザを操作し、動的なコンテンツをロードする方法
Seleniumライブラリの基本的な使い方
まず、Seleniumとブラウザドライバ（この例ではChromeDriver）をインストールする必要があります。以下はその手順です。

Seleniumのインストール:
bash
Copy code
pip install selenium
ChromeDriverのインストール:
ChromeDriverの公式ページから、使用しているChromeのバージョンに合ったChromeDriverをダウンロードしてください。
ダウンロードしたchromedriver.exe（Windowsの場合）を、Pythonのスクリプトと同じディレクトリ、もしくはPATHに含まれるディレクトリに配置してください。
問題:

http://quotes.toscrape.com/js/ は、JavaScriptで動的に引用をロードするサンプルサイトです。

このサイトから、以下のタスクを実行してください：

最初のページの引用文と著者を抽出します。
次のページに進み、そのページの引用文と著者を抽出します。
ファイル名: dynamic_scraping.py

このタスクを解決するためのプログラムを書き、その出力結果も教えてください。
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. ブラウザを起動
driver = webdriver.Chrome()  # Chromeドライバーを使用。他のブラウザも可能。
driver.get('http://quotes.toscrape.com/js/')


try:
    # 2. 引用文と著者を取得 
    all_quotes = driver.find_elements(By.CLASS_NAME, 'quote')
    for quote in all_quotes:
        text = quote.find_element(By.CLASS_NAME, 'text').text
        author = quote.find_element(By.CLASS_NAME, 'author').text
        tags = [tag.text for tag in quote.find_elements(By.CLASS_NAME, 'tag')]
        print(f"{text}\nby {author}\nTags: {' '.join(tags)}\n")

    # 3. 次のページのURLを得て、遷移する
    next_link = driver.find_elements(By.CLASS_NAME, 'next')[0].find_element(By.TAG_NAME, 'a').get_attribute('href')
    driver.get(next_link)
    
    # そのページの引用文と著者を抽出
    all_quotes = driver.find_elements(By.CLASS_NAME, 'quote')
    for quote in all_quotes:
        text = quote.find_element(By.CLASS_NAME, 'text').text
        author = quote.find_element(By.CLASS_NAME, 'author').text
        tags = [tag.text for tag in quote.find_elements(By.CLASS_NAME, 'tag')]
        print(f"{text}\nby {author}\nTags: {' '.join(tags)}\n")

finally:
    # 3. ブラウザを閉じる
    driver.close()