
import pandas as pd

def carregar_microdados_antigos(caminho_arquivo, schema_colunas):
    """
    Carrega os microdados do Censo Escolar no formato antigo (2024-),
    filtrando apenas escolas públicas ativas do Estado do Acre.

    Parâmetros:
    -----------
    raw_dir : Path
        Diretório onde estão os arquivos CSV
    schema_colunas : 
        lista de colunas de interesse

    """
    df = pd.read_csv(
        caminho_arquivo,
        sep=";",
        encoding="latin-1",
        low_memory=False
    )

    df = df[
        (df['SG_UF'] == "AC") &
        (df['TP_DEPENDENCIA'] != 4) & # exclui escolas privadas
        (df['TP_SITUACAO_FUNCIONAMENTO'] == 1) # seleciona somente escolas ativas
        ].copy()
    
    # adiciona colunas faltantes
    #for col in schema_colunas:
    #    if col not in df.columns:
    #        df[col] = pd.NA

    colunas_faltantes = [col for col in schema_colunas if col not in df.columns]

    df_faltantes = pd.DataFrame({col: pd.NA for col in colunas_faltantes}, index=df.index)

    df = pd.concat([df, df_faltantes], axis=1)

    # garante ordem do schema
    df = df[schema_colunas].copy()

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


def carregar_microdados_vigente(raw_dir, ano, schema_colunas):

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
        (df_escola['SG_UF'] == "AC") &
        (df_escola['TP_DEPENDENCIA'] != 4) &
        (df_escola['TP_SITUACAO_FUNCIONAMENTO'] == 1)
    ].copy()

    escolas_validas = df_escola["CO_ENTIDADE"]

    # ----------------------
    # MATRÍCULA → AGREGAR
    # ----------------------
    df_matricula = pd.read_csv(
        raw_dir / f"Tabela_Matricula_{ano}.csv",
        sep=";",
        encoding="latin-1",
        low_memory=False
    )

    df_matricula = df_matricula[
        df_matricula["CO_ENTIDADE"].isin(escolas_validas)
    ]

    df_matricula_agg = (
        df_matricula
        .groupby("CO_ENTIDADE")
        .size()
        .reset_index(name="QT_MAT_BAS")
    )

    # ----------------------
    # TURMA → AGREGAR
    # ----------------------
    df_turma = pd.read_csv(
        raw_dir / f"Tabela_Turma_{ano}.csv",
        sep=";",
        encoding="latin-1",
        low_memory=False
    )

    df_turma = df_turma[
        df_turma["CO_ENTIDADE"].isin(escolas_validas)
    ]

    df_turma_agg = (
        df_turma
        .groupby("CO_ENTIDADE")
        .size()
        .reset_index(name="QT_TURMAS")
    )

    # ----------------------
    # DOCENTE → AGREGAR
    # ----------------------
    df_docente = pd.read_csv(
        raw_dir / f"Tabela_Docente_{ano}.csv",
        sep=";",
        encoding="latin-1",
        low_memory=False
    )

    df_docente = df_docente[
        df_docente["CO_ENTIDADE"].isin(escolas_validas)
    ]

    df_docente_agg = (
        df_docente
        .groupby("CO_ENTIDADE")
        .size()
        .reset_index(name="QT_DOCENTES")
    )

    # ----------------------
    # MERGE FINAL
    # ----------------------
    df_final = df_escola.copy()

    df_final = df_final.merge(df_matricula_agg, on="CO_ENTIDADE", how="left")
    df_final = df_final.merge(df_turma_agg, on="CO_ENTIDADE", how="left")
    df_final = df_final.merge(df_docente_agg, on="CO_ENTIDADE", how="left")

    # adicionar ano
    df_final["NU_ANO_CENSO"] = ano

    # ----------------------
    # PADRONIZAÇÃO DO SCHEMA
    # ----------------------
    colunas_faltantes = [col for col in schema_colunas if col not in df_final.columns]

    df_faltantes = pd.DataFrame({col: pd.NA for col in colunas_faltantes}, index=df_final.index)
    
    df_final = pd.concat([df_final, df_faltantes], axis=1)

    df_final = df_final[schema_colunas].copy()

    return df_final


def gerar_panorama(df, colunas):

    colunas_validas = [col for col in colunas if col in df.columns]

    return df[colunas_validas].copy()