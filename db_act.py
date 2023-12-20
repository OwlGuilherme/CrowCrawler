import sqlite3
import datetime

def criar_tabela():
    with sqlite3.connect('banco.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS dados
                        (produto TEXT, horario TIMESTAMP, precos REAL)''')

def salvar_dados(nome, preco_atual):
    horario = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    
    with sqlite3.connect('banco.db') as conn:
        conn.execute('INSERT INTO dados VALUES (?, ?, ?)',
                     (nome, horario, preco_atual))
        conn.commit()

def obter_dados():
    with sqlite3.connect('banco.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT produto, horario, precos FROM dados')
        dados = cursor.fetchall()

    return dados

