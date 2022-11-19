import mysql.connector as coneccion

try:
    connection = coneccion.connect(
        host='181.28.157.113',
        port='3306',
        user='root',
        password='ar200441256',
        db='cienciasdatos'
    )

    if connection.is_connected():
        print("exitosa")
except Exception as ex:
    print(ex)