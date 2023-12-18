from copy import deepcopy
import random
import numpy as np
from Grafos.Grafo import GrafoAvanzado
import pprint

class GrafoDamas(GrafoAvanzado):

    def __init__(self, n):
        GrafoAvanzado.__init__(self)
        self.nElementos = n
        self.poblacion = [[0 for i in range(self.nElementos)] for i in range(self.nElementos)]
        pass

    # generar nelem individuos al azar
    def genera_nelementos(self):
       return []

    # valora cuantos errores tiene la posición
    # 0 es ningún error, cualquier otro valor es positivo
    def valora_errores_posicion(self,pos):
      if pos.count(1)>1 : 
         return pos.count(1)
      return 0
    
    def genera_sucesores(self, nodo_actual):
      nodo_actual=nodo_actual.replace('[','')
      nodo_actual=nodo_actual.split(']')
      nodo_actual.pop(-1)
      value=deepcopy(nodo_actual)
      for index,row in enumerate(value):
         nodo_actual[index]=[int(x) for x in (row.replace(' ','')).split(",")]
      value=deepcopy(nodo_actual)
      listValues=[]
      if len(value)>0:
        for i in range(self.nElementos):
          for j in range(self.nElementos):
            x = random.randint(0,self.nElementos-1)
            y = random.randint(0,self.nElementos-1)
            value[x][y] = 1
            listValues.append(deepcopy(value))
            value[x][y] = 0
      return (':'.join(str(v) for v in listValues).replace("]]","]").replace("[[","[").replace("], ","]").split(":"))


    def es_solucion(self, nodo_actual, **kargs):
      nodo_actual=nodo_actual.replace('[','')
      nodo_actual=nodo_actual.split(']')
      nodo_actual.pop(-1)
      value=deepcopy(nodo_actual)
      errorLinea=0
      for index,row in enumerate(value):
        nodo_actual[index]=[int(x) for x in (row.replace(' ','')).split(",")]
        errorLinea+=self.valora_errores_posicion(nodo_actual[index])
        if(nodo_actual.count(1)==0):
          errorLinea+=1
      if(errorLinea==0):
        return True
      return False

    def procesa_peor_posiciones(self,hijos):
      listErrores={}
      for index,hijo in enumerate(hijos):
        errorHijo=0
        hijo=hijo.replace('[','')
        hijo=hijo.split(']')
        hijo.pop(-1)
        value=deepcopy(hijo)
        for indexC,row in enumerate(value):
           hijo[indexC]=[int(x) for x in (row.replace(' ','')).split(",")]

        #HORIZONTAL
        for horizontal in hijo:
          errorHijo+=self.valora_errores_posicion(horizontal)

        #VERTICAL
        #for Ivertical in range(self.nElementos):
        #  valuesVERTICAL=[]
        #  for Ihorizontal in range(self.nElementos):
        #    valuesVERTICAL.append(hijo[Ivertical][Ihorizontal])
        #  errorHijo+=self.valora_errores_posicion(valuesVERTICAL)
        #listErrores[index]=deepcopy(errorHijo)

        #CRUZ
        #matrix = np.array(
        #         hijo)
        #diags = [matrix[::-1,:].diagonal(i) for i in range(-3,4)]
        #diags.extend(matrix.diagonal(i) for i in range(3,-4,-1))
        #for n in diags:
        #  errorHijo+=self.valora_errores_posicion(n.tolist())
        listErrores[index]=deepcopy(errorHijo)
      min_values = sorted(listErrores.values())[:len(hijos)]
      min_keys = [key for key, value in listErrores.items() if value in min_values]
      print(min_values)
      return [hijos[x] for x in min_keys][:len(hijos)]
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
        if self.es_solucion(nodo_actual=actual):
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
          #self.valora_errores_posicion()
        # calcular la distancia a destino de cada hijo y anotarla en él
          if nodo_destino:
            d_destino = self.calcula_distanciaDst(hijo, nodo_destino)
            # actualizar en hijo esta distancia
            self.set_node_atributtes(hijo, distanciaDst=d_destino)
        # que hacer con los repetidos
        hijos = self.procesa_repetidos(hijos)

        hijos = self.procesa_peor_posiciones(hijos)
        # insertar los hijos en abiertos
        for hijo in hijos:
          self.abiertos.append(hijo)