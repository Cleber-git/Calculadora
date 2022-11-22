import pandas as pd

vendas = {
    'Produto': ['Feijão', 'Arroz', 'Farinha', 'Macarrão', 'Goiabada'],
    'Preço': [10, 9.50, 8.45, 4.87, 5.50],
    'Data de venda':['21/11/2022', '19/08/2022', '12/07/2022', '09/07/2022', '29/06/2022']
}


pessoas = {
    'nome':['Cleber', 'Arthur', 'Larissa', 'Louize', 'Leone', 'Jaqueline'],
    'sobrenome':['Gonçalves', 'Gonçalves', 'Adorno', 'Santana', 'Alberto', 'Gonçalves'],
    'idade': [20, 19, 17, 21, 26, 20],
    'sexo': ['Masculino', 'Masculino', 'Feminino', 'Feminino', 'Masculino', 'Feminino']
}
vendas_df = pd.DataFrame(vendas)
# print(vendas_df)

# pegando colunas 

produtos = vendas_df[['Produto', 'Preço']]
# print(produtos)

# pegando linhas 

linha = vendas_df.loc[0:3]
# print(linha)

# outra forma 
# tree_line = vendas_df.head(3)
# print(tree_line)

# somar uma coluna
# coluna_preços = vendas_df['Preço'].sum()
# print(coluna_preços)

# deletando colunas ou linhas
# vendas_df = vendas_df.drop(['Data de venda'], axis=1)
# print(vendas_df)

# Outro grupo de dataframe
pessoas_df = pd.DataFrame(pessoas)
# print(pessoas_df)
meninas = pessoas_df.loc[pessoas_df['sexo'] == 'Feminino']
print()
print(meninas)
print('-=' * 25)
print()
