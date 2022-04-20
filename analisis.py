import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# esta función se encargará de leer los datos del archivo .csv
def lectura(archivo):
    data = pd.read_csv(archivo, sep=',', header=None)
    return data
print(lectura('criticas.csv'))