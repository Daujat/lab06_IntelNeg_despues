import pandas as pd
df = pd.read_csv('Compras_v2_imputado.csv')

#nueva columna 'compras_nombre' basada en 'Compra'
df['compras_nombre'] = df['Compra'].apply(lambda x: 'compro_si' if x == 1 else 'compro_no')

print(df)