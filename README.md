# 🍇 API Vitivinicultura - Embrapa

API desenvolvida para consulta de dados da vitivinicultura brasileira com base nos arquivos CSV públicos da Embrapa. Permite acesso a dados de produção, comercialização, exportação e importação de uvas, vinhos e derivados.

---

## 🚀 Funcionalidades

- 🔍 Consulta de dados: produção, comercialização, exportação e importação
- 📊 Dados estruturados a partir de arquivos CSV
- 🗃️ Banco de dados SQLite local (com possibilidade futura de PostgreSQL)
- 🔐 Estrutura pronta para autenticação com JWT (em construção)

---

## 🧱 Estrutura do Projeto

```
├── main.py               # Inicialização da API
├── models.py             # Modelos do banco (SQLAlchemy)
├── database.py           # Conexão com o SQLite
├── create_tables.py      # Script de criação das tabelas
├── routers/              # Rotas separadas por área (produção, exportação, etc.)
├── data/csvs/            # Arquivos CSV originais da Embrapa
├── vitivinicultura.db    # Banco de dados SQLite
├── requirements.txt      # Dependências do projeto
└── README.md             # Esta documentação
```

---

## 🛠️ Como executar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/DouglasFragatti/api-embrapa.git
cd api-embrapa
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
# Ative:
# Windows:
venv\Scripts\activate

# Linux/macOS:
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Crie o banco de dados e as tabelas

```bash
python create_tables.py
```

### 5. Execute a API com Uvicorn

```bash
uvicorn main:app --reload
```

---

## 📫 Acesse a documentação

Acesse a interface interativa da API em:

🔗 [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📦 Deploy (em breve)

O projeto será publicado com link público gratuito via [Render.com](https://render.com) ou Railway.

---

## 💡 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

---

## 📄 Licença

Este projeto está sob a licença MIT.
