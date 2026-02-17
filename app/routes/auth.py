from fastapi import APIRouter, Form, Depends, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User

router = APIRouter()

# dependency de db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# registro
@router.post("/register")
def register(nome: str = Form(...), email: str = Form(...), senha: str = Form(...), db: Session = Depends(get_db)):
    user = User(nome=nome, email=email, senha_hash=senha)
    db.add(user)
    db.commit()
    return {"msg": "Usuário criado"}


# login
@router.post("/login")
def login(
    request: Request,
    email: str = Form(...),
    senha: str = Form(...),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        User.email == email,
        User.senha_hash == senha
    ).first()

    if not user:
        return {"erro": "Credenciais inválidas"}

    request.session["user_id"] = user.id

    return {"msg": "Login realizado com sucesso"}