from fastapi import APIRouter, Query
from sqlalchemy import create_engine, MetaData, select
from fastapi.responses import JSONResponse

router = APIRouter()

DATABASE_URL = "sqlite:///vitivinicultura.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata = MetaData()
metadata.reflect(bind=engine)

# Pegando cada tabela de uva processada
proc_americana = metadata.tables.get("PROCESSADA_AMERICANA")
proc_mesa = metadata.tables.get("PROCESSADA_MESA")
proc_sem_classificacao = metadata.tables.get("PROCESSADA_SEM_CLASSIFICACAO")
proc_viniferas = metadata.tables.get("PROCESSADA_VINIFERAS")

def listar_tabela(tabela, limit: int, offset: int, ano: int = None):
    with engine.connect() as conn:
        query = select(tabela).limit(limit).offset(offset)
        
        # Adicionando o filtro por ano, se fornecido
        if ano:
            query = query.where(tabela.c.ano == ano)
        
        result = conn.execute(query)
        dados = [dict(row._mapping) for row in result]
    return JSONResponse(content=dados)

@router.get("/processada/americana")
def listar_proc_americana(limit: int = Query(50), offset: int = Query(0), ano: int = Query(None)):
    return listar_tabela(proc_americana, limit, offset, ano)

@router.get("/processada/mesa")
def listar_proc_mesa(limit: int = Query(50), offset: int = Query(0), ano: int = Query(None)):
    return listar_tabela(proc_mesa, limit, offset, ano)

@router.get("/processada/sem_classificacao")
def listar_proc_sem_classificacao(limit: int = Query(50), offset: int = Query(0), ano: int = Query(None)):
    return listar_tabela(proc_sem_classificacao, limit, offset, ano)

@router.get("/processada/viniferas")
def listar_proc_viniferas(limit: int = Query(50), offset: int = Query(0), ano: int = Query(None)):
    return listar_tabela(proc_viniferas, limit, offset, ano)
