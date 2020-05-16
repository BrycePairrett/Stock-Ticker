#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:06:32 2020

@author: bryce
"""


from bs4 import BeautifulSoup
import requests
import time

tickers = ['GOOG', 'FB', 'TSLA', 'DKLA', 'COST', 'AMZN']

stock_dict = {}

#function to get content from the webpage
def get_html(url):
   #sending the request to the webpage
   html = requests.get(url)
   #returns the html page
   return html.content
#funcion to extract information
def extract_info(html, ticker):
    try:
        soup = BeautifulSoup(html, 'html5lib')

        name = soup.find('h1').text
        price = soup.find_all(class_='Trsdu(0.3s)')[0].text
        change = soup.find_all(class_='Trsdu(0.3s)')[1].text
        
        print(f'Name: {name}')
        print(f'Price: ${price}')
        print(f'Change: {change}')
        print()
#for if ticker is not found        
    except AttributeError:
        print(f'WARNING: Stock not found - skipping {tickers[number - 1]}')
        print()
    
    try:       
        for company in tickers:             
            stock_dict[name] = 'Price: ' + price + ' Change: ' + change
#avoid the calling price and change before assigned as variables
    except UnboundLocalError:
        pass
       
#index the correct ticker for incorrect tickers
number = 0
#for each element in the list
for company in tickers:
   number += 1
   #get the url
   html = get_html(f'https://finance.yahoo.com/quote/{company}')
   #call the function   
   
   extract_info(html, company)
   time.sleep(2)


