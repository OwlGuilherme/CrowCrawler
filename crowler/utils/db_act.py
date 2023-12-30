import sqlite3
import datetime
import pandas as pd

def criar_tabela():
    with sqlite3.connect('banco.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS dados
                        (produto TEXT, horario TIMESTAMP, precos REAL, site TEXT)''')
        conn.execute('''CREATE TABLE IF NOT EXISTS ultimo_preco
                        (produto TEXT, preco REAL, site TEXT, PRIMARY KEY (produto, site))''')

def salvar_dados(nome, preco_atual, site):
    preco_atual = preprocessar_preco(preco_atual)

    horario = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

    with sqlite3.connect('banco.db') as conn:
        try:
            conn.execute('INSERT INTO dados VALUES (?, ?, ?, ?)', (nome, horario, preco_atual, site))
            conn.commit()
            print(f"Dados inseridos com sucesso: {nome}, {horario}, {preco_atual}, {site}")

            # Atualizar o último preço registrado
            conn.execute('INSERT OR REPLACE INTO ultimo_preco VALUES (?, ?, ?)', (nome, preco_atual, site))
            conn.commit()

        except Exception as e:
            print(f"Erro ao inserir dados: {e}")

def preprocessar_preco(preco):
    if isinstance(preco, str) and 'R$' in preco:
        # Remover "R$" e substituir vírgulas por pontos
        preco = preco.replace('R$', '').replace('.', '').replace(',', '.')

        # Remover espaços em branco antes e depois da string
        preco = preco.strip()

    return preco


def obter_ultimo_preco(nome, site):
    with sqlite3.connect('banco.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT preco FROM ultimo_preco WHERE produto=? AND site=?', (nome, site))
        ultimo_preco = cursor.fetchone()

    return ultimo_preco[0] if ultimo_preco else None

def obter_dados():
    with sqlite3.connect('banco.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT produto, horario, precos, site FROM dados')
        dados = cursor.fetchall()

    return dados


def carrega_dados(site):
    with sqlite3.connect('banco.db') as conn:
        query = f"SELECT produto, horario, precos FROM dados WHERE site='{site}'"

        df = pd.read_sql_query(query, conn)

        df['produto'] = df['produto'].str.lstrip()

        print(df)


def obter_produtos(site):
    with sqlite3.connect('banco.db') as conn:
        query = f"SELECT DISTINCT produto FROM dados WHERE site='{site}'"
        df = pd.read_sql_query(query, conn)

    return df['produto'].tolist()