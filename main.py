import sqlite3

conexao=sqlite3.connect("banco.db")
cursor=conexao.cursor()

cursor.execute("""CREATE TABLE contas_bancarias(
                id 
                )""")