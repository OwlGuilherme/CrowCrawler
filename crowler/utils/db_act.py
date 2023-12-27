import sqlite3
import datetime

def criar_tabela():
    with sqlite3.connect('banco.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS dados
                        (produto TEXT, horario TIMESTAMP, precos REAL, site TEXT)''')

def salvar_dados(nome, preco_atual, site):
    # Remover "R$" e substituir vírgulas por pontos
    if 'R$' in preco_atual:
        # Remover "R$" e substituir vírgulas por pontos
        preco_atual = float(preco_atual.replace('R$', '').replace(',', '.'))
    else:
        # Se não contiver "R$", apenas substituir vírgulas por pontos
        preco_atual = float(preco_atual.replace(',', '.'))

    # Obter o horário atual
    horario = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

    with sqlite3.connect('banco.db') as conn:
        try:
            conn.execute('INSERT INTO dados VALUES (?, ?, ?, ?)', (nome, horario, preco_atual, site))
            conn.commit()
            print(f"Dados inseridos com sucesso: {nome}, {horario}, {preco_atual}, {site}")

        except Exception as e:
            print(f"Erro ao inserir dados: {e}")


def obter_dados():
    with sqlite3.connect('banco.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT produto, horario, precos FROM dados')
        dados = cursor.fetchall()

    return dados

