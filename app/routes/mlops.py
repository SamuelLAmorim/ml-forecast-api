from fastapi import APIRouter
import subprocess

router = APIRouter()

@router.post("/retrain-model")
def retrain_model():
    try:
        subprocess.run(["python", "ml/retrain_pipeline.py"], check=True)

        return {
            "status": "ok",
            "mensagem": "Modelo re-treinado com dados mais recentes."
        }

    except Exception as e:
        return {
            "status": "erro",
            "mensagem": str(e)
        }