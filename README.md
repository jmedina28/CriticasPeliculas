<h1 align="center">Críticas de películas</h1>

---
En este [repositorio](https://github.com/jmedina28/CriticasPeliculas) queda resuelto el ejercicio de críticas de películas. Para llevar a cabo el proyecto me he documentado a través de la teoría que se encuentra en el campus virtual y otras fuentes.
***
## Ejercicio 
Para conocer mejor la distribución gaussiana, vamos a dejar a un lado las notas obtenidas en el examen y vamos a concentrarnos en las críticas de películas.

Estas son las opiniones (calificadas de 0 a 5) obtenidas por una película, donde 5 es la mejor nota que puede obtener la película: las famosas 5 estrellas que podemos encontrar en todos los sitios de críticas de cine.

Curva de Gauss

Ante este tipo de gráfico, podemos afirmar que la serie de observaciones sigue una ley matemática llamada ley normal o ley de Gauss (en honor a Karl Friederich Gauss (1777-1855)).

En estadística y en probabilidad, la ley normal permite representar muchos fenómenos aleatorios naturales. Cuando una serie de observaciones obedece a la ley normal, se puede afirmar:

El 50 % de las observaciones están por encima de la media.

El 50 % de las observaciones están por debajo de la media.

El 68 % de las observaciones están comprendidas en el intervalo que va desde la media - la desviación típica hasta la media + la desviación típica.

El 95 % de las observaciones están comprendidas en el intervalo que va desde la media - 2* la desviación típica hasta la media + 2* la desviación típica.

El 99,7 % de las observaciones están comprendidas en el intervalo que va desde la media - 3* la desviación típica hasta la media + 3* la desviación típica.

Ahora vamos a hacer algunos cálculos que al mismo tiempo nos permitirán ver cómo utilizar la idea de frecuencia en los cálculos de media y de desviación típica.

Las opiniones corresponden a nuestros valores observados denominados Xi, y la cantidad de votantes se equipara a la cantidad de veces en que el valor observado ha sido elegido por los espectadores. Entonces hablamos de frecuencia de elección, que se denomina Ni.

A fin de calcular la media de esta serie de observaciones, para cada observación hay que realizar el producto de las opiniones por la cantidad de votantes:

Lo que da un valor de 1,35 para la desviación típica.

Ahora le toca a usted examinar el reparto de las observaciones en función de las desviaciones entre la media y la desviación típica que permite definir los 68 %, 95 % y 97 % de repartos.

Como ejemplo, podemos comprobar que el 68 % de las observaciones están comprendidas en el intervalo [1,3]. Los límites del intervalo se han determinado mediante la resta de la desviación típica a la media para el límite inferior y la suma de la desviación típica a la media para el límite superior. 

El código empleado para resolverlo es el siguiente: 
```python
from collections import Counter
from math import *
import matplotlib.pyplot as plt
import pandas as pd


class JMPEstadisticas:

    def __init__(self,caracteristica):
        self.caracteristica = caracteristica

    def leer_archivo(archivo):
        datos = pd.read_csv(archivo, sep=',', header=None, skiprows=1)
        return datos
    l = leer_archivo('criticas.csv')

    def diagrama_barras(datos, titulo, x, y):
        plt.bar(datos[x], datos[y]) ,plt.title(titulo)
        plt.xlabel("Opinión"), plt.ylabel("Cantidad de votantes")
        plt.show()
    diagrama_barras(l, 'Estudio sobre las críticas de una película', 0, 1)
    
    
    def calculoMediaAritmetica(self):

        n = self.caracteristica.count()
        sumaValoresObservaciones = 0
        mediaAritmetica = 0
        for valorObservacion in self.caracteristica:
            sumaValoresObservaciones = sumaValoresObservaciones + valorObservacion

        mediaAritmetica = sumaValoresObservaciones / n
        return mediaAritmetica

    def calculoMediana(self):
        mediana = 0
        caracteristica = self.caracteristica.sort_values()
        caracteristica = caracteristica.reset_index(drop=True)
        n = self.caracteristica.count()
        par = False;
        if (n % 2 == 0):
            print("La cantidad de observaciones es par.")
            par = True

        if par:
            rango = (n / 2);
            print("RANGO = "+str(rango))
            rangoPython = rango-1
            valor1 = caracteristica[rangoPython]
            valor2 = caracteristica[rangoPython+1]
            mediana = valor1 +((valor2-valor1)/2)
        else:
            rango = ((n + 1) / 2)
            rangoPython = rango - 1
            mediana = caracteristica[rangoPython]

        return [mediana, rango]

    def calculoModa(self):
        moda = Counter(self.caracteristica)
        return moda

    def calculoVarianzaDesviacionTipica(self):
        n = self.caracteristica.count()
        mediaAritmetica = self.caracteristica.mean()
        varianza = 0
        c3 = 0
        for valorObservacion in self.caracteristica:
            x = valorObservacion
            moy = mediaAritmetica
            c1 = valorObservacion - mediaAritmetica
            c2 = c1 * c1
            c3 = c3 + c2

        varianza = c3 / (n - 1)

        desviacionTipica = sqrt(varianza)

        return ([varianza, desviacionTipica])

    def calculoDelosCuartiles(self,mediana,rangoMediana):
        n = self.caracteristica.count()
        sort_caracteristica = self.caracteristica.sort_values()
        sort_caracteristica = sort_caracteristica.reset_index(drop=True)
        q1 = 0
        q2 = mediana
        q3 = 0

        #Cálculo Q1
        restoDivision = rangoMediana%2
        if (restoDivision != 0):
            q1 = sort_caracteristica[((rangoMediana/2)+1)-1]
        else:
            valorMin = sort_caracteristica[((rangoMediana/2)-1)]
            valorMax = sort_caracteristica[(rangoMediana/2)]
            q1 = (valorMin + ((valorMax - valorMin) / 2) + valorMax) / 2

        # Cálculo Q3
        nbdatos = len(sort_caracteristica)+1
        nbDatosDesdeMediana = nbdatos - rangoMediana
        restoDivision = nbDatosDesdeMediana % 2
        if (restoDivision != 0):
            q3 = sort_caracteristica[(rangoMediana+ceil(nbDatosDesdeMediana/2))-1]
        else:
            valorMinQ3 = sort_caracteristica[(rangoMediana+(nbDatosDesdeMediana/2))-1]
            valorMaxQ3 = sort_caracteristica[(rangoMediana+(nbDatosDesdeMediana/2))]
            q3 = (valorMin + ((valorMax - valorMin) / 2) + valorMax) / 2


        return ([q1, q2, q3])


    def criterioDeTukey(self, primerCuartil, tercerCuartil):

        valoresAberrantesInferiores = []
        valoresAberrantesSuperiores = []
        caracteristica = self.caracteristica.sort_values()
        intercuartil = tercerCuartil - primerCuartil
        print("Inter-cuartil = "+str(intercuartil))
        limiteInferior = primerCuartil - (1.5 * intercuartil)
        limiteSuperior = tercerCuartil + (1.5 * intercuartil)

        for valorObservacion in caracteristica:
            if valorObservacion < limiteInferior:
                valoresAberrantesInferiores.append(valorObservacion)

            if valorObservacion > limiteSuperior:
                valoresAberrantesSuperiores.append(valorObservacion)

        valoresAberrantes = valoresAberrantesInferiores + valoresAberrantesSuperiores

        return (valoresAberrantes)



    def visualizacion(self,media,mediana,cuartil_1,cuartil_2,cuartil_3):

        plt.subplot(2, 2, 1)
        plt.hist(self.caracteristica)
        plt.title("Histograma y media")
        plt.axvline(media, color='red', linestyle='dashed', linewidth=1,label = str(media))
        plt.legend(loc='upper right')

        plt.subplot(2, 2, 2)
        plt.hist(self.caracteristica)
        plt.title("Histograma y mediana")
        plt.axvline(mediana, color='green', linestyle='dashed', linewidth=1,label = str(mediana))
        plt.legend(loc='upper right')

        plt.subplot(2, 2, 3)
        plt.hist(self.caracteristica)
        plt.title("Histograma y cuartiles")
        plt.axvline(cuartil_1, color='orange', linestyle='dashed', linewidth=1,label = "Q1: "+str(cuartil_1))
        plt.axvline(cuartil_2, color='orange', linestyle='dashed', linewidth=1,label = "Q2: "+str(cuartil_2))
        plt.axvline(cuartil_3, color='orange', linestyle='dashed', linewidth=1,label = "Q3: "+str(cuartil_3))
        plt.legend(loc='upper right')

        plt.subplot(2, 2, 4)
        plt.boxplot(self.caracteristica)
        plt.title("Diagrama de caja y bigotes")
        plt.show()


    def analisisCaracteristica(self):

        print("-----------------------------------------")
        print("      MEDIDA DE TENDENCIA CENTRAL        ")
        print("-----------------------------------------\n")

        print("-- CANTIDAD DE OBSERVACIONES --")
        # -Cantidad de observaciones
        n = self.caracteristica.count()
        print("Cantidad de observaciones = " + str(n))

        print ("\n-- MIN --")
        valoresOrdenados = self.caracteristica.sort_values()
        valoresOrdenados = valoresOrdenados.reset_index(drop=True)
        print("Valor mínimo: "+str(valoresOrdenados[0]))

        print ("\n-- MAX --")
        valoresOrdenados = self.caracteristica.sort_values()
        valoresOrdenados = valoresOrdenados.reset_index(drop=True)
        print("Valor máximo: " + str(valoresOrdenados[len(valoresOrdenados)-1]))

        # -Media artimética:
        print("\n-- MEDIA --")
        media = self.calculoMediaAritmetica()
        print("Media aritmética calculada = " + str(media))
        print("> Observaciones: Si todas las observaciones tuvieran el mismo valor (reparto equitativo), este sería " + str(media))

        # -Media aritmética:
        print("\n-- MEDIANA --")
        mediana = self.calculoMediana()
        print("Mediana calculada = " + str(mediana[0]))
        print("> Observaciones: El valor que se encuentra en el punto medio de las observaciones es:" + str(mediana[0]))
        print("El reparto es: " + str(mediana[1]) + " valores en cada lado de la mediana")

        # -Moda
        print("\n-- MODA --")
        moda = self.calculoModa()
        print(moda)
        print("> Observacions: La moda permite determinar los valores observados con más frecuencia")


        print("\n\n-----------------------------------------")
        print("      MEDIDA DE DISPERSION        ")
        print("-----------------------------------------\n")
        print("-- RANGO --")
        print ("Rango de la serie = "+str(valoresOrdenados[len(valoresOrdenados)-1]-valoresOrdenados[0]))
        varianzaDesviacionTipica = self.calculoVarianzaDesviacionTipica()

        print("\n-- VARIANZA --")
        print("Varianza calculada = " + str(varianzaDesviacionTipica[0]))

        print("\n-- DESVIACION TIPICA --")
        print("Desviación típica calculada = " + str(varianzaDesviacionTipica[1]))
        desviacionTipica = varianzaDesviacionTipica[1]
        print("68 % de los valores de las observaciones se sitúan entre " + str(media - desviacionTipica) + " y " + str(
            media + desviacionTipica))
        print("95 % de los valores de las observaciones se sitúan entre " + str(media - (desviacionTipica * 2)) + " y " + str(
            media + (desviacionTipica * 2)))
        print("99 % de los valores de las observaciones se sitúan entre " + str(media - (desviacionTipica * 3)) + " y " + str(
            media + (desviacionTipica * 3)))

        print("\n\n-----------------------------------------")
        print("      CUARTILES        ")
        print("-----------------------------------------\n")
        cuartiles = self.calculoDelosCuartiles(mediana[0],mediana[1])
        print("25 % de las observaciones tienen un valor inferior a " + str(cuartiles[0]))
        print("50 % de las observaciones tienen un valor inferior a " + str(cuartiles[1]))
        print("75 % de las observaciones tienen un valor inferior a " + str(cuartiles[2]))


        print("\n\n-----------------------------------------")
        print("      DETECCION VALORES ABERRANTES        ")
        print("-----------------------------------------\n")
        print("> Criterios de Tukey")
        valoresAberrantes = self.criterioDeTukey(cuartiles[0], cuartiles[2])
        print("Cantidad de valores aberrantes: " + str(len(valoresAberrantes)))
        print("Valores:" + str(valoresAberrantes))


        print("\n\n-----------------------------------------")
        print("      VISUALIZACION        ")
        print("-----------------------------------------\n")
        print("Generación de las gráficas...")
        self.visualizacion(media,mediana[0],cuartiles[0],cuartiles[1],cuartiles[2])
```
