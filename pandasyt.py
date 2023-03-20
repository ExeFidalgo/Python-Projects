import pandas as pd

df = pd.read_csv('https://infra.datos.gob.ar/catalog/sspm/dataset/444/distribution/444.1/download/canastas-basicas-ciudad-de-buenos-aires.csv')

print(df['canasta_basica_total'])