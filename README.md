# API Vitivinicultura - FIAP

API desenvolvida com **FastAPI** para fornecer dados vitivinícolas públicos extraídos do portal da **Embrapa (Vitibrasil)**.

## - Funcionalidades

- Consulta de dados: produção, comercialização, exportação e importação
- Dados estruturados a partir de arquivos CSV
- Banco de dados SQLite local (com possibilidade de migração para PostgreSQL)
- Pronta para rotas autenticadas com JWT (em construção)

## Estrutura do Projeto
├── main.py # Inicialização da API
├── models.py # Modelos do banco (SQLAlchemy)
├── database.py # Conexão com o SQLite
├── create_tables.py # Script de criação das tabelas
├── routers/ # Rotas separadas por área
├── data/csvs/ # Arquivos CSV da Embrapa
├── vitivinicultura.db # Banco de dados SQLite
├── requirements.txt
└── README.md # Documentação

1. **Clone o repositório**

```bash
git clone https://github.com/DouglasFragatti/api-embrapa.git
cd API_Fiap


2. **Crie um ambiente virtual e ative-o
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows


3. Instale as dependências
pip install -r requirements.txt


4. Crie o banco e as tabelas
python cria_banco.py


5. Execute a API
uvicorn main:app --reload


Acesse: http://localhost:8000/docs