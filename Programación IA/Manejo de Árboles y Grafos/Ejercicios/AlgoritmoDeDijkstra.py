"""
    Es un algoritmo para la determinación del camino más corto, dado un vértice origen, hacia el resto de los vértices en un grafo que tiene pesos en cada arista

    SIEMPRE SE QUEDA CON EL MENOR DE LOS CASOS HASTA QUE SLO QUEDE LA OTRA ESQUINA, CALCULA LOS PESOS DE CADA GRAFO
"""

import pprint
import matplotlib.pyplot as plt
import numpy as np
from PersonalizedException import PersonalizedException as pe

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




    def pop_abiertos(self):
        values = {}
        for x in self.abiertos:
            values[x] = self.get_node_attributtes(x,"peso",np.inf)
        return self.abiertos.pop(self.abiertos.index(min(values)))

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
    
    
    def recorre_grafo(self, nodo_inicial = None):

        # si no se proporciona inicial escojo el primero que se creó
        if nodo_inicial is None: nodo_inicial = list(self.nodos.keys())[0]

        # poner en todos los nodos un atributo distanciaOrg = inf
        # excepto en el inicial que es 0

        # metemos en abiertos el nodo inicial
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

    def procesamiento_peso(self,nodo_actual):
        if nodo_actual is not(None):
            for nodo_conectado in self.nodos[nodo_actual].get("edges",None):
                if nodo_conectado not in self.nodosVistos:
                    if self.get_node_attributtes(nodo_conectado,"peso",np.inf)  > self.get_node_attributtes(nodo_actual,"peso",0) + self.get_edge_atributtes(nodo_conectado,nodo_actual,"coste",0):
                        self.set_node_atributtes(nodo_conectado,peso=self.get_node_attributtes(nodo_actual,"peso",0) + self.get_edge_atributtes(nodo_conectado,nodo_actual,"coste",0)) 


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
    g.recorre_grafo()
    pprint.pprint(g.nodos)
except pe:
    pe.getErrorMessage()
    