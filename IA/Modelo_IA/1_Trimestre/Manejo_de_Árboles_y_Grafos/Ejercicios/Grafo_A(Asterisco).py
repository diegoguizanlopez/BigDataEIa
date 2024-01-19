"""
    FUSIÓN DE LOS MÉTODOS DE DIJKSTRA Y AVARICIOSO QUE PERMITE PONER UN NIVEL DE BÚSQUEDA MÁXIMO
"""

import datetime
import json
import math
from pathlib import Path
import pprint
import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from Grafos.Grafo import Grafo
from Grafos.GrafoConProvincias import GrafoConProvincias

import sys
path = str(Path(__file__).parent.parent.parent.parent.absolute())      #MANEJO DE CLASES Y MÉTODOS LLAMADOS ATRÁS
sys.path.insert(0, path)
from Clases.PersonalizedException import PersonalizedException as pe




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
    g.recorre_grafo(nodo_inicial="A Coruña",modo='A*',nodo_destino="León",dijkstra=0,avaricioso=1,nivel_max=5)
    g.dibuja()
    pprint.pprint(g.nodos)
    g.dibuja_ruta(g.genera_ruta('Almería'))
except pe as p:
    pe.getErrorMessage()
except Exception as e:
    print(e)