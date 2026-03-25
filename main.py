import time
import pandas as pd
from pathlib import Path
from tqdm import tqdm

from etl import carregar_microdados_antigos
from etl import carregar_microdados_vigente
from etl import detectar_anos_formato_vigente
from etl import gerar_panorama

from schema import SCHEMA_CURICA
from schema import SCHEMAS_PANORAMAS

# inicializacao contador de tempo
inicio_execucao = time.time()

# diretórios de saída
BASE_DIR = Path(__file__).resolve().parent
RAW_CENSO_DIR = BASE_DIR / "data" / "raw"
OUTPUT_INTERIM_DIR = BASE_DIR / "data" / "interim"
OUTPUT_PROCESSED_DIR = BASE_DIR / "data" / "processed"

def executar_etl(raw_dir):

    arquivos = sorted(raw_dir.glob("microdados_ed_basica_*.csv"))

    dfs = []

    # ----------------------
    # ANOS ANTIGOS
    # ----------------------
    tqdm.write("\nProcessando arquivos no formato antigo:")

    for arq in tqdm(arquivos, desc="Formato antigo"):
        tqdm.write(f"Processando {arq.name}")

        df = carregar_microdados_antigos(arq, SCHEMA_CURICA)
        dfs.append(df)

    # ----------------------
    # 2025+
    # ----------------------
    tqdm.write("\nProcessando microdados no formato vigente:")

    anos = sorted(detectar_anos_formato_vigente(raw_dir))

    for ano in tqdm(anos, desc="Formato vigente"):
        tqdm.write(f"Processando microdados do ano {ano}")
        
        df = carregar_microdados_vigente(raw_dir, ano, SCHEMA_CURICA)
        dfs.append(df)

    # ----------------------
    # CONCAT FINAL
    # ----------------------
    df_final = pd.concat(dfs, ignore_index=True)

    del dfs

    return df_final


# EXECUÇÃO
df_censo = executar_etl(RAW_CENSO_DIR)

# salvamento do arquivo CSV
df_censo.to_csv(OUTPUT_INTERIM_DIR / "df_censo.csv", sep=";", encoding="latin-1", index=False)
print(f"\nDataframe intermediário salvo em {OUTPUT_INTERIM_DIR}")

# Criação dos dataframes dos panoramas
dfs_panoramas = {}

for nome, colunas in SCHEMAS_PANORAMAS.items():
    dfs_panoramas[nome] = gerar_panorama(df_censo, colunas)

# liberação de memória
del df_censo

for nome, df in dfs_panoramas.items():

    caminho = OUTPUT_PROCESSED_DIR / f"df_{nome}.csv"

    df.to_csv(caminho, sep=";", encoding="latin-1", index=False)

    print(f"\n{nome} salvo em {caminho}")

del dfs_panoramas

fim_execucao = time.time()
tempo_execucao = fim_execucao - inicio_execucao
print(f"\nTempo total de execução: {tempo_execucao:.2f} segundos")
print("\nProcesso concluído com sucesso.")

