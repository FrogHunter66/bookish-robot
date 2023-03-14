from bs4 import BeautifulSoup
# Main class in html/devices - js-product t-store__card t-col t-col_4 t-align_center t-item
# class for img - t-store__card__img t-store__card__img_second t-img loaded


def data():
    price = list()
    names = list()
    img_src = list()

    with open('devices.html', 'r', encoding="utf8") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        divs = soup.find_all("div", {'js-product t-store__card t-col t-col_4 t-align_center t-item'})

        #names_disordered = soup.find_all("div", {"class":"js-store-prod-name js-product-name t-store__card__title t-name t-name_md"})
        #price_disordered = soup.find_all("div", {"class":"js-product-price js-store-prod-price-val t-store__card__price-value notranslate"})

    for div in divs:
        names.append((div.find("div", {"class":"js-store-prod-name js-product-name t-store__card__title t-name t-name_md"}).text.split('\n'))[0])
        price.append((div.find("div", {"class":"js-product-price js-store-prod-price-val t-store__card__price-value notranslate"}).text.split('\n'))[0])
        img_src.append(str(div.find("img")['data-original']))

data()



# for i in range(0,len(div)):
#     c += 1
#     print('----------------------------------------------')
#     print(names[i])
#     print(price[i])
#     print(img_src[i])


