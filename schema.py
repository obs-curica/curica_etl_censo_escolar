# Esquema que define as colunas de interesse
SCHEMA_CURICA = [

    # ESCOLAS
    # identificação
    'NU_ANO_CENSO',
    'SG_UF',
    'NO_MUNICIPIO',
    'CO_MUNICIPIO',
    'CO_ENTIDADE',
    'NO_ENTIDADE',
    
    # caracterização
    'TP_DEPENDENCIA',
    'TP_LOCALIZACAO',
    'TP_LOCALIZACAO_DIFERENCIADA',
    'DS_ENDERECO',
    'NU_ENDERECO',
    'DS_COMPLEMENTO',
    'NO_BAIRRO',
    'CO_CEP',
    'TP_SITUACAO_FUNCIONAMENTO',
    'LATITUDE',
    'LONGITUDE',
    
    # infra prédio
    'IN_LOCAL_FUNC_PREDIO_ESCOLAR',
    'TP_OCUPACAO_PREDIO_ESCOLAR',
    'IN_LOCAL_FUNC_GALPAO',
    'IN_LOCAL_FUNC_SALAS_OUTRA_ESC',
    'IN_LOCAL_FUNC_OUTROS',
    'IN_PREDIO_COMPARTILHADO',

    # infra água
    'IN_AGUA_POTAVEL',
    'IN_AGUA_REDE_PUBLICA',
    'IN_AGUA_POCO_ARTESIANO',
    'IN_AGUA_CACIMBA',
    'IN_AGUA_FONTE_RIO',
    'IN_AGUA_INEXISTENTE',
    'IN_AGUA_CARRO_PIPA',
    'IN_ENERGIA_REDE_PUBLICA',

    # infra energia elétrica
    'IN_ENERGIA_REDE_PUBLICA',
    'IN_ENERGIA_GERADOR_FOSSIL',
    'IN_ENERGIA_RENOVAVEL',
    'IN_ENERGIA_INEXISTENTE',

    # infra esgoto
    'IN_ESGOTO_REDE_PUBLICA',
    'IN_ESGOTO_FOSSA_SEPTICA',
    'IN_ESGOTO_FOSSA_COMUM',
    'IN_ESGOTO_FOSSA',
    'IN_ESGOTO_INEXISTENTE',

    # infra dependências físicas
    'IN_ALMOXARIFADO',
    'IN_BANHEIRO', # infra prédio
    'IN_BANHEIRO_FUNCIONARIOS',
    'IN_BIBLIOTECA',
    'IN_BIBLIOTECA_SALA_LEITURA',
    'IN_COZINHA', # alimentacao escolar
    'IN_DESPENSA', # alimentacao escolar
    'IN_LABORATORIO_CIENCIAS',
    'IN_LABORATORIO_INFORMATICA',
    'IN_REFEITORIO',
    'IN_SALA_DIRETORIA',
    'IN_SALA_LEITURA',
    'IN_SALA_PROFESSOR',
    'IN_SECRETARIA',
    'IN_SALA_ATENDIMENTO_ESPECIAL',
    
    # salas utilizadas
    'QT_SALAS_UTILIZADAS_DENTRO',
    'QT_SALAS_UTILIZADAS_FORA',
    'QT_SALAS_UTILIZADAS',

    # equipamentos de informática e multimídia
    'IN_EQUIP_PARABOLICA',
    'IN_COMPUTADOR',
    'IN_EQUIP_COPIADORA',
    'IN_EQUIP_IMPRESSORA',
    'IN_EQUIP_IMPRESSORA_MULT',
    'IN_EQUIP_SCANNER',
    'IN_EQUIP_NENHUM',
    'IN_EQUIP_DVD',
    'QT_EQUIP_DVD',
    'IN_EQUIP_SOM',
    'QT_EQUIP_SOM',
    'IN_EQUIP_TV',
    'QT_EQUIP_TV',
    'IN_EQUIP_LOUSA_DIGITAL',
    'QT_EQUIP_LOUSA_DIGITAL',
    'IN_EQUIP_MULTIMIDIA',
    'QT_EQUIP_MULTIMIDIA',
    'IN_DESKTOP_ALUNO',
    'QT_DESKTOP_ALUNO',
    'IN_COMP_PORTATIL_ALUNO',
    'QT_COMP_PORTATIL_ALUNO',
    'IN_TABLET_ALUNO',
    'QT_TABLET_ALUNO',
    'IN_INTERNET', # disponibilidade de internet
    'IN_INTERNET_ALUNOS',
    'IN_INTERNET_ADMINISTRATIVO',
    'IN_INTERNET_APRENDIZAGEM',
    'IN_INTERNET_COMUNIDADE',
    'IN_ACESSO_INTERNET_COMPUTADOR',
    'IN_ACES_INTERNET_DISP_PESSOAIS',
    'TP_REDE_LOCAL',
    'IN_BANDA_LARGA',

    # recursos humanos
    'QT_PROF_ADMINISTRATIVOS',
    'QT_PROF_SERVICOS_GERAIS',
    'QT_PROF_ALIMENTACAO',
    'QT_PROF_SECRETARIO',
    'QT_PROF_SEGURANCA',
    'QT_PROF_MONITORES',
    'QT_PROF_GESTAO',
    
    # alimentação escolar
    'IN_ALIMENTACAO',

    # órgãos colegiados
    'IN_ORGAO_ASS_PAIS',
    'IN_ORGAO_ASS_PAIS_MESTRES',
    'IN_ORGAO_CONSELHO_ESCOLAR',
    'IN_ORGAO_GREMIO_ESTUDANTIL',
    'IN_ORGAO_OUTROS',
    'IN_ORGAO_NENHUM',

    # ensino especial
    'TP_AEE',
    'IN_COMUM_CRECHE',
    'IN_COMUM_PRE',
    'IN_COMUM_FUND_AI',
    'IN_COMUM_FUND_AF',
    'IN_COMUM_MEDIO_MEDIO',
    'IN_COMUM_MEDIO_INTEGRADO',
    'IN_COMUM_MEDIO_FIC',
    'IN_COMUM_MEDIO_NORMAL',
    'IN_ESP_EXCLUSIVA_CRECHE',
    'IN_ESP_EXCLUSIVA_PRE',
    'IN_ESP_EXCLUSIVA_FUND_AI',
    'IN_ESP_EXCLUSIVA_FUND_AF',
    'IN_ESP_EXCLUSIVA_MEDIO_MEDIO',
    'IN_ESP_EXCLUSIVA_MEDIO_INTEGR',
    'IN_ESP_EXCLUSIVA_MEDIO_FIC',
    'IN_ESP_EXCLUSIVA_MEDIO_NORMAL',

    # modalidade de ensino
    'IN_ESCOLARIZACAO', # qualquer etapa disponível com matrícula
    'IN_MEDIACAO_PRESENCIAL',
    'IN_MEDIACAO_SEMIPRESENCIAL',
    'IN_MEDIACAO_EAD',
    'IN_ESPECIAL_EXCLUSIVA',
    'IN_REGULAR',


    # MATRÍCULAS
    # quantidade de matrículas
    'QT_MAT_BAS', # total geral
    'QT_MAT_INF',
    'QT_MAT_INF_CRE',
    'QT_MAT_INF_PRE',
    'QT_MAT_FUND',
    'QT_MAT_FUND_AI',
    'QT_MAT_FUND_AI_1',
    'QT_MAT_FUND_AI_2',
    'QT_MAT_FUND_AI_3',
    'QT_MAT_FUND_AI_4',
    'QT_MAT_FUND_AI_5',
    'QT_MAT_FUND_AF',
    'QT_MAT_FUND_AF_6',
    'QT_MAT_FUND_AF_7',
    'QT_MAT_FUND_AF_8',
    'QT_MAT_FUND_AF_9',
    'QT_MAT_MED', # somatório de todas as modalidades
    'QT_MAT_MED_PROP', # é o tradicional
    'QT_MAT_MED_PROP_1', # 1o. ano
    'QT_MAT_MED_PROP_2',
    'QT_MAT_MED_PROP_3',
    'QT_MAT_MED_PROP_4',
    'QT_MAT_MED_PROP_NS', # não seriado!
    'QT_MAT_MED_IFTP_CT', # curso técnico
    'QT_MAT_MED_IFTP_QP', # itinerário formativo técnico
    'QT_MAT_MED_IFA', # itinerário formativo aprofundamento
    'QT_MAT_MED_NM', # magistério

    # matrículas ensino integral 
    'QT_MAT_INF_INT',
    'QT_MAT_INF_CRE_INT',
    'QT_MAT_INF_PRE_INT',
    'QT_MAT_FUND_INT',
    'QT_MAT_FUND_AI_INT',
    'QT_MAT_FUND_AF_INT',
    'QT_MAT_MED_INT',
    
    # matrículas educação especial
    'QT_MAT_ESP', 
    'QT_MAT_ESP_INF', # detalhamento a partir de 2025
    'QT_MAT_ESP_INF_CRE',
    'QT_MAT_ESP_INF_PRE',
    'QT_MAT_ESP_FUND',
    'QT_MAT_ESP_FUND_AI',
    'QT_MAT_ESP_FUND_AF',
    'QT_MAT_ESP_MED',

    # matrículas por turno, a partir de 2025
    'QT_MAT_INF_CRE_DM', # matutino
    'QT_MAT_INF_CRE_DV', # vespertino
    'QT_MAT_INF_CRE_N', # noturno
    'QT_MAT_INF_PRE_D',
    'QT_MAT_INF_PRE_DM',
    'QT_MAT_INF_PRE_DV',
    'QT_MAT_INF_PRE_N',
    'QT_MAT_FUND_D',
    'QT_MAT_FUND_DM',
    'QT_MAT_FUND_DV',
    'QT_MAT_FUND_N',
    'QT_MAT_FUND_AI_D',
    'QT_MAT_FUND_AI_DM',
    'QT_MAT_FUND_AI_DV',
    'QT_MAT_FUND_AI_N',
    'QT_MAT_FUND_AF_D',
    'QT_MAT_FUND_AF_DM',
    'QT_MAT_FUND_AF_DV',
    'QT_MAT_FUND_AF_N',
    'QT_MAT_MED_D',
    'QT_MAT_MED_DM',
    'QT_MAT_MED_DV',
    'QT_MAT_MED_N',

    # matrículas tempo integral
    'QT_MAT_INF_INT',
    'QT_MAT_INF_CRE_INT',
    'QT_MAT_INF_PRE_INT',
    'QT_MAT_FUND_INT',
    'QT_MAT_FUND_AI_INT',
    'QT_MAT_FUND_AF_INT',
    'QT_MAT_MED_INT',
    'QT_MAT_BAS_INT', # total, a partir de 2025

    # transporte escolar
    'QT_TRANSP_PUBLICO',
    'QT_TRANSP_RESP_EST',
    'QT_TRANSP_RESP_MUN',

    
    # DOCENTES
    # quantidade de docentes por etapa
    'QT_DOC_BAS',
    'QT_DOC_INF',
    'QT_DOC_INF_CRE',
    'QT_DOC_INF_PRE',
    'QT_DOC_FUND',
    'QT_DOC_FUND_AI',
    'QT_DOC_FUND_AI_1',
    'QT_DOC_FUND_AI_2',
    'QT_DOC_FUND_AI_3',
    'QT_DOC_FUND_AI_4',
    'QT_DOC_FUND_AI_5',
    'QT_DOC_FUND_AI_MULTIETAPA',
    'QT_DOC_FUND_AF',
    'QT_DOC_FUND_AF_6',
    'QT_DOC_FUND_AF_7',
    'QT_DOC_FUND_AF_8',
    'QT_DOC_FUND_AF_9',
    'QT_DOC_FUND_AF_MULTI',
    'QT_DOC_FUND_AF_CORRFLUXO',
    'QT_DOC_MED',
    'QT_DOC_MED_PROP',
    'QT_DOC_MED_PROP_1',
    'QT_DOC_MED_PROP_2',
    'QT_DOC_MED_PROP_3',
    'QT_DOC_MED_PROP_4',
    'QT_DOC_MED_PROP_NS', # Não seridado!
    'QT_DOC_ESP', # ensino especial
    'QT_DOC_ESP_CC', # ensino especial classes comuns
    'QT_DOC_ESP_CE', # ensino especial classes exclusivas
    
    # escolaridade dos docentes
    'QT_DOC_BAS_ESCO_EF',
    'QT_DOC_BAS_ESCO_EM',
    'QT_DOC_BAS_ESCO_SUP_GRAD',
    'QT_DOC_BAS_ESCO_SUP_GRAD_LICEN',
    'QT_DOC_BAS_ESCO_SUP_GRAD_SLICEN',
    'QT_DOC_BAS_ESCO_SUP_POS_ESPEC',
    'QT_DOC_BAS_ESCO_SUP_POS_MESTRA',
    'QT_DOC_BAS_ESCO_SUP_POS_DOUTO',
    'QT_DOC_BAS_ESCO_SUP_POS_NENHUM',
    
    # vínculo de trabalho dos docentes
    'QT_DOC_BAS_VINCULO_CONCUR',
    'QT_DOC_BAS_VINCULO_CONTRA',
    'QT_DOC_BAS_VINCULO_TERCEIR',
    'QT_DOC_BAS_VINCULO_CLT',

    # quantidade de docentes com cursos de formação continuada
    'QT_DOC_BAS_ESPEC_CRE',
    'QT_DOC_BAS_ESPEC_PRE_ESCOLA',
    'QT_DOC_BAS_ESPEC_ANOS_INICIAIS',
    'QT_DOC_BAS_ESPEC_ANOS_FINAIS',
    'QT_DOC_BAS_ESPEC_ENS_MEDIO',
    'QT_DOC_BAS_ESPEC_ED_ESPECIAL',

    # TURMAS
    # Quantidade de turmas
    'QT_TUR_BAS',
    'QT_TUR_INF',
    'QT_TUR_INF_CRE',
    'QT_TUR_INF_PRE',
    'QT_TUR_FUND',
    'QT_TUR_FUND_AI',
    'QT_TUR_FUND_AI_1',
    'QT_TUR_FUND_AI_2',
    'QT_TUR_FUND_AI_3',
    'QT_TUR_FUND_AI_4',
    'QT_TUR_FUND_AI_5',
    'QT_TUR_FUND_AI_MULTIETAPA', # multietapa
    'QT_TUR_FUND_AF',
    'QT_TUR_FUND_AF_6',
    'QT_TUR_FUND_AF_7',
    'QT_TUR_FUND_AF_8',
    'QT_TUR_FUND_AF_9',
    'QT_TUR_FUND_AF_MULTI', # multietapa
    'QT_TUR_FUND_AF_CORRFLUXO',
    'QT_TUR_MED',
    'QT_TUR_MED_PROP',
    'QT_TUR_MED_PROP_1',
    'QT_TUR_MED_PROP_2',
    'QT_TUR_MED_PROP_3',
    'QT_TUR_MED_PROP_4',
    'QT_TUR_MED_PROP_NS', # não seriado

    # turnos das turmas
    'QT_TUR_BAS_D',
    'QT_TUR_BAS_DM',
    'QT_TUR_BAS_DV',
    'QT_TUR_BAS_N',
    'QT_TUR_INF_CRE_D',
    'QT_TUR_INF_CRE_DM',
    'QT_TUR_INF_CRE_DV',
    'QT_TUR_INF_CRE_N',
    'QT_TUR_INF_PRE_D',
    'QT_TUR_INF_PRE_DM',
    'QT_TUR_INF_PRE_DV',
    'QT_TUR_INF_PRE_N',
    'QT_TUR_FUND_D',
    'QT_TUR_FUND_DM',
    'QT_TUR_FUND_DV',
    'QT_TUR_FUND_N',
    'QT_TUR_FUND_AI_D',
    'QT_TUR_FUND_AI_DM',
    'QT_TUR_FUND_AI_DV',
    'QT_TUR_FUND_AI_N',
    'QT_TUR_FUND_AF_D',
    'QT_TUR_FUND_AF_DM',
    'QT_TUR_FUND_AF_DV',
    'QT_TUR_FUND_AF_N',
    'QT_TUR_MED_D',
    'QT_TUR_MED_DM',
    'QT_TUR_MED_DV',
    'QT_TUR_MED_N',

    # ensino integral
    'QT_TUR_BAS_INT',
    'QT_TUR_INF_INT',
    'QT_TUR_INF_CRE_INT',
    'QT_TUR_INF_PRE_INT',
    'QT_TUR_FUND_INT',
    'QT_TUR_FUND_AI_INT',
    'QT_TUR_FUND_AF_INT',
    'QT_TUR_MED_INT',

    # ensino especial
    'QT_TUR_ESP',
    'QT_TUR_ESP_CC',
    'QT_TUR_ESP_CE',
    # turnos especial
    'QT_TUR_ESP_D',
    'QT_TUR_ESP_DM',
    'QT_TUR_ESP_DV',
    'QT_TUR_ESP_N',
    # especial integral
    'QT_TUR_ESP_INT',
    'QT_TUR_ESP_CC_INT',
    'QT_TUR_ESP_CE_INT',
]