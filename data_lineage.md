# 📊 Data Lineage — ETL Censo Escolar (Observatório Curica)

## 1. Visão Geral

Este documento descreve o fluxo de dados (data lineage) do pipeline ETL desenvolvido para o processamento dos microdados do Censo Escolar, com foco na geração de datasets analíticos (panoramas) utilizados no Observatório Curica.

O pipeline segue uma arquitetura em camadas, com separação entre dados brutos, dados intermediários e dados processados.

---

## 2. Camadas do Pipeline

### 🔹 2.1. Camada RAW (Entrada)

**Local:** `data/raw/`
**Fonte:** INEP — Microdados do Censo Escolar

#### Estrutura:

* **Modelo antigo (até 2024):**

  * `microdados_ed_basica_<ano>.csv`
  * Unidade: 1 linha por escola

* **Modelo vigente (2025+):**

  * `Tabela_Escola_<ano>.csv`
  * `Tabela_Matricula_<ano>.csv`
  * `Tabela_Turma_<ano>.csv`
  * `Tabela_Docente_<ano>.csv`

#### Características:

* Dados brutos, sem transformação
* Não sofrem alterações
* Fonte única da verdade (source of truth)

---

### 🔹 2.2. Camada INTERIM (Processamento)

**Local:** `data/interim/`
**Arquivo gerado:** `df_censo.csv`

#### Processos aplicados:

##### 📌 Modelo Antigo (2019–2024)

* Leitura dos arquivos CSV
* Filtros:

  * `SG_UF == "AC"`
  * `TP_DEPENDENCIA != 4` (exclui escolas privadas)
  * `TP_SITUACAO_FUNCIONAMENTO == 1` (somente escolas ativas)
* Padronização de schema:

  * Seleção de colunas existentes
  * Inclusão de colunas ausentes com `NaN`

##### 📌 Modelo Vigente (2025+)

* Leitura das tabelas separadas
* Filtro de escolas válidas (Acre, públicas, ativas)
* Subconjunto das demais tabelas via `CO_ENTIDADE`
* Agregações:

  * Matrículas → `QT_MAT_BAS`
  * Turmas → `QT_TURMAS`
  * Docentes → `QT_DOCENTES`
* Merge final:

  * Base: `df_escola`
  * Junção com agregações por `CO_ENTIDADE`
* Inclusão do campo `NU_ANO_CENSO`
* Padronização de schema (compatível com anos anteriores)

##### 📌 Consolidação

* Concatenação de todos os anos (`pd.concat`)
* Geração do dataframe unificado `df_censo`

---

### 🔹 2.3. Camada PROCESSED (Saída Analítica)

**Local:** `data/processed/`
**Arquivos gerados:**

* `df_panorama_rede.csv`
* `df_agua_potavel.csv`
* (outros panoramas conforme expansão)

#### Processos aplicados:

* Projeção de colunas por panorama:

  * Baseada no dicionário `SCHEMAS_PANORAMAS`
* Seleção segura de colunas:

  * Apenas colunas existentes no dataframe são consideradas
* Geração de dataframes especializados por tema

#### Resultado:

* Dataframes leves
* Estruturados para consumo analítico
* Independentes entre si

---

## 3. Fluxo de Transformação

```text
RAW (CSV INEP)
   ↓
Leitura e Filtragem
   ↓
Padronização de Schema
   ↓
(2025+) Agregações + Merge
   ↓
Concatenação (todos os anos)
   ↓
df_censo (INTERIM)
   ↓
Projeção por Panorama
   ↓
Arquivos CSV (PROCESSED)
```

---

## 4. Regras de Negócio Aplicadas

* Exclusão de escolas privadas (`TP_DEPENDENCIA != 4`)
* Consideração apenas de escolas ativas (`TP_SITUACAO_FUNCIONAMENTO == 1`)
* Restrição geográfica ao Estado do Acre (`SG_UF == "AC"`)
* Agregação por escola (`CO_ENTIDADE`) no modelo vigente
* Manutenção de valores ausentes como `NaN`
* Padronização de schema entre diferentes anos

---

## 5. Estrutura de Dependências

| Camada    | Dependência                              |
| --------- | ---------------------------------------- |
| RAW       | Arquivos CSV do INEP                     |
| INTERIM   | Funções ETL (`etl.py`) + `SCHEMA_CURICA` |
| PROCESSED | `df_censo` + `SCHEMAS_PANORAMAS`         |

---

## 6. Características do Pipeline

* ✔ Processamento batch
* ✔ Arquitetura em camadas (raw → interim → processed)
* ✔ Padronização de schema entre anos heterogêneos
* ✔ Separação entre lógica de transformação e configuração (schemas)
* ✔ Escalável para novos panoramas
* ✔ Preparado para evolução incremental

---

## 7. Considerações Finais

O pipeline foi projetado para garantir:

* Consistência estrutural dos dados ao longo dos anos
* Flexibilidade para inclusão de novos indicadores
* Baixo acoplamento entre ETL e camada de visualização
* Facilidade de manutenção e evolução

Este data lineage serve como base para governança de dados, documentação técnica e futuras evoluções do Observatório Curica.

---
