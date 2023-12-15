import numpy as np
from Grafos.Grafo import GrafoAvanzado
import pprint

class GrafoDamas(GrafoAvanzado):

    def __init__(self, n):
        self.nElementos = n
        self.poblacion = []
        pass

    # generar nelem individuos al azar
    def genera_nelementos(self):
       return [[0 for i in range(self.nElementos)] for i in range(self.nElementos)]

    # valora cuantos errores tiene la posición
    # 0 es ningún error, cualquier otro valor es positivo
    def valora_errores_posicion(self, pos):
        return pos.count(1)


#Generar una población inicial
#durante un número máximo de iteraciones:
#  ordenar la poblacion
#  quedarse con los mejores
#  si alguno es solucion acabar
#  cruzar individuos
#  añadir hijos a la población
            
def recorre_grafo(self, nodo_inicial = None,nodo_destino=None,modo='A*',**kargs):   

        # si no se proporciona inicial escojo el primero que se creó
    if nodo_inicial is None: nodo_inicial = list(self.nodos.keys())[0]
    if nodo_inicial not in self.nodos:
        self.add_node(nodo_inicial, distanciaOrg = 0,  distanciaDst = np.inf)

    # poner en todos los nodos un atributo distanciaOrg = inf
    # excepto en el inicial que es 0
    for n in self.nodos:
      self.set_node_atributtes(n, distanciaOrg=np.inf)
      self.set_node_atributtes(n, antecesor=None)
    self.set_node_atributtes(nodo_inicial, distanciaOrg=0)
     #%%%% poner en nodo_inicial distancia a destino
     # metemos en abiertos el nodo inicial
    self.abiertos.append(nodo_inicial)
    while len(self.abiertos) > 0: # mientras en abiertos existan nodos
      # quitar un nodo
      actual = self.pop_abiertos(modo,avaricioso=kargs.get("avaricioso",0.5),dijkstra=kargs.get("djkistra",0.5))
      # mirar si es una solución
      # si tal CAMBIAMOS A RETURN
      if self.es_solucion(actual,nodo_destino):
        return actual
      # actual a cerrado
      self.cerrados.append(actual)
      # generar sucesores
      hijos = self.genera_sucesores(actual)
      # para cada hijo,
      # Si (distanciaOrg de actual + coste hacia el hijo )   <    distanciaOrg del hijo
      #       distanciaOrg del hijo = (distanciaOrg de actual + coste hacia el hijo )
      d_actual = self.get_node_attributtes(actual, "distanciaOrg", 0)
      for hijo in hijos:
        if hijo not in self.nodos:
            self.add_node(hijo, distanciaOrg = d_actual+1,  distanciaDst = np.inf)
            self.set_node_atributtes(hijo, antecesor=actual)
        self.add_edge(actual, hijo, weight=1)
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
      # que hacer con los repetidos
      hijos = self.procesa_repetidos(hijos)
      # insertar los hijos en abiertos
      for hijo in hijos:
        self.abiertos.append(hijo)