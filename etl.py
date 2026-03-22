

def carregar_microdados_antigos(caminho_arquivo):

    import pandas as pd
    import gc

    df = pd.read_csv(
        caminho_arquivo,
        sep=";",
        encoding="latin-1",
        low_memory=False
    )

    df = df[df["SG_UF"] == "AC"].copy()

    return df


def detectar_anos_formato_vigente(raw_dir):
    """
    Detecta os anos do Censo Escolar disponíveis no formato novo (2025+).
    
    Parâmetros:
    -----------
    raw_dir : Path
        Diretório onde estão os arquivos CSV
    """

    arquivos = raw_dir.glob("Tabela_Escola_*.csv")

    anos = sorted([
        int(arq.stem.split("_")[-1])
        for arq in arquivos
    ])

    return anos


def carregar_microdados_vigente(raw_dir, ano):
    """
    Carrega os microdados do Censo Escolar no formato novo (2025+),
    filtrando apenas escolas do Acre e alinhando as demais tabelas.

    Parâmetros:
    -----------
    raw_dir : Path
        Diretório onde estão os arquivos CSV
    ano : int
        Ano do Censo (>= 2025)

    Retorno:
    --------
    tuple:
        df_escola, df_matricula, df_turma, df_docente
    """

    import pandas as pd
    import gc

    print(f"\n📅 Processando modelo moderno: {ano}")

    # ----------------------
    # ESCOLA (base)
    # ----------------------
    df_escola = pd.read_csv(
        raw_dir / f"Tabela_Escola_{ano}.csv",
        sep=";",
        encoding="latin-1",
        low_memory=False
    )

    df_escola = df_escola[
        df_escola["SG_UF"] == "AC"
    ].copy()

    escolas_validas = df_escola["CO_ENTIDADE"]

    gc.collect()

    # ----------------------
    # MATRÍCULA
    # ----------------------
    df_matricula = pd.read_csv(
        raw_dir / f"Tabela_Matricula_{ano}.csv",
        sep=";",
        encoding="latin-1",
        low_memory=False
    )

    df_matricula = df_matricula[
        df_matricula["CO_ENTIDADE"].isin(escolas_validas)
    ].copy()

    gc.collect()

    # ----------------------
    # TURMA
    # ----------------------
    df_turma = pd.read_csv(
        raw_dir / f"Tabela_Turma_{ano}.csv",
        sep=";",
        encoding="latin-1",
        low_memory=False
    )

    df_turma = df_turma[
        df_turma["CO_ENTIDADE"].isin(escolas_validas)
    ].copy()

    gc.collect()

    # ----------------------
    # DOCENTE
    # ----------------------
    df_docente = pd.read_csv(
        raw_dir / f"Tabela_Docente_{ano}.csv",
        sep=";",
        encoding="latin-1",
        low_memory=False
    )

    df_docente = df_docente[
        df_docente["CO_ENTIDADE"].isin(escolas_validas)
    ].copy()

    gc.collect()

    return df_escola, df_matricula, df_turma, df_docente