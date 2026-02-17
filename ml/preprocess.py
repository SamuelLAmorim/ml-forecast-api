import pandas as pd

# caminho do dataset
DATA_PATH = "data/Personal_Finance_Dataset.csv"

# carregar
df = pd.read_csv(DATA_PATH)

print("Colunas encontradas:")
print(df.columns)

# converter data
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# remover linhas com data inválida
df = df.dropna(subset=['Date'])

# filtrar apenas despesas
df_expense = df[df['Type'] == 'Expense'].copy()

# criar features temporais
df_expense['ano'] = df_expense['Date'].dt.year
df_expense['mes'] = df_expense['Date'].dt.month

# garantir que Amount é numérico
df_expense['Amount'] = pd.to_numeric(df_expense['Amount'], errors='coerce')

# remover valores inválidos
df_expense = df_expense.dropna(subset=['Amount'])

# agregação mensal
df_model = df_expense.groupby(['ano', 'mes'])['Amount'].sum().reset_index()

# renomear coluna alvo
df_model.rename(columns={'Amount': 'valor'}, inplace=True)

print("\nDataset após preprocess:")
print(df_model.head())

# salvar dataset final para ML
df_model.to_csv("data/gastos_mensais_model.csv", index=False)

df_kaggle = pd.read_csv("data/Personal_Finance_Dataset.csv")
df_app = pd.read_csv("data/gastos_app.csv")

df_total = pd.concat([df_kaggle, df_app])

print("\nArquivo salvo em data/gastos_mensais_model.csv")