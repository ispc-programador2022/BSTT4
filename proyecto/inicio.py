import pandas as pd
import os
import csv

dirActual=os.getcwd()

with open(dirActual + "/proyecto/precios_en_surtidor.csv","r") as arch:
    lectura = csv.reader(arch, delimiter=",")
    
    contador =0 
    for rows in lectura:
        print(rows.count)
        print(rows[1])
        contador+=1
        if contador>3:
            break
