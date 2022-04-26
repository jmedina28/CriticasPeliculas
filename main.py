import pandas as pnd
import estadistica as jmp
import numpy as np

datos = pnd.read_csv("criticas.csv", header=0 , sep =",")
lista_notas = list(datos["Opinión"])
observaciones = pnd.DataFrame({'NOTAS': lista_notas})
#--- ANALISIS DE UNA CARACTERISTICA ---
stats = jmp.JMPEstadisticas(observaciones['NOTAS'])
stats.analisisCaracteristica()