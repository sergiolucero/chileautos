import random, requests
from bs4 import BeautifulSoup

BASE = 'https://chileautos.cl/autos/busqueda?s=%d&l=50'

def scrape_page(id):
    out = []
    for ix in range(5):
        url = BASE %(50*id+ix)
        print(url)
        bs = BeautifulSoup(requests.get(url).text,'lxml')
        heads = [h.find_next('a') for h in bs.find_all('div',attrs={'class':'listing-item__header'})]
        #ps = bs.find_all('div',attrs={'class':"listing-item__features-wrapper"})   # car info
        ps = [p.find_next('p').text for p in bs.find_all('div',attrs={'class':"listing-item__price"})]
        info = [(h.text,h['href'],p) for h,p in zip(heads,ps)]      # level 1: title,url
        out += info
        
    return out
