
import pandas as pd

anio_inicio = int(input ("ingrese un año de inicio"))
anio_final = int(input ("ingrese un año final"))
ventas = {}

for i in range (anio_inicio, anio_final + 1):
    ventas [i] = int (input('Introduce las ventas del año ' + str(i) +': '))

    
var_series = pd.Series(ventas)
print(var_series.size)
# print(var_series[0])
print(var_series[2022])