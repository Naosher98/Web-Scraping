from bs4 import BeautifulSoup as bs4
import requests
import pandas as pd

pages=[]
prices=[]
stars=[]
titles=[]
urlss=[]

pages_to_scrape=5
for item in pages:
    page = requests.get(item)
    soup = bs4(page.text, 'html.parser')
#     print(soup.prettify())
#     print(type(soup))
    for i in soup.findAll('h3'):
        ttl=i.getText()
#         print(ttl)
        titles.append(ttl)
    for a in soup.findAll('p', class_='instock availability'):
        stock=a.getText().strip()
#         print(stock)
        stocks.append(stock)
    for j in soup.findAll('p', class_='price_color'):
        price=j.getText().strip('Â')
#         print(price)
        prices.append(price)
    for s in soup.findAll('p', class_='star-rating'):
        for k,v in s.attrs.items():
#             print(k, v)
            star =v[1]
#             print(star)
            stars.append(star)

    for h in soup.findAll('h3'):
        w= h.find('a')
        #         print(w['href'])
        url1='http://books.toscrape.com/'+str('catalogue/'+ w['href'])
        #         print(urls)
        page1s.append(url1)
for u1 in page1s:
    page1 = requests.get(u1)
    soup1 = bs4(page1.text, 'html.parser')
    #         print(soup1.prettify())
    divs =soup1.findAll('div', class_='item active')
    for thumb in divs:
        tg=thumb.find('img')
    #             print(tg['src'])
        u='http://books.toscrape.com/'+str(tg['src'])
        n=u.replace("../","")
        newurls= n.strip('../')
    #             print(newurls)
        img_urls.append(newurls)
data={'Title': titles, 'Prices': prices, 'Stars':stars,'Images':img_urls,"Stock":stocks}
df=pd.DataFrame(data=data)
df.index+=1
df
df.to_excel("~/Desktop/output.xlsx")

