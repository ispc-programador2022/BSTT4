import pandas as pd
import os
import csv
import mysql.connector


limpiar = os.system('cls')


def cargarDatosTabla():
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
            sql = "INSERT INTO datosestaciones (periodo) VALUES (%s)"
            val=('2010')
            cursor.execute(sql,val)
            conexion.commit()
            conexion.close()



    except Exception as ex:
        print(ex)
    finally:
        conexion.close()
cargarDatosTabla()



#def crear_connexion():
 #   try:
#        connection=coneccion.connect(
#             host='181.28.157.113',
#             port='3306',
#             user='root',
#             password='ar200441256',
#             db='cienciasdatos'
#        )
#        if connection.is_connected():
#            return connection
#        else:
#            connection.close()
#            return None
#    except Exception as ex:       
#        return None
#def cargarTabla():
    
    #if conexion==None:
    #    print("error de conexion")
    #    quit()
    #else:
    #    cursor= conexion.cursor()
        
    #    sql = "INSERT INTO datosestaciones (periodo) VALUES (%s)"    
    #    val = ('2010')
    #    cursor.execute(sql, ("hola"))  
    #    conexion.close()
#    try:
 #       connection = coneccion.connect(
  #          host='181.28.157.113',
  #            port='3306',
     #         user='root',
   #           password='ar200441256',
   #           db='cienciasdatos'
   #       )       
  #        if connection.is_connected():
   #           cursor=connection.cursor()
   #           cursor.execute("CREATE TABLE IF NOT EXISTS datos( iddatos INT NOT NULL, PRIMARY KEY (iddatos));")
  #            
   #   except Exception as ex:
    #          print(ex)
    #  finally:
    #          if connection.is_connected():
   #               connection.close()
#def tomarDatosCsv():
 #   dirActual=os.getcwd()

#with open(dirActual + "/proyecto/precios_en_surtidor.csv","r") as arch:
#    lectura = csv.reader(arch, delimiter=",")
 
#    contador =0 
#    for rows in lectura:
#        print(rows.count)
#        print(rows[1])
#        contador+=1
#        if contador >3:
#            break