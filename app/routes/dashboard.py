from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database import SessionLocal
from app.models import Gasto

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(request: Request):
    return request.session.get("user_id")


@router.get("/me")
def dashboard_usuario(request: Request, db: Session = Depends(get_db)):

    user_id = get_current_user(request)

    if not user_id:
        return {"erro": "Usuário não autenticado"}


    # TOTAL GASTO
    total = (
        db.query(func.sum(Gasto.valor))
        .filter(Gasto.user_id == user_id)
        .scalar()
    ) or 0

    # GASTO POR CATEGORIA
    categorias = (
        db.query(Gasto.categoria, func.sum(Gasto.valor))
        .filter(Gasto.user_id == user_id)
        .group_by(Gasto.categoria)
        .all()
    )

    categorias_dict = [
        {"categoria": cat, "total": float(valor or 0)}
        for cat, valor in categorias
    ]

    # GASTO POR MÊS (ISO YYYY-MM)
    mensal = (
        db.query(
            func.strftime("%Y-%m", Gasto.data).label("mes"),
            func.sum(Gasto.valor)
        )
        .filter(Gasto.user_id == user_id)
        .group_by("mes")
        .order_by("mes")  
        .all()
    )

    mensal_dict = [
        {"mes": mes, "total": float(valor or 0)}
        for mes, valor in mensal
    ]

    return {
        "total_gasto": float(total),
        "gastos_por_categoria": categorias_dict,
        "gastos_mensais": mensal_dict
    }