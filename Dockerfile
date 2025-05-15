# Usando imagem oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia todos os arquivos do projeto para dentro do container
COPY . /app

# Atualiza o pip e instala as dependências
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Expõe a porta da aplicação FastAPI
EXPOSE 8000

# Comando para iniciar o servidor com Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
