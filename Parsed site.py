import requests
from bs4 import BeautifulSoup

with open('devices.html', 'r', encoding="utf8") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    names_disordered = soup.find_all("div", {"class":"js-store-prod-name js-product-name t-store__card__title t-name t-name_md"})
    price_disordered = soup.find_all("div", {"class":"js-product-price js-store-prod-price-val t-store__card__price-value notranslate"})

price = list()
names = list()


for i in range(0, len(price_disordered)):
    n = names_disordered[i].text.split('\n')
    p = price_disordered[i].text.split('\n')
    names.append(str(n[0]))
    price.append(str(p[0]))

for i in range(0, len(price_disordered)):
    print(names[i], price[i])
#print(price[0].text)



# Получаем все элементы с классом 'device-name'
#device_names = soup.find('div', {'class':'js-store-prod-name js-product-name t-store__card__title t-name t-name_md'})
# Печатаем имена устройств
# for device_name in device_names:
#     print(device_name.text)