import pandas as pd


# importando uma tabela específica
vendas_df = pd.read_excel('Vendas.xlsx')

# exibir tabela
# print(vendas_df)


# exibir as dez prinmeiras linhas
vendas_df = vendas_df.head(10)
# print(vendas_df)


# exibir colunas específicas
vendas_df = vendas_df.loc[:, ['ID Loja', 'Produto', 'Valor Unitário']]
# print(vendas_df)

#  deletar coluna específica 
# vendas_df = vendas_df.drop('ID Loja', axis=1)
# print(vendas_df)

# criar coluna
vendas_df['Comissão'] = vendas_df['Valor Unitário'] * 0.05
# print(vendas_df)

# filtrando tabela
vendas_df_norte = vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping']
print(vendas_df_norte)