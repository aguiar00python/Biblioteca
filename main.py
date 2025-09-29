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

#ETAPA 3 -  listando livros
def listar_livros():
    cursor.execute("SELECT * FROM Biblioteca")
    livros = cursor.fetchall()
    if not livros:
        print("Não tem livros")
    else:
        print("Lista de livros:")
        for livro in livros:
            id, titulo, autor, ano, disponivel = livro
            print(f"ID: {id} | Título: {titulo} | Autor: {autor} | Ano: {ano} | Disponível: {disponivel}")

#ETAPA 3
def listar_livros():
    cursor.execute("SELECT * FROM Biblioteca")
    livros = cursor.fetchall()
    if not livros:
        print("Não tem livros")
    else:
        print("Lista de livros:")
        for livro in livros:
            id, titulo, autor, ano, disponivel = livro
            print(f"ID: {id} | Título: {titulo} | Autor: {autor} | Ano: {ano} | Disponível: {disponivel}")

#Etapa 4 - atualização da disponibilidade 

def alterar_disponibilidade(id_livro):
    cursor.execute("SELECT Disponivel FROM Biblioteca WHERE id = ?", (id_livro,))
    resultado = cursor.fetchone()

    disponivel_atual = resultado[0]
    novo_valor = "Não" if disponivel_atual == "Sim" else "Sim"

    cursor.execute("UPDATE Biblioteca SET Disponivel = ? WHERE id = ?", (novo_valor, id_livro))
    conexao.commit()
    print(f"Disponibilidade do livro ID {id_livro} alterada para '{novo_valor}'.")

# Etapa 5 - removendo livros
def remover_livro():
    try:
        id_livro = int(input("Digite o ID do livro que deseja remover: "))
        cursor.execute("DELETE FROM Biblioteca WHERE id = ?", (id_livro,))
        conexao.commit()

        if cursor.rowcount > 0: # Exibe quantas linhas foram deletadas
            print("Livro removido com sucesso!")
        else:
            print("Nenhum livro encontrado com o ID fornecido")
    except ValueError:
        print("Por favor, digite um número válido para o ID")
    except Exception as erro:
        print(f"Erro ao tentar excluir livro: {erro}")
