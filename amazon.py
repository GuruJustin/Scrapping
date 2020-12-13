import sys
import os

os.chdir("C:/Users/sos/AppData/Roaming/Python/Python39/site-packages/")
sys.path.append("C:/Users/sos/AppData/Roaming/Python/Python39/site-packages/")

from bs4 import BeautifulSoup
import requests
import cloudscraper
import re 
import pprint
from operator import itemgetter

#############################

def price_sort(item):
    return item.get('price')

# searchinput = sys.argv[1]
searchinput = "note+8"

#############################
#scraper = cloudscraper.create_scraper()
#scraper = cloudscraper.CloudScraper()
searchinput = input("Enter your value: ")
print (searchinput)

itemlist = []

for i in range(1,10):
    ebayUrl = "https://www.ebay.com/sch/i.html?_from=R40&_nkw="+searchinput+"&_sacat=0&_pgn="+str(i)
    f = requests.get(ebayUrl)
    s = BeautifulSoup(f.content, 'html.parser')
    f.close

    itemarr = s.findAll("div", {"class" : "s-item__wrapper clearfix"})

    print (len(itemarr))
    print (ebayUrl)

    if (len(itemarr) > 0) :
        for item in itemarr :
            itemDetail = {}

            itemDetail['title'] = item.findAll("h3", {})[0].text
            itemDetail['description'] = item.findAll('div', {'class' : 's-item__subtitle'})[0].text
            itemDetail['url'] = item.findAll("a",{})[0].get('href')
            itemDetail['img'] = item.findAll("img", {"class" : "s-item__image-img"})[0].get('src')

            itemDetail['price'] = item.findAll("span", {'class', "s-item__price"})[0].text
            itemDetail['price'] = ''.join(x for x in itemDetail['price'] if x.isdigit())

            itemlist.append(itemDetail)
    else :
        break
print ("=========================")
itemlist.sort(key=price_sort)
# print(itemlist, end='\n\n')
pprint.pprint(itemlist[0:10])

# items = []
# listings = s.find_all('li', attrs={'class': 's-item'})

# for listing in listings:
#     temp_item = {}
#     prod_name=" "
#     prod_price = " "

#     print (listing)
#     break
    
#     # temp_item['description'] = listing.findAll('div', {'class' : 's-item__subtitle'})[0].text
#     # temp_item['url'] = listing.findAll("a",{})[0].get('href')
#     # temp_item['img'] = listing.findAll("img", {"class" : "s-item__image-img"})[0].get('src')

#     for name in listing.find_all('h3', attrs={'class':"s-item__title"}):
#         if(str(name.find(text=True, recursive=False))!="None"):
#             prod_name=str(name.find(text=True, recursive=False))
#             temp_item['name'] = prod_name

#     if(prod_name!=" "):
#         price = listing.find('span', attrs={'class':"s-item__price"})
#         prod_price = str(price.find(text=True, recursive=False))
#         # prod_price = int(re.sub(",","",prod_price.split("руб.")[1].split(".")[0]))
#         # prod_price = int(sub(",","",prod_price.split("INR")[1].split(".")[0]))

#         temp_item['price'] = ''.join(x for x in prod_price if x.isdigit())
#     items.append(temp_item)
# # if (len(s.findAll("div", {"class": "mw-search-result-heading"})) > 0) :
# # 	firsturl = s.findAll("div", {"class": "mw-search-result-heading"})[0].findAll("a")[0]["href"]
# # 	print(firsturl)
# print (items)
# pprint.pprint(items)
# sys.stdout.flush()
