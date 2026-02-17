import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# carregar dataset preprocessado
df = pd.read_csv("data/gastos_mensais_model.csv")

print("Dataset de treino:")
print(df.head())

# features e target
X = df[['ano', 'mes']]
y = df['valor']

# modelo
model = LinearRegression()
model.fit(X, y)

print("\nModelo treinado com sucesso.")

# salvar modelo
joblib.dump(model, "models/model_gastos.pkl")

print("Modelo salvo em models/model_gastos.pkl")