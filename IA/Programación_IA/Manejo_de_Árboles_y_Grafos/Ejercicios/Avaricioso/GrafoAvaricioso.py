"""
    Es un algoritmo para la determinación del camino más corto, dado un vértice origen, hacia el resto de los vértices en un grafo que tiene pesos en cada arista

    SIEMPRE SE QUEDA CON EL MENOR DE LOS CASOS HASTA QUE SLO QUEDE LA OTRA ESQUINA, CALCULA LOS PESOS DE CADA GRAFO
"""

import json
import math
import pprint
import matplotlib.pyplot as plt
import numpy as np

import sys

import PersonalizedException as pe

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


class Grafo():
    def __init__(self) -> None:
        self.nodos = {}
        self.abiertos=[]
        self.cerrados=[]
        self.nodosVistos={}
    
    def add_node(self,nodo,**kargs) -> None:
        if nodo in self.nodos: raise pe("YA EXISTE EL NODO")
        self.nodos[nodo] = {"edges":{}}
        for k,v in kargs.items(): self.nodos[nodo][k]=v
            
    def remove_node(self,nodo) -> None:
        if nodo not in self.nodos: raise pe("NO SE ENCONTRÓ EL NODO A BORRAR")
        for n in self.nodos[nodo]["edges"]:
            self.nodos[n]["edges"].pop(nodo)
        self.nodos.pop(nodo)

    def add_edge(self,nodo1,nodo2,**kargs) -> None :
        if nodo1 not in self.nodos or nodo2 not in self.nodos: raise pe("ERROR UNO DE LOS BORDES NO ENCONTRADOS")
        self.nodos[nodo1]["edges"][nodo2]=kargs
        self.nodos[nodo2]["edges"][nodo1]=kargs

    def remove_edge(self,nodo1,nodo2):
        if nodo1 not in self.nodos or nodo2 not in self.nodos: raise pe("BORDE NO ENCONTRADO")
        self.nodos[nodo1]["edges"].pop(nodo2, None)
        self.nodos[nodo2]["edges"].pop(nodo1, None)

    def set_node_atributtes(self,nodo,**kargs):
        for k,v in kargs.items():
            self.nodos[nodo][k]=v

    def get_node_attributtes(self,nodo,attributte,default=None):
        return self.nodos[nodo].get(attributte,default)
    
    def set_edge_atributtes(self,nodo1,nodo2,**kargs):
        for k,v in kargs.items():
            self.nodos[nodo1]["edges"][nodo2][k]=v

    def get_edge_atributtes(self,nodo1,nodo2,attributte,default=None):
        return self.nodos[nodo1]["edges"][nodo2].get(attributte,default)
    
    def adj(self, nodo):
        adyacentes = [n for n in self.nodos[nodo]["edges"]]
        return adyacentes
    
    def dibuja(self):
        fig, ax = plt.subplots(figsize=[20,20])
        # para cada nodo, dibuja un circulo en la posicion Xn, Yn
        for n in self.nodos:
          Xn = self.get_node_attributtes(n, "x", 0)
          Yn = self.get_node_attributtes(n, "y", 0)
          ax.scatter(Xn, Yn, s=300)
          ax.text(Xn,Yn, n)
          # para cada arista
          for arista in self.nodos[n]["edges"]:
            # mira la posicion del nodo destino Xd, Yd
            Xd = self.get_node_attributtes(arista, "x", 0)
            Yd = self.get_node_attributtes(arista, "y", 0)
            ax.plot([Xn, Xd], [Yn, Yd], color="b", linewidth=0.5)
            # Escribe el coste en la mitad de camino entre los dos nodos
            ax.text((Xn+Xd)/2, (Yn+Yd)/2, self.get_edge_atributtes(n, arista, "weight", 0), alpha=0.5)




    def pop_abiertos(self,modo="djkstra"):
        ret = None
        if modo == "profundidad":
          ret = self.abiertos.pop()
        elif modo == "anchura":
          ret = self.abiertos.pop(0)
        elif modo == "djkstra":
            values = {}
            for x in self.abiertos:
                values[x] = self.get_node_attributtes(x,"peso",np.inf)
            ret = self.abiertos.pop(self.abiertos.index(min(values)))
        elif modo == "avaricioso":
            # escoger de todos los de abiertos el que tenga menor
            # valor de distanciaDst %%%%%
            listaV={}
            for x in self.abiertos:
                listaV[x] = self.get_node_attributtes(x,"distanciaDst",np.inf)
            ret = self.abiertos.pop(self.abiertos.index(min(listaV)))
        return ret

      # si el nodo es una solución del problema devuelve TRUE
    def es_solucion(self, nodo_actual):
        print(f"Procesando nodo: {nodo_actual}")
        return False

  # devuelve una lista con todos los nodos conectados al nodo actual
    def genera_sucesores(self, nodo_actual):
        return self.adj(nodo_actual)

    # devuelve una lista con los hijos, decidiendo que hacer si ya están en abiertos o cerrados
    def procesa_repetidos(self, hijos_iniciales):
      # print(f"procesa_repetidos: {hijos_iniciales}")
      hijos = [h for h in hijos_iniciales if h not in self.abiertos and h not in self.cerrados]
      return hijos
    
    
    def recorre_grafo(self, nodo_inicial = None,nodo_destino=None,modo='djkstra'):

        # si no se proporciona inicial escojo el primero que se creó
        if nodo_inicial is None: nodo_inicial = list(self.nodos.keys())[0]

        # poner en todos los nodos un atributo distanciaOrg = inf
        # excepto en el inicial que es 0

        # metemos en abiertos el nodo inicial
        self.abiertos.append(nodo_inicial)

        while len(self.abiertos) > 0: # mientras en abiertos existan nodos
            # quitar un nodo
            actual = self.pop_abiertos(modo)
            # mirar si es una solución
            # si tal break
            if self.es_solucion(actual):
                break

            # actual a cerrado
            self.cerrados.append(actual)

            # generar sucesores
            hijos = self.genera_sucesores(actual)

            # para cada hijo,
            # Si (distanciaOrg de actual + coste hacia el hijo )   <    distanciaOrg del hijo
            #       distanciaOrg del hijo = (distanciaOrg de actual + coste hacia el hijo )
            d_actual = self.get_node_attributtes(actual, "distanciaOrg", 0)
            for hijo in hijos:
              c_hijo = self.get_edge_atributtes(actual, hijo, "weight", 0)
              d_hijo = self.get_node_attributtes(hijo, "distanciaOrg", 0)
              if (c_hijo + d_actual) < d_hijo:
                self.set_node_atributtes(hijo, distanciaOrg=(c_hijo+d_actual))
                self.set_node_atributtes(hijo, antecesor=actual)
            # calcular la distancia a destino de cada hijo y anotarla en él
              if nodo_destino:
                d_destino = self.calcula_distanciaDst(hijo, nodo_destino)
                # actualizar en hijo esta distancia
                self.set_node_atributtes(hijo, distanciaDst=d_destino)

            # si estamos en modo dijkstra
            # para cada hijo,
            # Si (distanciaOrg de actual + coste hacia el hijo )   <    distanciaOrg del hijo
            #       distanciaOrg del hijo = (distanciaOrg de actual + coste hacia el hijo )
            self.procesamiento_peso(actual)
            # que hacer con los repetidos
            hijos = self.procesa_repetidos(hijos)


            # insertar los hijos en abiertos
            for hijo in hijos:
              self.abiertos.append(hijo)

    def genera_ruta(self, inicial, puntero="antecesor"):
        listasucesos=[]
        nodo = inicial
        while nodo is not None and nodo not in listasucesos:
            listasucesos.append(nodo)
            nodo=self.get_node_attributtes(nodo,puntero)
        return listasucesos

    def dibuja_ruta(self,ruta):
        for i, n in enumerate(ruta):
            if i == 0: continue
            x1 = self.get_node_attributtes(ruta[i-1], "x")
            y1 = self.get_node_attributtes(ruta[i-1], "y")
            x2 = self.get_node_attributtes(ruta[i], "x")
            y2 = self.get_node_attributtes(ruta[i], "y")
            plt.plot([x1, x2], [y1, y2], color="k", linewidth=3)
        plt.show()
 

    def rellenar_data(self,jsonFile):
      with open(jsonFile) as line:
        data = json.load(line)
      self.nodos=data

    def procesamiento_peso(self,nodo_actual):
        if nodo_actual is not(None):
            for nodo_conectado in self.nodos[nodo_actual].get("edges",None):
                if nodo_conectado not in self.nodosVistos:
                    if self.get_node_attributtes(nodo_conectado,"peso",np.inf)  > self.get_node_attributtes(nodo_actual,"peso",0) + self.get_edge_atributtes(nodo_conectado,nodo_actual,"weight",0):
                        self.set_node_atributtes(nodo_conectado,peso=self.get_node_attributtes(nodo_actual,"peso",0) + self.get_edge_atributtes(nodo_conectado,nodo_actual,"weight",0)) 
                        self.set_node_atributtes(nodo_conectado, antecesor=nodo_actual)

    def calcula_distanciaDst(self, destino, origen):
      return math.sqrt((self.get_node_attributtes(origen,"x",0)-self.get_node_attributtes(destino,"x",0))**2
                       +(self.get_node_attributtes(origen,"y",0)-self.get_node_attributtes(destino,"y",0))**2)



g = Grafo()
try:
    g.rellenar_data(data_dir+"provincias.json")
    g.recorre_grafo(nodo_inicial="A Coruña",modo='avaricioso',nodo_destino="Lugo")
    pprint.pprint(g.nodos)
    g.dibuja()
    g.dibuja_ruta(g.genera_ruta('Barcelona'))
except pe:
    pe.getErrorMessage()
    