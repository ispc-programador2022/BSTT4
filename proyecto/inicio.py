import pandas as pd
import os
import mysql.connector
import requests
from bs4 import BeautifulSoup
import time

os.system('cls')

lista=list()


def leerArchivo_csv():    
    dirArctual=os.getcwd()
    archivo =pd.read_csv(dirArctual +"/proyecto/precios_en_surtidor.csv") 
    lectura=archivo.values.tolist()   
    for filas in lectura:               
        try:
            vector=[]
            vector.append(filas[0])
            vector.append(filas[1])
            vector.append(filas[3])
            vector.append(filas[8])
            vector.append(filas[9])
            vector.append(filas[12])  
            lista.append(vector)            
        except Exception as ex:
             print("")                     
    
    return lista       

def borrarDatos():
    try:
        conexion= mysql.connector.connect(
            host='181.28.157.113',
             port='3306',
             user='root',
             password='ar200441256',
             db='cienciasdatos'
        )

        if conexion.is_connected():
            cursor= conexion.cursor()                                      
            cursor.execute("set SQL_SAFE_UPDATES=0")
            conexion.commit()
            cursor.execute("DELETE FROM datosestaciones")
            conexion.commit()
            cursor.execute("set SQL_SAFE_UPDATES=1")
            conexion.commit()
            conexion.close()
    except Exception as ex:
        print(ex)
    finally:
        conexion.close()

def guardarenBaseDatos():
    borrarDatos()    

    try:
        
        conexion= mysql.connector.connect(
            host='181.28.157.113',
             port='3306',
             user='root',
             password='ar200441256',
             db='cienciasdatos'
        )

        if conexion.is_connected():                                
            cursor= conexion.cursor()
            sql = "INSERT INTO datosestaciones "\
                   "(periodo, id_empresa, "\
                   "empresa, id_productos, "\
                   "productos, precio) "\
                    "VALUES (%s,%s,%s,%s,%s,%s)"
            cursor.executemany(sql,lista)    
            conexion.commit()            
            conexion.close()
    except Exception as ex:
        print(ex)
    finally:
        conexion.close()

def web_scraping():
    anos=["2016", "2017" , "2018", "2019", "2020", "2021", "2022"]
    mesano={'Enero':'01', 'Febrero':'02', 'Marzo': '03', 'Abril': '04', 'Mayo': '05','Junio':'06', 'Julio':'07', 'Agosto':'08','Septiembre':'09','Octubre':'10','Noviembre':'11','Diciembre':'12'}
    #mesano={"Enero": "01","": 02,"","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" }
    for ano in anos:

        url_inicial = 'https://datosmacro.expansion.com/ipc-paises/argentina?sector=IPC+General&sc=IPC-IG&anio=' + ano
        print (url_inicial)
        # Pedido a la página
        r = requests.get(url_inicial)

        # Armamos la sopa
        soup = BeautifulSoup(r.text, 'html.parser')
        # print(soup)

        # Tabla
        rows = soup.find('table', attrs={"id": "tb1_415"}).find('tbody').find_all('tr')       
        # print(rows)

        

        try:
        
            conexion= mysql.connector.connect(
                host='181.28.157.113',
                port='3306',
                user='root',
                password='ar200441256',
                db='cienciasdatos'
            )
            if  conexion.is_connected():   
                for row in rows:
                    cursor= conexion.cursor()
                    periodo=row.find_all('td')[0].get_text().split()[1] + "-" +\
                    mesano[row.find_all('td')[0].get_text().split()[0]]
                    
                    sqlArc="SELECT * FROM inflacionmensual WHERE periodo LIKE '" + periodo +"'"                   
                    cursor.execute(sqlArc)
                    
                    if len(cursor.fetchall())==0:
                        
                        inter= str(row.find_all('td')[1].get_text()).replace("%","").replace(",",".").replace("--","0.00")
                        acumu= str(row.find_all('td')[3].get_text()).replace("%","").replace(",",".").replace("--","0.00")
                        vari=str(row.find_all('td')[5].get_text()).replace("%","").replace(",",".").replace("--","0.00")
                        if len(acumu)==0:
                            acumu="0.00"
                        else:
                            acumu=acumu

                        sql = "INSERT INTO inflacionmensual "\
                                "(periodo, infacioninteranual, inflacionacumulada, inflacionvariacion) "\
                                "VALUES ('" + periodo + "', "\
                                + inter + ", "\
                                + acumu + ", "\
                                + vari + ")"
                        
                        cursor.execute(sql)
                        conexion.commit()                                                      

                   
            
                    
                conexion.close()
        except  Exception as ex:
            print(ex)
        finally:
            conexion.close()
      

web_scraping()



#leerArchivo_csv()
#guardarenBaseDatos()
    