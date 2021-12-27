import random
import time
from time import sleep
import requests
from bs4 import BeautifulSoup
import json
import csv
import os
from fake_useragent import UserAgent

with open('img.html', 'r', encoding='utf-8') as file:
    page = file.read()

soup = BeautifulSoup(page, 'html.parser')

list_url_data = soup.find(id='divLoadMore').find_all('div')
# print(list_url_data[0])

url_one_pars = []
for div in list_url_data:
    if div.find('a') != None:
        url_one_pars.append('https://www.yeniavaz.com' + div.find('a').get('href'))

print(url_one_pars)