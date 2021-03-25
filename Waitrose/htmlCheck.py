#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 10:27:04 2021

@author: kathrynhewitt
"""
import requests
from bs4 import BeautifulSoup
import framework

result = requests.get("https://www.waitrose.com/ecom/products/essential-waitrose-fairtrade-bananas/088528-45453-45454")
src = result.content
soup = BeautifulSoup(src, 'lxml')   

url = "https://www.waitrose.com/ecom/products/essential-waitrose-fairtrade-bananas/088528-45453-45454"
    
productNames = []
prices = []
amounts = []
pricePers = []

for price in soup.find_all('span',{'data-test':'product-pod-price'}):
    prices.append(price.text.strip())
print(prices)


for amount in soup.find_all('span', {'class':'size___2HSwr sizeMessage___3o5Ri'}):
    amounts.append(amount.text.strip())
print(amounts)

      

for pricePer in soup.find_all('span',{'class':'pricePerUnit___1L8TG'}):
    pricePers.append(pricePer.text.strip())
print(pricePers)


"""
Created on Thu Jan  7 09:37:59 2021
@author: kathrynhewitt
python3

framework containing all the functions for the webscraper
functions will be called in the main.py
"""
import requests 
from bs4 import BeautifulSoup
from datetime import date
from openpyxl import Workbook

start = "£"
end = "p"
end2 = "est."
s = "s"
g = "g"
h = "h"
kg = "kg"
minn = "min "
minn2 = "minimum"
typicalWeight = "Typical weight"   
each = "each"
slashkg = "/kg"
peach = "p each"
per100 = "/100g"
pper100 = "p/100g"
pkg = "p/kg"
og = "0g"

def getInformation():
    result = requests.get(url)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    
    for productName in soup.find_all('span',{'class':'name___30fwb'}):
        productNames.append(productName.text.strip())
        print(productNames)
    
    for price in soup.find_all('span',{'data-test':'product-pod-price'}):
       # prices.append(price.text.strip())
        #print(prices)
        newPrice = price.text.strip()
        if newPrice[0] in start:
            splitPrice = newPrice.split('£')[1]
            #print(splitPrice)
            prices.append(splitPrice)
        elif newPrice[-1] in end:
                splitPrice = newPrice.split('p')[0]
                intsplitPrice = int(splitPrice)
                finalPrice = (intsplitPrice/100)
                #print(finalPrice)
                prices.append(splitPrice)
        elif newPrice[-1] in end2:
                splitPrice = newPrice.split('p')[0]
                intsplitPrice = int(splitPrice)
                finalPrice = (intsplitPrice/100)
                #print(finalPrice)
                prices.append(splitPrice)
        else:
            #print(newPrice)
            prices.append("null")
    print(prices)

    for amount in soup.find_all('span', {'class':'size___2HSwr sizeMessage___3o5Ri'}):
        newAmount = amount.text.strip()
        if newAmount[-1] in s and newAmount[0] in minn:
            splitAmount = newAmount.split('s')[0]
            splitAmount2 = splitAmount.split('min ')[1]
            #print(splitAmount2)
            amounts.append(splitAmount2)
        #5s    
        elif newAmount[-1] in s:
            splitAmount = newAmount.split('s')[0]
            #print(splitAmount)
            amounts.append(splitAmount)
        #each 
        elif newAmount == each:
            newAmount = 1
            #print(newAmount)
            amounts.append(newAmount)
        #typical weight 10kg
        elif newAmount[0] in typicalWeight and newAmount[-2] in kg:
            splitAmount = newAmount.split('Typical weight ')[1]
            splitAmount2 = splitAmount.split('kg')[0]
            #print(splitAmount2)
            amounts.append(splitAmount2)
        #typical weight 100g
        elif newAmount[0] in typicalWeight and newAmount[-1] in g:
            splitAmount = newAmount.split('Typical weight ')[1]
            splitAmount2 = splitAmount.split('g')[0]
            intsplitAmount = int(splitAmount2)
            finalAmount = (intsplitAmount/1000)
            #print(finalAmount)
            amounts.append(finalAmount)
        #100g    
        elif newAmount[-1] in g:
            splitAmount = newAmount.split('g')[0]
            intsplitAmount = int(splitAmount)
            finalAmount = (intsplitAmount/1000)
            #print(finalAmount)
            amounts.append(finalAmount)
        #min 6
        elif newAmount[0] in minn:
            splitAmount = newAmount[-1:]
            #print(splitAmount)
            amounts.append(splitAmount)
        #minimum 6
        elif newAmount[0] in minn2:
            splitAmount = newAmount[-1:]
            #print(splitAmount)
            amounts.append(splitAmount)
        #all else
        else:
            #print(newAmount)
            amounts.append("null")
        print(amounts)
        
        
    
    for pricePer in soup.find_all('span',{'class':'pricePerUnit___1L8TG'}):
        newPriceP = pricePer.text.strip()
        newPriceP2 = newPriceP[1:-1]
        #50p each
        if newPriceP2[-1] in peach:
            splitPriceP = newPriceP2.split('p each')[0]
            inte = float(splitPriceP)
            finalPriceP = (inte/100)
            #print(finalPriceP)
            pricePers.append(finalPriceP)
        #£1/kg
        elif newPriceP2[0] in start and newPriceP2[-2] in kg:
            splitPriceP = newPriceP2.split('£')[1]
            splitPriceP2 = splitPriceP.split('/kg')[0]
            #print(splitPriceP2)
            pricePers.append(splitPriceP2)
        #£1/100g    
        elif newPriceP2[0] in start and newPriceP2[-2] in og:
            splitPriceP = newPriceP2.split('£')[1]
            splitPriceP2 = splitPriceP.split('/100g')[0]          
            inte = float(splitPriceP2)
            finalPriceP = (inte*10)
            #print(finalPriceP)
            pricePers.append(finalPriceP)
        #50p/100g       
        elif newPriceP2[-2] in og:
            splitPriceP = newPriceP2.split('p/100g')[0]
            inte = float(splitPriceP)
            finalPriceP = (inte/10)
            #print(finalPriceP)
            pricePers.append(finalPriceP)
        #50p/kg   
        elif newPriceP2[-2] in kg:
            splitPriceP = newPriceP2.split('p/kg')[0]
            inte = float(splitPriceP)
            finalPriceP = (inte/100)
            #print(finalPriceP)
            pricePers.append(finalPriceP)
        #else if not found
        else:
            #print("null") 
            pricePers.append("null")
        print(pricePers)
        time.sleep(1)

def createExcel():
    book = Workbook()
    sheet = book.active
    sheet['B1'] = "M&S on Ocado"
    sheet['J1'] = "Waitrose.com"
    rows = (

            (0,'Product Link','Product (my definition)','Website product name', 'Price',
             'Number per pack/weight/size', 'Price per item/kg/Litre', '','',
             'Product Link','Product (my definition)','Website product name', 'Price',
             'Number per pack/weight/size', 'Price per item/kg/Litre')
            )

    for i in range(1,15):
        cellref=sheet.cell(row=2,column=i)
        cellref.value=rows[i]  
    
    today = date.today()
    d4= today.strftime("%b-%d-%Y") 
    #print(d4)
    
    book.save(d4+'_price_comparison.xlsx')

