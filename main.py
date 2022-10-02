from bs4 import BeautifulSoup 
import requests

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'it', 'accelerator', 'raspberry', 'блокчейн']
URL = 'https://habr.com/ru/all/'

response = requests.get(URL)
html = response.text

soup = BeautifulSoup(html, features='html.parser')

#Вывести в консоль список подходящих статей в формате: <дата> - <заголовок> - <ссылка>#
articles = soup.find_all('article')
#articles = soup.find_all(class_="tm-articles-list__item")
for article in articles:
    time = article.find('time').get('title')
    h2 = article.find('h2').find('span').text
    href = article.find('h2').find('a').get('href')
    text = ''.lower()
    response_full = requests.get(f'https://habr.com{href}')
    soup_full = BeautifulSoup(response_full.text, features='html.parser')
    posts = soup_full.find('div', {'id':'post-content-body'})
    for word in KEYWORDS:
        if word in posts.text.lower():
            print(f'{time} - {h2} - https://habr.com{href}, слово {word}')
            break

 