import mysql.connector
from CRUD.DataBase import DataBase

class Main:

    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="drive"
        )

    except Exception:
        print("Usuário ou Senha incorretos")
    
    else:
        cursor = db.cursor()
        # mexer no banco de dados
        cursor.close()
        db.close()
        