import pandas as pd
import os
import csv
import mysql.connector


os.system('cls')

lista=list()

def leerArchivo_csv():    
    dirArctual=os.getcwd()
    archivo =pd.read_csv(dirArctual +"/proyecto/precios_en_surtidor.csv") 
    lectura=archivo.values.tolist()    
    contador=0
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

leerArchivo_csv()
guardarenBaseDatos()
    