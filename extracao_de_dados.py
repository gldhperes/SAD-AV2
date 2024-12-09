import pandas as pd

# Caminho para o arquivo .csv
arquivo_csv = '../MICRODADOS_ENEM_2023.csv'

dados = pd.read_csv(arquivo_csv, encoding='latin1', sep=';')

Fato_Desempenho = [

    # CHAVES ESTRANGEIRAS
    'NU_INSCRICAO',
    'CO_UF_ESC',
    'CO_UF_PROVA',
    'CO_MUNICIPIO_ESC',
    'CO_MUNICIPIO_PROVA',
    'TP_ESCOLA',
    'TP_SEXO',
    'TP_FAIXA_ETARIA',
    'TP_COR_RACA',

    # MEDIDAS
    'NU_NOTA_CN',
    'NU_NOTA_CH',
    'NU_NOTA_LC',
    'NU_NOTA_MT',
    'NU_NOTA_REDACAO',
    'NU_NOTA_COMP1',
    'NU_NOTA_COMP2',
    'NU_NOTA_COMP3',
    'NU_NOTA_COMP4',
    'NU_NOTA_COMP5',
]

Dim_Aluno = [
    'NU_INSCRICAO',
    'TP_FAIXA_ETARIA',
    'TP_SEXO',
    'TP_ESTADO_CIVIL',
    'TP_COR_RACA',
    'TP_NACIONALIDADE',
    'TP_ST_CONCLUSAO',
    'TP_ANO_CONCLUIU',
    'IN_TREINEIRO'
]

Dim_Escola = [
    'CO_MUNICIPIO_ESC',
    'NO_MUNICIPIO_ESC',
    'CO_UF_ESC',
    'SG_UF_ESC',
    'TP_DEPENDENCIA_ADM_ESC',
    'TP_LOCALIZACAO_ESC',
    'TP_SIT_FUNC_ESC'
]

Dim_Local_Prova = [
    'CO_MUNICIPIO_PROVA',
    'NO_MUNICIPIO_PROVA',
    'CO_UF_PROVA',
    'SG_UF_PROVA'
]

Dim_Socioeconômica = [
    'NU_INSCRICAO',
    'Q001',
    'Q002',
    'Q003',
    'Q004',
    'Q005',
    'Q006',
    'Q007',
    'Q008',
    'Q009',
    'Q010',
    'Q011',
    'Q012',
    'Q013',
    'Q014',
    'Q015',
    'Q016',
    'Q017',
    'Q018',
    'Q019',
    'Q020',
    'Q021',
    'Q022',
    'Q023',
    'Q024',
    'Q025'
]

Dim_Tipo_Escola = [
    'TP_ESCOLA',
    'TP_ENSINO'
]

Dim_Provas = [
    'CO_PROVA_CN',
    'CO_PROVA_CH',
    'CO_PROVA_LC',
    'CO_PROVA_MT',
    'TP_PRESENCA_CN',
    'TP_PRESENCA_CH',
    'TP_PRESENCA_LC',
    'TP_PRESENCA_MT',
    'TP_LINGUA'
]


def Extracao_Tabelas(name, tabela):
    dados_combinados = dados[tabela]
    nome_arquivo = f"{name}.csv"  # Define o nome do arquivo com base na tabela
    dados_combinados.to_csv(nome_arquivo, index=False, encoding='latin1')

Extracao_Tabelas('Fato_Desempenho', Fato_Desempenho)
Extracao_Tabelas('Dim_Aluno', Dim_Aluno)
Extracao_Tabelas('Dim_Escola', Dim_Escola)
Extracao_Tabelas('Dim_Local_Prova', Dim_Local_Prova)
Extracao_Tabelas('Dim_Socioeconômica', Dim_Socioeconômica)
Extracao_Tabelas('Dim_Tipo_Escola', Dim_Tipo_Escola)
Extracao_Tabelas('Dim_Provas', Dim_Provas)