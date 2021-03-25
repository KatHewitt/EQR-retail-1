import requests
from bs4 import BeautifulSoup
import time

productNames = []
prices = []
amounts = []
pricePers = []

attempts = 0

result = requests.get("https://www.ocado.com/products/m-s-select-farms-lemons-528784011")
src = result.content
soup = BeautifulSoup(src, 'lxml')

for i in range(2):
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

while attempts < 2:
    try:
        price = soup.find('h2',{'class':'bop-price__current'})
        print(price.text.strip())
    except AttributeError:
        print("i encountered and error try again")
        time.sleep(2)
        attempts +=1
        continue
    else:
        break
else:
     print("0")




# try:
#     amount = soup.find('span',{'class':'bop-catchWeight'})
#     print(amount.text.strip())
# except:
#     print("0")
