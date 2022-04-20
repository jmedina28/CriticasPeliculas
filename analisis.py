import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# esta funcion leera el archivo y lo guardara en una variable
def leer_archivo(archivo):
    datos = pd.read_csv(archivo, sep=',', header=None, skiprows=1)
    return datos
l = leer_archivo('criticas.csv')
print(l)