import pandas as pd
import time 

df = pd.read_csv(
'https://infra.datos.gob.ar/catalog/sspm/dataset/444/distribution/444.1/download/canastas-basicas-ciudad-de-buenos-aires.csv')

print (df)

time.sleep(3)
# print(df.max(name = "canasta_basica_total"))

print(df ['canasta_basica_total'].max())
print(df["canasta_basica_total"].max())




