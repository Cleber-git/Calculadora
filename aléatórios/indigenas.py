import pandas as pd


total = {
    'anos': [1991, 2000, 2010],
    
    'total': [146815790, 169872856, 190755799],
    
    'não indigenas': [145.986780, 167.932053, 189931228],
    
    'indigenas': [294131, 734127, 817963]
}

urbano = {
    'anos': [1991, 2000, 2010],
    'Urbana(1)': [110996829, 137925238, 160925792],
    'Não indígena':	[110494732, 136620255, 160605299],
    'Indígena':	[71026, 383298, 315180]
}

rural = {
    'anos': [1991, 2000, 2010],
    'Rural(1)':	[35818961, 31947618, 29830007],
    'Não indígena':	[35492049, 31311798, 29325929],
    'Indígena':	[223105, 350829, 502783]
}
# Criando a tabela
total_df = pd.DataFrame(total)

# criando tabela2
urbano_df = pd.DataFrame(urbano)

# criando tabela3
rural_df  = pd.DataFrame(rural)


# juntando tabelas
total_df1 = total_df.append(urbano_df)
total_df2 = total_df1.append(rural_df)


# exibindo tabela
# print(total_df2)
total_df2 = total_df2.ffill()
print(total_df2)
total_df2[['Urbana(1)', 'Não indígena', 'Indígena', 'Rural(1)']] = total_df2[['Urbana(1)', 'Não indígena', 'Indígena', 'Rural(1)']].fillna(total_df2[['Urbana(1)', 'Não indígena', 'Indígena', 'Rural(1)']].mean())
print(total_df2)
