from fastapi import APIRouter, Query
from sqlalchemy import create_engine, MetaData, select
from fastapi.responses import JSONResponse

router = APIRouter()

DATABASE_URL = "sqlite:///vitivinicultura.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata = MetaData()
metadata.reflect(bind=engine)

# Tabelas
exp_espumante = metadata.tables.get("EXP_ESPUMANTE")
exp_suco = metadata.tables.get("EXP_SUCO")
exp_uva = metadata.tables.get("EXP_UVA")
exp_vinho = metadata.tables.get("EXP_VINHO")

@router.get("/exportacao/espumante")
def listar_exp_espumante(ano: int = Query(None), limit: int = Query(50), offset: int = Query(0)):
    with engine.connect() as conn:
        query = select(exp_espumante).limit(limit).offset(offset)
        if ano is not None:
            query = query.where(exp_espumante.c.ano == ano)
        result = conn.execute(query)
        dados = [dict(row._mapping) for row in result]
    return JSONResponse(content=dados)

@router.get("/exportacao/suco")
def listar_exp_suco(ano: int = Query(None), limit: int = Query(50), offset: int = Query(0)):
    with engine.connect() as conn:
        query = select(exp_suco).limit(limit).offset(offset)
        if ano is not None:
            query = query.where(exp_suco.c.ano == ano)
        result = conn.execute(query)
        dados = [dict(row._mapping) for row in result]
    return JSONResponse(content=dados)

@router.get("/exportacao/uva")
def listar_exp_uva(ano: int = Query(None), limit: int = Query(50), offset: int = Query(0)):
    with engine.connect() as conn:
        query = select(exp_uva).limit(limit).offset(offset)
        if ano is not None:
            query = query.where(exp_uva.c.ano == ano)
        result = conn.execute(query)
        dados = [dict(row._mapping) for row in result]
    return JSONResponse(content=dados)

@router.get("/exportacao/vinho")
def listar_exp_vinho(ano: int = Query(None), limit: int = Query(50), offset: int = Query(0)):
    with engine.connect() as conn:
        query = select(exp_vinho).limit(limit).offset(offset)
        if ano is not None:
            query = query.where(exp_vinho.c.ano == ano)
        result = conn.execute(query)
        dados = [dict(row._mapping) for row in result]
    return JSONResponse(content=dados)
