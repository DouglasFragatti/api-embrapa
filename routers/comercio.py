from fastapi import APIRouter, Query, HTTPException
from sqlalchemy import create_engine, MetaData, Table, select, insert, update, delete
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError

router = APIRouter()

DATABASE_URL = "sqlite:///vitivinicultura.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata = MetaData()
metadata.reflect(bind=engine)

comercio_table = metadata.tables.get("COMERCIO")

# Método GET para listar os registros de COMERCIO
@router.get("/comercio")
def listar_comercio(ano: int = Query(None), limit: int = Query(50), offset: int = Query(0)):
    with engine.connect() as conn:
        query = select(comercio_table).limit(limit).offset(offset)
        if ano is not None:
            query = query.where(comercio_table.c.ano == ano)
        result = conn.execute(query)
        registros = [dict(row._mapping) for row in result]
    return JSONResponse(content=registros)

# Método POST para inserir um novo registro de COMERCIO
@router.post("/comercio")
def inserir_comercio(ano: int, valor: float, quantidade: float):
    with engine.connect() as conn:
        # Inserindo um novo registro na tabela COMERCIO
        try:
            query = insert(comercio_table).values(ano=ano, valor=valor, quantidade=quantidade)
            conn.execute(query)
            conn.commit()
            return JSONResponse(content={"message": "Registro inserido com sucesso"}, status_code=201)
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail="Erro de integridade: dados duplicados ou inválidos.")

# Método PUT para atualizar um registro de COMERCIO
@router.put("/comercio/{registro_id}")
def atualizar_comercio(registro_id: int, ano: int = Query(None), valor: float = Query(None), quantidade: float = Query(None)):
    with engine.connect() as conn:
        # Verificando se o registro existe
        query = select(comercio_table).where(comercio_table.c.id == registro_id)
        result = conn.execute(query)
        registro = result.fetchone()
        
        if not registro:
            raise HTTPException(status_code=404, detail="Registro não encontrado")
        
        # Atualizando os valores do registro
        update_values = {}
        if ano is not None:
            update_values['ano'] = ano
        if valor is not None:
            update_values['valor'] = valor
        if quantidade is not None:
            update_values['quantidade'] = quantidade

        if update_values:
            query = update(comercio_table).where(comercio_table.c.id == registro_id).values(update_values)
            conn.execute(query)
            conn.commit()
            return JSONResponse(content={"message": "Registro atualizado com sucesso"})
        else:
            raise HTTPException(status_code=400, detail="Nenhum dado para atualizar")

# Método DELETE para excluir um registro de COMERCIO
@router.delete("/comercio/{registro_id}")
def excluir_comercio(registro_id: int):
    with engine.connect() as conn:
        # Verificando se o registro existe
        query = select(comercio_table).where(comercio_table.c.id == registro_id)
        result = conn.execute(query)
        registro = result.fetchone()

        if not registro:
            raise HTTPException(status_code=404, detail="Registro não encontrado")
        
        # Excluindo o registro
        query = delete(comercio_table).where(comercio_table.c.id == registro_id)
        conn.execute(query)
        conn.commit()
        return JSONResponse(content={"message": "Registro excluído com sucesso"})
