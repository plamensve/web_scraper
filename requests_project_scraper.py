import requests
import row as row
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl.workbook import Workbook

company_name = input('Въведете името на фирмата:').lower()
urls = {'svetoslavov': 'https://svetoslavov.bg/%d1%86%d0%b5%d0%bd%d0%b8-%d0%bd%d0%b0-%d0%b4%d0%b8%d0%b7%d0%b5%d0%bb-%d0%bd%d0%b0-%d0%b5%d0%b4%d1%80%d0%be/',
        'gtapetroleum': 'https://gtapetroleum.com/%d1%86%d0%b5%d0%bd%d0%b8-%d0%bd%d0%b0-%d0%b5%d0%b4%d1%80%d0%be/'}


for k, v in urls.items():
    if company_name in k:
        response = requests.get(v)
        soup = BeautifulSoup(response.text, 'html.parser')

        if company_name == 'svetoslavov':
            rows = soup.find('table', {'id': 'tablepress-3'}).find('tbody').find_all('tr')

        elif company_name == 'gtapetroleum':
            rows = soup.find('tbody', {'class': 'jet-table__body'}).find_all('tr')

        fuels_list = []

        for row in rows:
            dic = {'Продукт': row.find_all('td')[0].text, 'Мярка': row.find_all('td')[1].text,
                   'Цена': row.find_all('td')[2].text, 'Акциз': row.find_all('td')[3].text,
                   'Данъчна основа': row.find_all('td')[4].text, 'ДДС 20%': row.find_all('td')[5].text,
                   'Крайна цена с ДДС': row.find_all('td')[6].text}

            fuels_list.append(dic)

        for fuel in fuels_list:
            print(f"{fuel['Продукт']} | {fuel['Мярка']} | {fuel['Цена']} | {fuel['Акциз']} | {fuel['Данъчна основа']} | {fuel['ДДС 20%']} | {fuel['Крайна цена с ДДС']}")

        df = pd.DataFrame(fuels_list)
        df.to_excel('fuel_data.xlsx', index=False)