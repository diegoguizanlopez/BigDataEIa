import math

import numpy as np
from Grafos.Grafo import GrafoAvanzado

class PuzleN(GrafoAvanzado):
    def __init__(self, np=8):
        GrafoAvanzado.__init__(self)
        self.lado = int(math.sqrt(np+1))
    
    def es_solucion(self, nodo_actual,nodoDestino,nivel_max=np.inf):
        print(f"Procesando nodo: {nodo_actual}")
        if nodo_actual == nodoDestino: return True
        return False

    def calcula_distanciaDst(self, nodo, nodo_destino):
        nodoInicial=nodo.split("-")
        nodoFinal=nodo_destino.split("-")
        listaDistancias=[]
        for indexInicial,inicial in enumerate(nodoInicial):
           for index,final in enumerate(nodoFinal):
              if(inicial == final):
                 listaDistancias.append(0 if indexInicial==index else (int(inicial)-index))
        return sum(list(map(lambda x:x**2,listaDistancias)))
        







    # devuelve una lista de nodos hijo
    def genera_sucesores(self, nodo):
      hijos = []

 #     print(f"genero sucesores de {nodo}")
      # convertir la cadena en una lista
      l = nodo.split("-")
      ind = l.index("0")
      fila = ind // self.lado;  columna = ind % self.lado
      incs = [(-1,0), (1,0), (0,-1), (0,1)]
      for inc in incs:
         f = fila + inc[0]; c = columna + inc[1]
         if f >= 0 and f < self.lado and c >= 0 and c < self.lado:
            #intercambiar
            l[ind] = l[f*self.lado + c];   l[f*self.lado + c] = "0"
            s = "-".join(l)
            hijos.append(s)
            # dejar todo como estaba
            l[f*self.lado + c] = l[ind];   l[ind] = "0"
      return hijos

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
