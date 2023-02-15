import requests
from bs4 import BeautifulSoup
# Main class in html/devices - js-product t-store__card t-col t-col_4 t-align_center t-item
# class for img - t-store__card__img t-store__card__img_second t-img loaded
#
with open('devices.html', 'r', encoding="utf8") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    divs = soup.find_all("div", {'js-product t-store__card t-col t-col_4 t-align_center t-item'})

    names_disordered = soup.find_all("div", {"class":"js-store-prod-name js-product-name t-store__card__title t-name t-name_md"})
    # price_disordered = soup.find_all("div", {"class":"js-product-price js-store-prod-price-val t-store__card__price-value notranslate"})

price = list()
names = list()
img_src = list()
img = list()
c = 0
for div in divs:
    # names.append((div.find("div", {"class":"js-store-prod-name js-product-name t-store__card__title t-name t-name_md"}).text.split('\n'))[0])
    # price.append((div.find("div", {"class":"js-product-price js-store-prod-price-val t-store__card__price-value notranslate"}).text.split('\n'))[0])
    img_src.append(str(div.find("img")['data-original']))
    img.append(div.find('img'))





for i in range(0,177):
    c += 1

    print(c)
    print(img_src[i])
    print(img[i])

# for i in range(0, len(price_disordered)):
#     print(names[i], price[i])


