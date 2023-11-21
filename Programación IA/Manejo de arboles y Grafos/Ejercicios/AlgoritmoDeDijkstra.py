"""
    Es un algoritmo para la determinación del camino más corto, dado un vértice origen, hacia el resto de los vértices en un grafo que tiene pesos en cada arista

    SIEMPRE SE QUEDA CON EL MENOR DE LOS CASOS HASTA QUE SLO QUEDE LA OTRA ESQUINA, CALCULA LOS PESOS DE CADA GRAFO
"""

import matplotlib.pyplot as plt
import numpy as np
from PersonalizedException import PersonalizedException as pe

class Grafo():
    def __init__(self) -> None:
        self.nodos = {}
        self.abiertos=[]
        self.cerrados=[]
    
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

    def pop_abiertos(self):
        return self.abiertos.pop(0)

      # si el nodo es una solución del problema devuelve TRUE
    def es_solucion(self, nodo_actual):
        if nodo_actual is not(None):
            for v in self.nodos[nodo_actual].get("edges",None):
                print(v)
        return False

  # devuelve una lista con todos los nodos conectados al nodo actual
    def genera_sucesores(self, nodo_actual):
        return self.adj(nodo_actual)

    # devuelve una lista con los hijos, decidiendo que hacer si ya están en abiertos o cerrados
    def procesa_repetidos(self, hijos_iniciales):
      # print(f"procesa_repetidos: {hijos_iniciales}")
      hijos = [h for h in hijos_iniciales if h not in self.abiertos and h not in self.cerrados]
      return hijos
    
    
    def recorrer_grafo_algortimo(self,nodo_inicial=None):

        if nodo_inicial is None: nodo_inicial=list(self.nodos.keys())[0]

        self.abiertos.append(nodo_inicial)

        while len(self.abiertos) > 0: # mientras en abiertos existan nodos
        # quitar un nodo
            actual = self.pop_abiertos()

        # mirar si es una solución
        # si tal break
            if self.es_solucion(actual):
                break

        # actual a cerrado
            self.cerrados.append(actual)

        # generar sucesores
            hijos = self.genera_sucesores(actual)

        # que hacer con los repetidos
            hijos = self.procesa_repetidos(hijos)

            for hijo in hijos:
                self.abiertos.append(hijo)


g = Grafo()
try:
    g.add_node("A", x=1, y=5,peso=0)
    g.add_node("B", x=3, y=6)
    g.add_node("C", x=2, y=0)
    g.add_node("D", x=4, y=2)
    g.add_node("E", x=5, y=7)
    g.add_edge("A", "B", coste=3)
    g.add_edge("A", "C", coste=1)
    g.add_edge("B", "C", coste=7)
    g.add_edge("C", "D", coste=2)
    g.add_edge("B", "D", coste=5)
    g.add_edge("B", "E", coste=1)
    g.add_edge("D", "E", coste=7)
    g.recorrer_grafo_algortimo()
except pe:
    pe.getErrorMessage()
    