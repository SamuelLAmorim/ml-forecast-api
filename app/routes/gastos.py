from fastapi import APIRouter, Depends, Request, Form
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Gasto
from datetime import datetime

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(request: Request):
    user_id = request.session.get("user_id")
    if not user_id:
        return None
    return user_id


@router.post("/novo")
def criar_gasto(
    request: Request,
    data: str = Form(...),
    categoria: str = Form(...),
    valor: float = Form(...),
    tipo_pagamento: str = Form(...),
    db: Session = Depends(get_db)
):
    user_id = get_current_user(request)

    if not user_id:
        return {"erro": "Usuário não autenticado"}

    try:
        data_convertida = datetime.strptime(data, "%Y-%m-%d").date()
    except ValueError:
        return {"erro": "Data deve estar no formato ISO: YYYY-MM-DD"}

    gasto = Gasto(
        data=data_convertida,
        categoria=categoria,
        valor=valor,
        tipo_pagamento=tipo_pagamento,
        user_id=user_id
    )

    db.add(gasto)
    db.commit()

    return {"msg": "Gasto registrado com sucesso"}