import os
import pandas as pd
import sqlite3

# Caminhos
folder_path = "data/csvs"
db_path = "vitivinicultura.db"

# Conecta ao SQLite
conn = sqlite3.connect(db_path)

def importar_e_transformar_csv(nome_arquivo_csv, nome_tabela, colunas_fixas):
    caminho_arquivo = os.path.join(folder_path, nome_arquivo_csv)

    print(f"Importando {nome_arquivo_csv}...")

    df = pd.read_csv(caminho_arquivo, sep=';', encoding='latin1')

    #print("Colunas do DataFrame:", df.columns.tolist())
    #print(df.head())  # Para conferir as primeiras linhas


    # Colunas que são anos (ex: "1970", "1980", etc)
    colunas_ano = [col for col in df.columns if col.isdigit()]

    # Transforma os dados para formato relacional
    df_melted = df.melt(id_vars=colunas_fixas, value_vars=colunas_ano,
                        var_name="ano", value_name="quantidade")

    df_melted["ano"] = df_melted["ano"].astype(int)

    # Salva no banco
    df_melted.to_sql(nome_tabela, conn, if_exists="replace", index=False)

    print(f"{nome_tabela} importada com sucesso!")

# Lista de arquivos e suas configurações
arquivos_para_importar = [
    ("COMERCIO.csv", "COMERCIO", ["id", "control", "produto"]),
    ("PRODUCAO.csv", "PRODUCAO", ["id", "control", "produto"]),
    ("EXP_ESPUMANTE.csv", "EXP_ESPUMANTE", ["id", "pais"]),
    ("EXP_SUCO.csv", "EXP_SUCO", ["id", "pais"]),
    ("EXP_UVA.csv", "EXP_UVA", ["id", "pais"]),
    ("EXP_VINHO.csv", "EXP_VINHO", ["id", "pais"]),
    ("IMP_ESPUMANTE.csv", "IMP_ESPUMANTE", ["id", "pais"]),
    ("IMP_FRESCA.csv", "IMP_FRESCA", ["id", "pais"]),
    ("IMP_PASSA.csv", "IMP_PASSA", ["id", "pais"]),
    ("IMP_SUCO.csv", "IMP_SUCO", ["id", "pais"]),
    ("IMP_VINHO.csv", "IMP_VINHO", ["id", "pais"]),
    ("PROCESSADA_AMERICANA.csv", "PROCESSADA_AMERICANA", ["id", "control", "cultivar"]),
    ("PROCESSADA_MESA.csv", "PROCESSADA_MESA", ["id", "control", "cultivar"]),
    ("PROCESSADA_SEM_CLASSIFICACAO.csv", "PROCESSADA_SEM_CLASSIFICACAO", ["id", "control", "cultivar"]),
    ("PROCESSADA_VINIFERAS.csv", "PROCESSADA_VINIFERAS", ["id", "control", "cultivar"])
]

# Executa para todos
for arquivo_csv, nome_tabela, colunas_fixas in arquivos_para_importar:
    importar_e_transformar_csv(arquivo_csv, nome_tabela, colunas_fixas)

conn.close()

print("Importação de todos os arquivos concluída.")
