# Importar librerías
import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml

url_inicial = 'https://datosmacro.expansion.com/ipc-paises/argentina?sector=IPC+General&sc=IPC-IG&anio=2017'

# Pedido a la página
r = requests.get(url_inicial)

# Armamos la sopa
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup)

# Tabla
rows = soup.find('table', attrs={"id":"tb1_415"}).find('tbody').find_all('tr')
# print(rows)

mes = []
interanual = []
acum = []
var_m = []
for row in rows:
    mes.append(row.find_all('td')[0].get_text())
    interanual.append(row.find_all('td')[1].get_text())
    acum.append(row.find_all('td')[3].get_text())
    var_m.append(row.find_all('td')[5].get_text())

# print(mes)
# print(interanual)
# print(acum)
# print(var_m)

# Convertimos datos a un DataFrame
df = pd.DataFrame({'mes':mes, 'interanual':interanual, 'acum': acum, 'var_m':var_m})
print(df)

# Exportamos el DataFrame
df.to_csv('Tabla 2016-2017')
