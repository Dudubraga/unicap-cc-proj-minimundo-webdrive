import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    database='drive'
)
cursor = conexao.cursor()

#CRUD -> CREATE READ UPDATE DELATE

def create():
    login = "Carlos777"
    email = "carlos.porto@gmail.com"
    senha = "carlinhos"
    data_ingresso = 23/9/12

    comando = f'INSERT INTO administrador(login, email, senha, data_ingresso) VALUES ("{login}", "{email}","{senha}", {data_ingresso})'
    cursor.execute(comando)
    conexao.commit() #edita o banco de dados

#READ
#comando = f'SELECT * FROM administrador'
#cursor.execute(comando)
#resultado = cursor.fetchall() #ler o banco de dados
#print(resultado)

def buscar():   
    login = "Carlos777"
    comando = f'SELECT administrador.login FROM administrador'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)

def atualizar():
    login = "josé"
    novo_login = "Braga"
    comando = f'UPDATE administrador SET login = "{novo_login}" WHERE login = "{login}"'
    cursor.execute(comando)
    conexao.commit()

def remover():
    pass


atualizar()


cursor.close()

conexao.close()