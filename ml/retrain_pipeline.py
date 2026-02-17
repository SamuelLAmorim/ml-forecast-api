import pandas as pd
import sqlite3
import subprocess

def exportar_dados_app():
    conn = sqlite3.connect("gastos.db")
    df = pd.read_sql_query("SELECT * FROM gastos", conn)

    df.to_csv("data/gastos_app.csv", index=False)
    conn.close()

    print("Dados do app exportados.")


def rodar_pipeline():
    subprocess.run(["python", "ml/preprocess.py"])
    subprocess.run(["python", "ml/train.py"])
    print("Modelo atualizado com novos dados.")


if __name__ == "__main__":
    exportar_dados_app()
    rodar_pipeline()