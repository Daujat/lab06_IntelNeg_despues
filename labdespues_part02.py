import pandas as pd
df = pd.read_csv('Compras_v2_imputado.csv', sep=',')

#nueva columna 'Salario_mas_10' sumando 10 al salario
df['Salario_mas_10'] = df['Salario'] + 10
print(df)