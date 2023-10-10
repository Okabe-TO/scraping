"""
ログインが必要なサイトのスクレイピング
必要な知識:

セッションとは何か
requests.Session()の基本的な使い方
Seleniumを使用したブラウザの自動操作方法
問題:

http://quotes.toscrape.com/login は、ログインが必要なサンプルサイトの一部です。このサイトでは、以下の認証情報を使用してログインできます:

Username: user
Password: pass

このサイトにログインして、ダッシュボード上の名言、著者、およびタグを抽出するPythonプログラムを作成してください。

ファイル名: login_scraping.py

この問題を解決するために、まずSeleniumを使ってブラウザを操作し、ログインページに入力し、ログインボタンをクリックする操作をシミュレートすることを考慮してください。その後、名言、著者、およびタグを抽出します。
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

# URLの値を束縛
url = 'http://quotes.toscrape.com/login'

# 1. ブラウザを起動
driver = webdriver.Chrome()
driver.get(url)

# ユーザー名とパスワードを入力
driver.find_element(By.ID, 'username').send_keys('user')  # IDやname属性を使って要素を特定
driver.find_element(By.ID, 'password').send_keys('pass')

# ログインボタンをクリック
driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

# ログイン後のソース確認
# print(driver.page_source)

# ダッシュボードからメッセージを抽出(ソースを見た感じ、ユーザーダッシュボードがどれかわからない。こんにちは、[username]！というメッセージはどこだろう？)
all_quotes = driver.find_elements(By.CLASS_NAME, 'quote')
for quote in all_quotes:
  text = quote.find_element(By.CLASS_NAME, 'text').text
  author = quote.find_element(By.CLASS_NAME, 'author').text
  tags = [tag.text for tag in quote.find_elements(By.CLASS_NAME, 'tag')]
  print(f"{text}\nby {author}\nTags: {' '.join(tags)}\n")

# ブラウザを閉じる
driver.quit()
