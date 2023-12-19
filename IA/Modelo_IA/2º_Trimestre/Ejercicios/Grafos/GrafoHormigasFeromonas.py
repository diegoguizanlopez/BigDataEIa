"""
Algoritmo de la colonia de hormigas

Hay un número máximo de iteraciones: maxiter
Dentro de cada iteración un número máximo de saltos: maxtrans
Hay una ciudad objetivo: target
en cada iteración se crean un número de hormigas totalh y se disponen aleatoriamente
por todas las ciudades
En cada arista del grafo se guarda la contidad de feromonas (0<=f<=1) asociadas a la arista
En cada transición cada hormiga elige una ciudad entre las que puede visitar directamente
Esta ciudad tiene que ser una que no haya ya visitado
La elección de la ciudad se basa en dos factores
    alfa: importancia de la feromona acumulada en la arista
    beta: (1-alfa) importancia de la heurística (distancia a la ciudad)
una vez alzanzado el máximo número de saltos:
    Se procede a una evaporación de feromona en las aristas por un factor de gamma
    las hormigas que hubiesen llegado a destino depositan una cantidad de feromona
    finc en su ruta. Esta cantidad es inv. proporcional a la lg de la ruta
"""
import sys
from Grafos_Clases.Grafo import GrafoAvanzado

from matplotlib import pyplot as plt
try:
  import google.colab
  IN_COLAB = True
except:
  IN_COLAB = False

if IN_COLAB:
    # montar el drive, que es donde tenemos el dataset
    from google.colab import drive
    drive.mount("/content/drive")
    data_dir = "/content/drive/MyDrive/2023/Publica/Alumnos/"
    sys.path.append(data_dir)
else:
    import os
    data_dir = os.path.dirname(__file__) + "/Útiles/"

def set_feromonas(grafo,value):
    ciudades=[]
    for nodo in grafo.nodos:
      for arista in grafo.get_node_attributtes(nodo,'edges'):
         grafo.set_edge_atributtes(nodo,arista,feromonas=value)
      ciudades.append(nodo)
    return ciudades

maxiter=1000
maxtrans=100
totalh=50
gamma=0.05
alfa=0.7
beta=1-alfa
fero_min = 1
fero_max = 300
finc = (fero_max - fero_min) * 10

g = GrafoAvanzado()
g.set_edge_atributtes
g.rellenar_data(data_dir+"provincias.json")
ciudades=set_feromonas(g,fero_min)
while iter < maxiter:
   print("a")
plt.show()