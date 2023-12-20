import datetime
import sqlite3


# Criação do banco de dados
conn = sqlite3.connect('banco.db')
cursor = conn.cursor()
conn.execute('''CREATE TABLE IF NOT EXISTS dados
                (produto TEXT, horario TIMESTAMP, precos REAL)''')

def save_to_DB(nome, preço_atual):
    conn = sqlite3.connect('banco.db')
    horario = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    conn.execute('INSERT INTO dados VALUES (?, ?, ?)',
                 (str(nome), horario, preço_atual))
    conn.commit()
    conn.close()

def obter_dados():
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    cursor.execute('SELECT produto, horario, precos FROM dados')
    dados = cursor.fetchall()
    conn.close()
    return dados