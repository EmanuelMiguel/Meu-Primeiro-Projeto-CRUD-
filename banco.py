# Importando SQLite
import sqlite3 as lite

# Criando Conexão
con = lite.connect('dados.db')

# Criando Tabela
with con:
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS formulario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, cpf TEXT, email TEXT, telefone TEXT, observacoes TEXT, dia_em DATE)")

    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cur.fetchall())


def cpf_existe(cpf):
    try:
        con = lite.connect('dados.db')
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM formulario WHERE cpf=?", (cpf,))
            result = cur.fetchone()
    except lite.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")
        return False  # Retorna False se houver um erro
    finally:
        if con:
            con.close()
    return result is not None
