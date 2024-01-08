import numpy as np
from Grafos.Grafo import GrafoAvanzado

class CanibalesGrafo(GrafoAvanzado):
    def es_posicion_valida(self,listaCanivales,listaMisioneros,misionero,pbarca,canibal=2):
        if listaCanivales.count(1) > listaMisioneros.count(1) and listaMisioneros.count(1)!=0: return False
        if listaCanivales.count(0) > listaMisioneros.count(0) and listaMisioneros.count(0)!=0: return False
        if misionero != pbarca: return False
        if misionero != canibal: return False
        return True
         
    def genera_sucesores(self, nodo):
      hijos=[]
      for i in range(128):
        s = format(i, "07b")
        if s[0] == nodo[0]: continue
        if s[1:5] == nodo [1:5]: continue
        if s[1:4].count("0") > 0 and s[1:4].count("0") < s[4:].count("0"): continue
        if s[1:7] == nodo[1:7] : continue
        if s[5] != nodo[5] and s[6]!=nodo[6]: continue

        if nodo[1:7].count("1") == s[1:7].count("1"): continue
        if nodo[1:7].count("0") == s[1:7].count("0"): continue
        if nodo[0] == "1" and s[1:7].count("1")>nodo[1:7].count("1"):continue
        if nodo[0] == "0" and s[1:7].count("0")>nodo[1:7].count("0"):continue
        if s[1:4].count("1")<s[4:7].count("1") and s[1:4].count("1")!=0:continue
        if s[1:4].count("0")<s[4:7].count("0") and s[1:4].count("0")!=0:continue
        if self.compare_strings(s[1:7],nodo[1:7])<4: continue
        hijos.append(s)
      return hijos

    def compare_strings(self,a, b):
      if a is None or b is None:
          print("Number of Same Characters: 0")
          return

      size = min(len(a), len(b))  # Finding the minimum length
      count = 0  # A counter to keep track of same characters

      for i in range(size):
          if a[i] == b[i]:
              count += 1  # Updating the counter when characters are same at an index
      return count

    def es_solucion(self, nodo_actual,**kargs):
        return nodo_actual == "1111111"


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