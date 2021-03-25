import requests
from bs4 import BeautifulSoup
import time

productNames = []
prices = []
amounts = []
pricePers = []

attempts = 0
attempts2 = 0
attempts3 = 0

urls = ["https://www.ocado.com/products/m-s-tomato-basil-sauce-528271011"]

for url in urls:
    result = requests.get(url)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    while attempts < 2:
        try:
            name = soup.find('h2', {'class': ''}).next_element
            print(name)
        except AttributeError:
            print("i encountered and error try again")
            time.sleep(2)
            continue
        else:
            break
    else:
        print("0")

    while attempts2 < 2:
        try:
            price = soup.find('h2', {'class': 'bop-price__current'})
            print(price.text.strip())
        except AttributeError:
            print("i encountered and error try again")
            time.sleep(2)
            attempts2 += 1
            continue
        else:
            break
    else:
        print("0")

    while attempts3 <2:
        try:
            amount = soup.find('span', {'class': 'bop-catchWeight'})
            print(amount.text.strip())
        except AttributeError:
            print("i encountered and error try again")
            time.sleep(2)
            attempts3 += 1
            continue
        else:
            break
    else:
        print("0")
