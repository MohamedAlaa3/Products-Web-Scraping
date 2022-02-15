from bs4 import BeautifulSoup
import requests
import lxml
from xlwt import *
workbook = Workbook(encoding = 'utf-8')
table = workbook.add_sheet('data',cell_overwrite_ok=True)
table.write(0, 0, 'Mobile Page')
table.write(0, 1, 'Mobile Name')
table.write(0, 2, 'Price')
table.write(0 ,3, 'Company name')
table.write(0 , 4 , 'Mobile Image')
table.write(0 , 5, 'Mobilereate')
table.write(0 , 6, 'price Range')

l = 1
headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
 }
url = 'https://www.jumia.com.eg/mobile-phones/apple/?sort=lowest-price&color_family=Red--Black--Blue--Pink--Purple--White&screen_size=5.4&price=15556-22799#catalog-listing'
html_page = requests.get( url , headers=headers)
soup = BeautifulSoup(html_page.text , 'lxml')
links_list = []
f = 0
Mobiles = soup.find_all('article',{'class':'prd _fb col c-prd'}) 
for Mobile in Mobiles:
    x = Mobile.find('a')
    Murl = 'https://jumia.com.eg' + x['href']
    Mobile_url = Murl
    Mobileurl = requests.get(Murl, headers = headers)
    Mobile_soup = BeautifulSoup(Mobileurl.text , 'lxml')
    Mobile_imgs = Mobile.find('div' , {'class' : 'img-c'})
    pf = Mobile_imgs.find('img').attrs
    pfimg = pf['data-src']
    Mobile_name = Mobile_soup.find('h1' , {'class':'-fs20 -pts -pbxs'})
    if Mobile_name is not None:
      M_name = Mobile_name.text
      price = Mobile_soup.find('span' , {'class' : '-b -ltr -tal -fs24'}).text
      company_name_tr = Mobile_soup.findAll('div' , {'class' : '-pvxs'})
      product_rating = Mobile_soup.find('a' , {'class':'-plxs _more'}).text
      result = ""
      for cp in company_name_tr:
       n = cp.find('a' , {'class' : '_more'})
       if n is not None:
        result = n.text
        break
    
    if l==1:
        min1=price
    
    #print(M_name)
    table.write(l,0,Murl)
    table.write(l,1,M_name)
    table.write(l,2,price)
    table.write(l,3,result)
    table.write(l,4,pfimg)
    table.write(l,5,product_rating)
    l += 1
    max1=price      
range1=min1 +" - "+max1
table.write(1,6,range1)

print("Done")
workbook.save('MobilesData.csv')