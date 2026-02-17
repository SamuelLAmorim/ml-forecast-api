from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from app.database import Base, engine
from app.routes import gastos, previsao, mlops, dashboard, auth


# cria app
app = FastAPI(
    title="ML Forecast API",
    description="API para previsão e gestão de gastos",
    version="1.0.0"
)

# cria tabelas no banco
Base.metadata.create_all(bind=engine)

# middleware de sessão (login)
app.add_middleware(
    SessionMiddleware,
    secret_key="super-secret-key"
)

# permitir comunicação com frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # depois restringe para domínio do frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# rotas da aplicação
app.include_router(auth.router, tags=["Auth"])
app.include_router(gastos.router, prefix="/gastos", tags=["Gastos"])
app.include_router(previsao.router, prefix="/previsao", tags=["Previsão"])
app.include_router(mlops.router, prefix="/mlops", tags=["MLOps"])
app.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])


@app.get("/")
def root():
    return {"status": "API running"}