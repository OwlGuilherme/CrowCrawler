import sqlite3

import matplotlib.pyplot as plt
import pandas as pd


def plotar_historico_precos(produto, site):
    with sqlite3.connect("banco.db") as conn:
        query = f"SELECT horario, precos FROM dados WHERE produto=? AND site=?"
        df = pd.read_sql_query(query, conn, params=(produto, site))

        if not df.empty:
            df["horario"] = pd.to_datetime(df["horario"])
            df.set_index("horario", inplace=True)

            plt.figure(figsize=(10, 6))
            plt.plot(df.index, df["precos"], marker="o", linestyle="-", color="b")
            plt.title(f"Histórico de preços para o produto{produto} - {site}")
            plt.xlabel("Dia e horário")
            plt.ylabel("Preço")
            plt.grid(True)
            plt.show()

        else:
            print("Não foram encontrados dados para o produto no site")
