import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl.workbook import Workbook

url = 'https://svetoslavov.bg/%d1%86%d0%b5%d0%bd%d0%b8-%d0%bd%d0%b0-%d0%b4%d0%b8%d0%b7%d0%b5%d0%bb-%d0%bd%d0%b0-%d0%b5%d0%b4%d1%80%d0%be/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

rows = soup.find('table', {'id': 'tablepress-3'}).find('tbody').find_all('tr')

fuels_list = []

for row in rows:
    dic = {}
    dic['Продукт'] = row.find_all('td')[0].text
    dic['Мярка'] = row.find_all('td')[1].text
    dic['Цена'] = row.find_all('td')[2].text
    dic['Акциз'] = row.find_all('td')[3].text
    dic['Данъчна основа'] = row.find_all('td')[4].text
    dic['ДДС 20%'] = row.find_all('td')[5].text
    dic['Крайна цена с ДДС'] = row.find_all('td')[6].text

    fuels_list.append(dic)

for fuel in fuels_list:
    print(f"{fuel['Продукт']} | {fuel['Мярка']} | {fuel['Цена']} | {fuel['Акциз']} | {fuel['Данъчна основа']} | {fuel['ДДС 20%']} | {fuel['Крайна цена с ДДС']}")

df = pd.DataFrame(fuels_list)
df.to_excel('fuel_data.xlsx', index=False)