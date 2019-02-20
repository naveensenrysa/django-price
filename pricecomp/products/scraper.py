import requests
from bs4 import BeautifulSoup

from products.models import *
from products.serializers import *

class Scraper(object):

    def __init__(self, **kwargs):
        self.platform = kwargs['marketplace_name']
        self.url = kwargs['url']
        self.ndh_price = kwargs['ndh_price']
        self.scrape_id = kwargs['scarape_id']

    def amazon(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        page = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')

        price_data = {}

        # DealPrice of Amazon Block
        if(soup.find("span", {"id": "priceblock_dealprice"})): 
            price_data['dealprice'] = soup.find("span", {"id": "priceblock_dealprice"}).get_text().strip()
        
        # Saleprice of Amazon Block
        elif(soup.find("span", {"id": "priceblock_saleprice"})):
            price_data['saleprice'] = soup.find("span", {"id": "priceblock_saleprice"}).get_text().strip()
        
        # Ourprice Amazon Block
        else:
            price_data['ourprice'] = soup.find("span", {"id": "priceblock_ourprice"}).get_text().strip()
        print(soup.find("span", {"class": "a-text-strike"})) 

        # Amazon MRP  
        price_data['mrp'] = soup.find("span", {"class": "a-text-strike"}).get_text().strip()

        return price_data