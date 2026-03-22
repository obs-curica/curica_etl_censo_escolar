from pathlib import Path
import pandas as pd
import gc

from etl import carregar_microdados_antigos
from etl import carregar_microdados_vigente
from etl import detectar_anos_formato_vigente

from schema import SCHEMA_CURICA

# toma como diretório pai o diretório do arquivo do notebook
BASE_DIR = Path("main.py").resolve().parent
RAW_CENSO_DIR = BASE_DIR / "data" / "raw"


def executar_etl(raw_dir):

    arquivos = sorted(raw_dir.glob("microdados_ed_basica_*.csv"))

    dfs = []

    # ----------------------
    # ANOS ANTIGOS
    # ----------------------
    for arq in arquivos:
        print(f"Processando {arq.name}")

        df = carregar_microdados_antigos(arq)
        dfs.append(df)

    # ----------------------
    # 2025
    # ----------------------
    print("Processando microdados no formato vigente")

    assert ano >= 2025, "Formato moderno só vale para 2025+"

    anos = detectar_anos_formato_vigente(RAW_CENSO_DIR)

    for ano in anos:
        df = carregar_microdados_vigente(RAW_CENSO_DIR, ano)

    dfs.append(dfs)

    return dfs