from fastapi import APIRouter
import joblib
import pandas as pd

router = APIRouter()

model = joblib.load("models/model_gastos.pkl")

@router.get("/previsao")
def prever_gasto(ano: int, mes: int):
    entrada = pd.DataFrame([[ano, mes]], columns=["ano", "mes"])
    previsao = model.predict(entrada)[0]

    return {
        "ano": ano,
        "mes": mes,
        "previsao_gasto": round(float(previsao), 2)
    }