import joblib
import pandas as pd

# carregar modelo treinado
model = joblib.load("models/model_gastos.pkl")

def prever_gasto(ano, mes):
    entrada = pd.DataFrame([[ano, mes]], columns=["ano", "mes"])
    previsao = model.predict(entrada)
    return float(previsao[0])

# execução direta via terminal
if __name__ == "__main__":
    ano = int(input("Digite o ano: "))
    mes = int(input("Digite o mês (1-12): "))

    resultado = prever_gasto(ano, mes)
    print(f"\nPrevisão de gasto para {mes}/{ano}: R$ {resultado:,.2f}")