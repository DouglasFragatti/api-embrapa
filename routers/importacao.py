from fastapi import APIRouter, Query
from sqlalchemy import create_engine, MetaData, select, and_
from fastapi.responses import JSONResponse

router = APIRouter()

DATABASE_URL = "sqlite:///vitivinicultura.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata = MetaData()
metadata.reflect(bind=engine)

# Pegando cada tabela de importação
imp_espumante = metadata.tables.get("IMP_ESPUMANTE")
imp_fresca = metadata.tables.get("IMP_FRESCA")
imp_passa = metadata.tables.get("IMP_PASSA")
imp_suco = metadata.tables.get("IMP_SUCO")
imp_vinho = metadata.tables.get("IMP_VINHO")

def listar_tabela(tabela, limit: int, offset: int, ano: int = None):
    with engine.connect() as conn:
        query = select(tabela).limit(limit).offset(offset)
        
        # Adicionando o filtro por ano, se fornecido
        if ano:
            query = query.where(tabela.c.ano == ano)
        
        result = conn.execute(query)
        dados = [dict(row._mapping) for row in result]
    return JSONResponse(content=dados)

@router.get("/importacao/espumante")
def listar_imp_espumante(limit: int = Query(50), offset: int = Query(0), ano: int = Query(None)):
    return listar_tabela(imp_espumante, limit, offset, ano)

@router.get("/importacao/fresca")
def listar_imp_fresca(limit: int = Query(50), offset: int = Query(0), ano: int = Query(None)):
    return listar_tabela(imp_fresca, limit, offset, ano)

@router.get("/importacao/passa")
def listar_imp_passa(limit: int = Query(50), offset: int = Query(0), ano: int = Query(None)):
    return listar_tabela(imp_passa, limit, offset, ano)

@router.get("/importacao/suco")
def listar_imp_suco(limit: int = Query(50), offset: int = Query(0), ano: int = Query(None)):
    return listar_tabela(imp_suco, limit, offset, ano)

@router.get("/importacao/vinho")
def listar_imp_vinho(limit: int = Query(50), offset: int = Query(0), ano: int = Query(None)):
    return listar_tabela(imp_vinho, limit, offset, ano)
