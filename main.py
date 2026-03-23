from pathlib import Path
import pandas as pd

from etl import carregar_microdados_antigos
from etl import carregar_microdados_vigente
from etl import detectar_anos_formato_vigente

from schema import SCHEMA_CURICA

# toma como diretório pai o diretório do arquivo do notebook
BASE_DIR = Path(__file__).resolve().parent
RAW_CENSO_DIR = BASE_DIR / "data" / "raw"

schema_colunas = SCHEMA_CURICA



def executar_etl(raw_dir):

    arquivos = sorted(raw_dir.glob("microdados_ed_basica_*.csv"))

    dfs = []

    # ----------------------
    # ANOS ANTIGOS
    # ----------------------
    for arq in arquivos:
        print(f"Processando {arq.name}")

        df = carregar_microdados_antigos(arq, schema_colunas)
        dfs.append(df)

    # ----------------------
    # 2025+
    # ----------------------
    print("\nProcessando microdados no formato vigente")

    anos = detectar_anos_formato_vigente(raw_dir)

    for ano in anos:
        df = carregar_microdados_vigente(raw_dir, ano, schema_colunas)
        dfs.append(df)

    # ----------------------
    # CONCAT FINAL
    # ----------------------
    df_final = pd.concat(dfs, ignore_index=True)

    return df_final


# EXECUÇÃO
df_censo = executar_etl(RAW_CENSO_DIR)

# salvamento do arquivo
output_dir = BASE_DIR / "processed"
output_dir.mkdir(exist_ok=True)

df_censo.to_csv(output_dir / "df_censo.csv", sep=";", encoding="latin-1", index=False)

