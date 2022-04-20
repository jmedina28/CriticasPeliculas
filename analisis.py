import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# esta función leerá el archivo y lo guardará en una variable
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
# función para calcular la media
def media(datos):
    productos = []
    for i in range(len(datos[0])):
        productos.append(datos[0][i]*datos[1][i])
    df = pd.DataFrame(datos) 
    df.insert(2,"Productos",productos,True)
    print(np.mean(df["Productos"])) 

print("La media de las críticas es: "), media(l)