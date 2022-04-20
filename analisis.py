import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# esta función se encargará de leer los datos del archivo .csv
def lectura(archivo):
    data = pd.read_csv(archivo, sep=',', header=None, skiprows= [0])
    return data
print(lectura('criticas.csv'))
# esta función se encargará de convertir los datos de la columna 0 a una lista
def convertir(data):
    lista0 = data[0].tolist()
    lista1 = data[1].tolist()
    return lista0, lista1
print(convertir(lectura('criticas.csv')))