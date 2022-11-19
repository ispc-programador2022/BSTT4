import mysql.connector as coneccion

class basesdatosdb:

    def __init__(self) -> None:
        try:
            connection = coneccion.connect(
                host='181.28.157.113',
                port='3306',
                user='root',
                password='ar200441256',
                db='cienciasdatos'
            )

            if connection.is_connected():
                print("exito")
                cursor=connection.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS datos( iddatos INT NOT NULL, PRIMARY KEY (iddatos));")
        except Exception as ex:
            print(ex)
        finally:
            if connection.is_connected():
                connection.close()