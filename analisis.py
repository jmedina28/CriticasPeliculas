import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# esta funcion leera el archivo y lo guardara en una variable
def leer_archivo(archivo):
    datos = pd.read_csv(archivo, sep=',', header=None, skiprows=1)
    return datos
l = leer_archivo('criticas.csv')
print(l)
# la siguiente función crea un diagrama de barras con los datos
def diagrama_barras(datos, titulo, x, y):
    plt.bar(datos[x], datos[y]) ,plt.title(titulo)
    plt.xlabel("Opinión"), plt.ylabel("Cantidad de votantes")
    plt.show()
diagrama_barras(l, 'Estudio sobre las críticas de una película', 0, 1)