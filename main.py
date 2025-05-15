from fastapi import FastAPI
from routers.producao import router as producao_router
from routers.comercio import router as comercio_router
from routers.exportacao import router as exportacao_router
from routers.importacao import router as importacao_router
from routers.processada import router as processada_router

app = FastAPI()

app.include_router(producao_router)
app.include_router(comercio_router)
app.include_router(exportacao_router)
app.include_router(importacao_router)
app.include_router(processada_router)

@app.get("/")
def root():
    return {"mensagem": "API Vitivinícola no ar"}
