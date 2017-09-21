import requests
import bs4
import re
lName=[]
lPrice=[]
searchKey=input('Enter search item:')
res=requests.get('http://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords='+searchKey)
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text)
soupName=soup.find_all(lambda tag: tag.name == 'h2' and tag.get('data-attribute'))
for i in range(len(soupName)):
    lName.append(soupName[i].getText())
soupPrice=soup.find_all('span',{'class':'a-size-base a-color-price s-price a-text-bold'})
for i in range(len(soupPrice)):
   lPrice.append(soupPrice[i].getText())
#print(len(lName))
#print(len(lPrice))
#print([s.replace('\\xa', '') for s in lPrice])
lPrice1 = ' '.join(lPrice).replace('\\xa','').split()
#print(lPrice1)
#print(lName)
str="RESULT"
print(str.center(100,'*'))
for i in range(10):
  print(lName[i]+lPrice[i])