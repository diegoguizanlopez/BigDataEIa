import numpy as np
from Grafos.Grafo import GrafoAvanzado

class CanibalesGrafo(GrafoAvanzado):
    def es_posicion_valida(self,listaCanivales,listaMisioneros,barca,movimiento):
        if listaCanivales.count(1) > listaMisioneros.count(1): return False
        if listaCanivales.count(0) > listaMisioneros.count(0): return False
        if barca == movimiento: return False
        return True
  
    def check_canibales(self,listaCanivales,listaMisioneros,hijos,pbarca,cCRema=False):
        listaCanivales[0] = 1-listaCanivales[0]
        if self.es_posicion_valida(listaCanivales,listaMisioneros,pbarca):
          hijos.append(f"{listaCanivales[0]}{listaCanivales[1]}{listaCanivales[2]}{listaMisioneros[0]}{listaMisioneros[1]}{listaMisioneros[2]}{pbarca}")
        listaCanivales[0] = 1-listaCanivales[0]

        listaCanivales[1] = 1-listaCanivales[1]
        if self.es_posicion_valida(listaCanivales,listaMisioneros,pbarca):
          hijos.append(f"{listaCanivales[0]}{listaCanivales[1]}{listaCanivales[2]}{listaMisioneros[0]}{listaMisioneros[1]}{listaMisioneros[2]}{pbarca}")
        listaCanivales[1] = 1-listaCanivales[1]

        listaCanivales[2] = 1-listaCanivales[2]
        if self.es_posicion_valida(listaCanivales,listaMisioneros,pbarca) and not(cCRema):
          hijos.append(f"{listaCanivales[0]}{listaCanivales[1]}{listaCanivales[2]}{listaMisioneros[0]}{listaMisioneros[1]}{listaMisioneros[2]}{pbarca}")
        listaCanivales[2] = 1-listaCanivales[2]
        
    
    def genera_sucesores(self, nodo):
        hijos = []
        listaMisioneros = [(int)(nodo[0]),(int)(nodo[1]),(int)(nodo[2])]
        listaCanivales = [(int)(nodo[3]),(int)(nodo[4]),(int)(nodo[5])]
        posicionBarca = (int)(nodo[6])
        
        listaMisioneros[0] = 1-listaMisioneros[0]
        posicionBarca=1-posicionBarca
        if self.es_posicion_valida(listaCanivales,listaMisioneros,posicionBarca):
          hijos.append(f"{listaCanivales[0]}{listaCanivales[1]}{listaCanivales[2]}{listaMisioneros[0]}{listaMisioneros[1]}{listaMisioneros[2]}{posicionBarca}")

        self.check_canibales(listaCanivales,listaMisioneros,hijos,posicionBarca)
        listaMisioneros[0] = 1-listaMisioneros[0]
        posicionBarca=1-posicionBarca

        listaMisioneros[1] = 1-listaMisioneros[1]
        posicionBarca=1-posicionBarca
        if self.es_posicion_valida(listaCanivales,listaMisioneros,posicionBarca):
          hijos.append(f"{listaCanivales[0]}{listaCanivales[1]}{listaCanivales[2]}{listaMisioneros[0]}{listaMisioneros[1]}{listaMisioneros[2]}{posicionBarca}")
        self.check_canibales(listaCanivales,listaMisioneros,hijos,posicionBarca)
        listaMisioneros[1] = 1-listaMisioneros[1]
        posicionBarca=1-posicionBarca


        listaMisioneros[2] = 1-listaMisioneros[2]
        posicionBarca=1-posicionBarca
        if self.es_posicion_valida(listaCanivales,listaMisioneros,posicionBarca):
          hijos.append(f"{listaCanivales[0]}{listaCanivales[1]}{listaCanivales[2]}{listaMisioneros[0]}{listaMisioneros[1]}{listaMisioneros[2]}{posicionBarca}")
        self.check_canibales(listaCanivales,listaMisioneros,hijos,posicionBarca)
        listaMisioneros[2] = 1-listaMisioneros[2]
        posicionBarca=1-posicionBarca
        

        listaCanivales[2] = 1-listaCanivales[2]
        posicionBarca=1-posicionBarca
        if self.es_posicion_valida(listaCanivales,listaMisioneros,posicionBarca,1 if listaCanivales[2]==0 else 0):
          hijos.append(f"{listaCanivales[0]}{listaCanivales[1]}{listaCanivales[2]}{listaMisioneros[0]}{listaMisioneros[1]}{listaMisioneros[2]}{posicionBarca}")
        self.check_canibales(listaCanivales,listaMisioneros,hijos,posicionBarca)
        listaCanivales[2] = 1-listaCanivales[2]
        posicionBarca=1-posicionBarca


        return hijos
  
    def es_solucion(self, nodo_actual,**kargs):
        return nodo_actual == "111111"


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