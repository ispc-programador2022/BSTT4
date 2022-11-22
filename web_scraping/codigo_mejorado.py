import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

for x in range(1, 9):

    url_inicial = 'https://datosmacro.expansion.com/ipc-paises/argentina?sector=IPC+General&sc=IPC-IG&anio='

    # Pedido a la página
    r = requests.get(url_inicial + str(2015 + x))

    # Armamos la sopa
    soup = BeautifulSoup(r.text, 'html.parser')
    # print(soup)

    # Tabla
    rows = soup.find('table', attrs={"id": "tb1_415"}).find('tbody').find_all('tr')
    # print(rows)

    mes = []
    interanual = []
    acum = []
    var_m = []
    datos = []
    for row in rows:
        mes.append(row.find_all('td')[0].get_text())
        interanual.append(row.find_all('td')[1].get_text())
        acum.append(row.find_all('td')[3].get_text())
        var_m.append(row.find_all('td')[5].get_text())

    time.sleep(3)

    # Convertimos datos a un DataFrame
    df = pd.DataFrame({'mes': mes, 'interanual': interanual, 'acum': acum, 'var_m': var_m})
    print(df)

# Exportamos el DataFrame
# df.to_csv('Tabla')