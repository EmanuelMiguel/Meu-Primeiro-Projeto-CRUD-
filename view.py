# Importando SQLite
import sqlite3 as lite

# CRUD

# CREATE = Inserir/CRIAR
# READY = ACESSAR/MOSTRAR
# UDATE = Autualizar
# DELETE = DELETAR/APAGAR


# Criando Conexão
con = lite.connect('dados.db')


# Inserir informações (BOTÃO INSERIR)
def inserir_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO formulario (nome, cpf, email, telefone, observacoes, dia_em) VALUES (?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)


# Acessar informações (READY)
def mostrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM formulario"
        cur.execute(query)
        informação = cur.fetchall()

        for i in informação:
            lista.append(i)
    return lista


# Autualizar informações (BOTÃO ATUALIZAR)
def atualizar_info(i):
    with con:
        cur = con.cursor()
        query = "UPDATE formulario SET nome=?, cpf=?, email=?, telefone=?, observacoes=?, dia_em=? WHERE id=?"
        cur.execute(query, i)


# Deletar informações (BOTÃO DELETAR)
def deletar_info(valores_ids):
    with con:
        cur = con.cursor()

        # Criar uma string de placeholders para a consulta
        placeholders = ', '.join('?' for _ in valores_ids)

        query = f"DELETE FROM formulario WHERE id IN ({placeholders})"

        print(f"Consulta SQL: {query}")  # Para depuração
        print(f"Valores a serem deletados: {valores_ids}")  # Para depuração

        cur.execute(query, valores_ids)


# Centralizando Janela
