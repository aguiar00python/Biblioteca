📚 Sistema de Biblioteca em Python

Este é um programa simples em Python que permite gerenciar livros usando um banco de dados SQLite.

✅ Funcionalidades

Criar banco de dados e tabela automaticamente

Cadastrar novos livros

Listar todos os livros cadastrados

Atualizar se o livro está disponível ou não

Remover livros do sistema

Menu interativo no terminal

▶️ Como usar

Salve o código em um arquivo, por exemplo: biblioteca.py

Execute o arquivo com Python:

python biblioteca.py


Siga o menu no terminal para usar o sistema.

💻 Requisitos

Python 3 instalado

⚠️ Observações

Os dados são salvos no arquivo biblioteca.db

Os livros cadastrados têm os campos: ID, Título, Autor, Ano e Disponibilidade

📁 Estrutura da Tabela (SQLite)
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    autor TEXT,
    ano INTEGER,
    disponivel TEXT NOT NULL
)
