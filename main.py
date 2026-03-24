import time
import pandas as pd
from pathlib import Path
from tqdm import tqdm

from etl import carregar_microdados_antigos
from etl import carregar_microdados_vigente
from etl import detectar_anos_formato_vigente

from schema import SCHEMA_CURICA

# inicializacao contador de tempo
inicio_execucao = time.time()

# toma como diretório pai o diretório do arquivo do notebook
BASE_DIR = Path(__file__).resolve().parent
RAW_CENSO_DIR = BASE_DIR / "data" / "raw"

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

# salvamento do arquivo
output_dir = BASE_DIR / "processed"
output_dir.mkdir(exist_ok=True)

df_censo.to_csv(output_dir / "df_censo.csv", sep=";", encoding="latin-1", index=False)
print(f"\nDataframe salvo em {output_dir}")

fim_execucao = time.time()
tempo_execucao = fim_execucao - inicio_execucao
print(f"\nTempo total de execução: {tempo_execucao:.2f} segundos")
print("\nProcesso concluído com sucesso.")

