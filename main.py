import sqlite3
conexao=sqlite3.connect("banco.db")
cursor=conexao.cursor()
cursor.execute("""
                CREATE TABLE IF NOT EXISTS contas_bancarias(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXTE NOT NULL,  
                saldo FLOAT NOT NULL,
                cpf TEXT NOT NULL UNIQUE
                )""")

# cursor.execute("""
#                 INSERT INTO contas_bancarias
#                 (nome,saldo,cpf) VALUES
#                 ('Pedro',-2000,'1234567810')
#                 """)

cursor.execute("""""")

conexao.commit()
