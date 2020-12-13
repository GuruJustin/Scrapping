import sys
import os

os.chdir("C:/Users/sos/AppData/Roaming/Python/Python39/site-packages/")
sys.path.append("C:/Users/sos/AppData/Roaming/Python/Python39/site-packages/")

from bs4 import BeautifulSoup
import requests
import cloudscraper
import re 
import numpy

item_name = []
prices = []

for i in range(1,10):

    ebayUrl = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=iphone&_sacat=0&_pgn="+str(i)
    r= requests.get(ebayUrl)
    data=r.text
    soup=BeautifulSoup(data)

    listings = soup.find_all('li', attrs={'class': 's-item'})

    for listing in listings:
        prod_name=" "
        prod_price = " "
        for name in listing.find_all('h3', attrs={'class':"s-item__title"}):
            if(str(name.find(text=True, recursive=False))!="None"):
                prod_name=str(name.find(text=True, recursive=False))
                item_name.append(prod_name)

        if(prod_name!=" "):
            price = listing.find('span', attrs={'class':"s-item__price"})
            prod_price = str(price.find(text=True, recursive=False))
            # prod_price = int(re.sub(",","",prod_price.split("INR")[1].split(".")[0]))
            prices.append(prod_price)

from scipy import stats
import numpy as np

data_note_8 = pd.DataFrame({"Name":item_name, "Prices": prices})
data_note_8 = data_note_8.iloc[np.abs(stats.zscore(data_note_8["Prices"])), 3,]