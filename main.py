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

cursor.execute("""SELECT nome,saldo FROM contas_bancarias
WHERE saldo>10""")
contas=cursor.fetchall()
for conta in contas:
    nome,saldo=conta
    print(f"""Nome: {nome}
Saldo: R${saldo}
""")
    print("\n")
conexao.commit()



