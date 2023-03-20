import pandas as pd

df = pd.read_csv('https://infra.datos.gob.ar/catalog/sspm/dataset/444/distribution/444.1/download/canastas-basicas-ciudad-de-buenos-aires.csv ')

print(df['canasta_basica_total'])
print(df['canasta_basica_alimentaria'])
print(df['indice_tiempo'])

print('Canasta basica total maxima')
print(df ['canasta_basica_total'].max())
print('Canasta basica alimentaria minima')
print(df["canasta_basica_alimentaria"].min())


descripcion = df.describe()
print('Descripcion de la tabla: ' )
print(descripcion)

diezfilas =  df.head(10)
print('Primeras 10 filas de la tabla: ')
print(diezfilas)

veinte_ultimas = df.tail(20)
print('Ultimas veinte filas de la tabla')
print(veinte_ultimas)

