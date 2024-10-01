import pandas as pd
df = pd.read_csv('Compras_v2_imputado.csv')

#variables dummy para la columna Region
region_dummies = pd.get_dummies(df['Region'], prefix='Region')

#Eliminar la columna original Region
df = df.drop('Region', axis=1)

#Concatenar las nuevas columnas dummy al dataframe original
df = pd.concat([df, region_dummies], axis=1)

print(df)