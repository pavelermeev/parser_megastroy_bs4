import csv
import re
import requests
from bs4 import BeautifulSoup

from models import Good


def parse(url: str):
    create_csv()
    page = 0
    count_items = 0
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    total = soup.find('div', class_='finds').string
    search_max_goods = re.search(r'\d+', total)
    max_goods = int(search_max_goods.group())
    while max_goods > count_items:
        list_goods = []
        res = requests.get(f'{url}?page={page}')
        soup = BeautifulSoup(res.text, 'lxml')
        goods = soup.find_all('div', class_='wrap')
        for good in goods:
            if count_items >= max_goods:
                break
            id = good.find('div', class_='code')
            price = good.find('meta', itemprop='price')
            href = good.find('a', class_='title')
            if id:
                count_items += 1
                list_goods.append(Good(id=id.string,
                                       name=href.get('title'),
                                       price=price.get('content'),
                                       link=href.get('href')))
        write_csv(list_goods)
        page += 1


def create_csv():
    with open('megastroy.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            'id', 'name', 'price', 'link'
        ])


def write_csv(goods):
    with open('megastroy.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        for good in goods:
            writer.writerow([
                good.id, good.name, good.price, good.link
            ])


if __name__ == '__main__':
    url = input('Вставьте нужный url для парсинга: ')
    parse(url)
