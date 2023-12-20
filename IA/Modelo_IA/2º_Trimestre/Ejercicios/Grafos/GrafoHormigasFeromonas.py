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
import random
import sys

import numpy as np
from Grafos_Clases.GrafoConProvincias import GrafoConProvincias

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

class Hormigas():
    def __init__(self,posicioninicial) -> None:
      self.posicion_inicial=posicioninicial
      self.posicion_actual=posicioninicial
      self.visitas=[]

maxiter=1000
maxtrans=100
totalh=50
gamma=0.05
alfa=0.7
beta=1-alfa
fero_min = 1
fero_max = 300
finc = (fero_max - fero_min) * 10

g = GrafoConProvincias()
g.set_edge_atributtes
g.rellenar_data(data_dir+"provincias.json")
g.dibuja()
ciudades=set_feromonas(g,fero_min)
iteract=0
trans=0
lHormigas=[]

for i in range(300):
  lHormigas.append(Hormigas(random.choice(list(g.nodos))))

while iteract < maxiter:
    while trans < maxtrans:
      for hormiga in lHormigas:
         if(hormiga.posicion_actual!="A Coruña"):
            distanciaMin=np.inf
            feromonas=0
            localizacionCercanaW=''
            localizacionCercanaF=''
            lFeromonas=[]
            hormiga_end=False
            for adyacente in g.get_node_attributtes(hormiga.posicion_actual,'edges'):
              weight=g.get_edge_atributtes(hormiga.posicion_actual,adyacente,'weight')
              fero=g.get_edge_atributtes(hormiga.posicion_actual,adyacente,'feromonas')
              if weight<distanciaMin:
                distanciaMin=weight
                localizacionCercanaW=adyacente
              if feromonas == fero:
                 lFeromonas.append(adyacente)
              if feromonas<fero:
                 feromonas=fero
                 localizacionCercanaF=adyacente
                 lFeromonas.clear()
            if len(lFeromonas)==0:
               g.set_edge_atributtes(hormiga.posicion_actual,localizacionCercanaF,feromonas=g.get_edge_atributtes(hormiga.posicion_actual,localizacionCercanaF,'feromonas')+1)
               hormiga.posicion_actual=localizacionCercanaF
               hormiga.visitas.append(localizacionCercanaF)
               print(int(g.get_edge_atributtes(hormiga.posicion_actual,localizacionCercanaF,'feromonas')+1))
            else:
               g.set_edge_atributtes(hormiga.posicion_actual,localizacionCercanaW,feromonas=g.get_edge_atributtes(hormiga.posicion_actual,localizacionCercanaF,'feromonas')+1)
               hormiga.posicion_actual=localizacionCercanaW
               hormiga.visitas.append(localizacionCercanaW)
               print(int(g.get_edge_atributtes(hormiga.posicion_actual,localizacionCercanaW,'feromonas'))+1)
      trans+=1
    iteract+=1
plt.show()