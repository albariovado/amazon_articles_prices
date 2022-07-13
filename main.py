from bs4 import BeautifulSoup
import requests
import lxml

URL = 'article_url'

# find your own header at: http://myhttpheader.com
HEADER = {
    "Accept-Language": "en-GB,en;q=0.9"
}

response = requests.get(URL,headers=HEADER)

soup = BeautifulSoup(response.text,'lxml')

price = soup.find(name='span',class_='a-offscreen') # to know what you need to put into brackets you have to inspect the Amazon site in your browser
price = price.getText() # get the price text tha probably is like '23,78€' or like '$23,78'
price = price[:-1] # remove the currency (if the price have the currency in the first position you have to use [1:])
price = price.split(',')
units = float(price[0])
decimals = float(price[1])*0.01
float_price = units+decimals
print(float_price)
