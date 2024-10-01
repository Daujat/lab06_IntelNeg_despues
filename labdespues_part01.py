import pandas as pd
data = pd.read_csv('Compras_v2.csv', delimiter=';')

#variable Genero
data['Genero'].fillna('Desconocido', inplace=True)

#variable Edad
data['Edad'].fillna(data['Edad'].median(), inplace=True)

#variable Salario
data['Salario'].fillna(data['Salario'].mean(), inplace=True)

#variable Compra
data['Compra'].fillna(data['Compra'].mode()[0], inplace=True)

#variable "Region"
data['Region'].fillna('Desconocida', inplace=True)

#variable Deuda_tc
data['Deuda_tc'].fillna(data['Deuda_tc'].median(), inplace=True)

#nuevo archivo CSV
data.to_csv('Compras_v2_imputado.csv', index=False)

print("Imputación completada. El conjunto de datos imputado se ha guardado en 'Compras_v2_imputado.csv'.")