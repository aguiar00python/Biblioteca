import sqlite3
conexao = sqlite3.connect("biblioteca.db")

cursor = conexao.cursor()

#ETAPA 1 - criando uma tabela

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

#ETAPA 2 - cadastrando livros

def cadastrar_livros():
    conexao = sqlite3.connect("biblioteca.db")
    cursor = conexao.cursor()
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o nome do autor do livro: ")
    ano = input("Digite o ano do livro: ")
    disponivel = "sim"
    
    cursor.execute("""
        INSERT INTO livros (titulo, autor, ano, disponivel)
        VALUES (?, ?, ?, ?)
    """, (titulo, autor, ano, disponivel))
    
    conexao.commit()
    conexao.close()

cadastrar_livros()
print("Livro cadastrado com sucesso!")

