import requests
from bs4 import BeautifulSoup

productNames = []
prices = []
amounts = []
pricePers = []

attempts = 0

result = requests.get("https://www.ocado.com/products/m-s-tomato-basil-sauce-528271011")
src = result.content
soup = BeautifulSoup(src, 'lxml')


try:
    name = soup.find('h2',{'class':''}).next_element
    print(name)
except AttributeError:
    print("0")

try:
    price = soup.find('h2',{'class':'bop-price__current'})
    print(price.text.strip())
except:
    print("0")
#
try:
    amount = soup.find('span',{'class':'bop-catchWeight'})
    print(amount.text.strip())
except:
    print("0")
