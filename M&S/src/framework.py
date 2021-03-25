import requests
from bs4 import BeautifulSoup


def getProductName(url):
    if url == None:
        productNames.append('none')
    else:
        result = requests.get(url)
        src = result.content
        soup = BeautifulSoup(src, 'lxml')

        # ProductNames
        try:
            name = soup.find('h2', {'class': ''}).next_element
            # print(name)
            productNames.append(name)
        except:
            productNames.append('none')


def getProductPrice(url):
    if url == None:
        productNames.append('none')
    else:
        result = requests.get(url)
        src = result.content
        soup = BeautifulSoup(src, 'lxml')

        try:
            price = soup.find('h2', {'class': 'bop-price__current'})
            # print(price.text.strip())
            productPrices.append(price.text.strip())
        except:
            productPrices.append(0.00)


def getProductAmount(url):
    if url == None:
        productNames.append('none')
    else:
        result = requests.get(url)
        src = result.content
        soup = BeautifulSoup(src, 'lxml')

        try:
            amount = soup.find('span', {'class': 'bop-catchWeight'})
            productAmounts.append(amount.text.strip())
        except:
            productAmounts.append(0.00)