import pandas as pd
import numpy as np



# print 1 Importação dos dados, Base Varejo.csv
# Carregando a base e realizando a delimitador é ponto e vírgula

df = pd.read_csv('Base_Varejo.csv', sep=';', encoding='latin1')

# Removendo as colunas vazias que vieram na Base devido aos ; no final de cada linha
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Visualizando as primeiras linhas da base
print(df.head())