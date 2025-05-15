from fastapi import APIRouter, Query, HTTPException
from sqlalchemy import create_engine, MetaData, Table, select, insert, update, delete
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError

router = APIRouter()

DATABASE_URL = "sqlite:///vitivinicultura.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata = MetaData()
metadata.reflect(bind=engine)

producao_table = metadata.tables.get("PRODUCAO")

# Método GET para listar os registros de PRODUCAO
@router.get("/producao")
def listar_producao(ano: int = Query(None), limit: int = Query(50), offset: int = Query(0)):
    with engine.connect() as conn:
        query = select(producao_table).limit(limit).offset(offset)
        if ano is not None:
            query = query.where(producao_table.c.ano == ano)
        result = conn.execute(query)
        registros = [dict(row._mapping) for row in result]
    return JSONResponse(content=registros)

# Método POST para inserir um novo registro de PRODUCAO
@router.post("/producao")
def inserir_producao(ano: int, quantidade: float, valor: float):
    with engine.connect() as conn:
        # Inserindo um novo registro na tabela PRODUCAO
        try:
            query = insert(producao_table).values(ano=ano, quantidade=quantidade, valor=valor)
            conn.execute(query)
            conn.commit()
            return JSONResponse(content={"message": "Registro inserido com sucesso"}, status_code=201)
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail="Erro de integridade: dados duplicados ou inválidos.")

# Método PUT para atualizar um registro de PRODUCAO
@router.put("/producao/{registro_id}")
def atualizar_producao(registro_id: int, ano: int = Query(None), quantidade: float = Query(None), valor: float = Query(None)):
    with engine.connect() as conn:
        # Verificando se o registro existe
        query = select(producao_table).where(producao_table.c.id == registro_id)
        result = conn.execute(query)
        registro = result.fetchone()
        
        if not registro:
            raise HTTPException(status_code=404, detail="Registro não encontrado")
        
        # Atualizando os valores do registro
        update_values = {}
        if ano is not None:
            update_values['ano'] = ano
        if quantidade is not None:
            update_values['quantidade'] = quantidade
        if valor is not None:
            update_values['valor'] = valor

        if update_values:
            query = update(producao_table).where(producao_table.c.id == registro_id).values(update_values)
            conn.execute(query)
            conn.commit()
            return JSONResponse(content={"message": "Registro atualizado com sucesso"})
        else:
            raise HTTPException(status_code=400, detail="Nenhum dado para atualizar")

# Método DELETE para excluir um registro de PRODUCAO
@router.delete("/producao/{registro_id}")
def excluir_producao(registro_id: int):
    with engine.connect() as conn:
        # Verificando se o registro existe
        query = select(producao_table).where(producao_table.c.id == registro_id)
        result = conn.execute(query)
        registro = result.fetchone()

        if not registro:
            raise HTTPException(status_code=404, detail="Registro não encontrado")
        
        # Excluindo o registro
        query = delete(producao_table).where(producao_table.c.id == registro_id)
        conn.execute(query)
        conn.commit()
        return JSONResponse(content={"message": "Registro excluído com sucesso"})
