import sqlite3
conexao = sqlite3.connect("biblioteca.db")

cursor = conexao.cursor()

#ETAPA 1

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    autor TEXT ,
    ano INTEGER, 
    disponivel TEXT NOT NULL              
    )                
""")
print("Tabela criada com sucesso!")

