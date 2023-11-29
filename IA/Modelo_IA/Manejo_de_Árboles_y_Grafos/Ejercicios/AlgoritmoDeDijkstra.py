"""
    Es un algoritmo para la determinación del camino más corto, dado un vértice origen, hacia el resto de los vértices en un grafo que tiene pesos en cada arista

    SIEMPRE SE QUEDA CON EL MENOR DE LOS CASOS HASTA QUE SLO QUEDE LA OTRA ESQUINA, CALCULA LOS PESOS DE CADA GRAFO
"""

import json
import pprint
import matplotlib.pyplot as plt
import numpy as np
from PersonalizedException import PersonalizedException as pe
from GrafoConProvincias import GrafoConProvincias

import sys
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
    data_dir = os.path.dirname(__file__) + "/"


g = GrafoConProvincias()
try:
    g.rellenar_data(data_dir+"provincias.json")
    g.recorre_grafo(nodo_inicial="A Coruña")
    pprint.pprint(g.nodos)
    g.dibuja()
    g.dibuja_ruta(g.genera_ruta('Barcelona'))
except pe:
    pe.getErrorMessage()
    