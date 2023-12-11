import math
from Grafos.Grafo import GrafoAvanzado

class PuzleN(GrafoAvanzado):
    def __init__(self, np=8):
        GrafoAvanzado.__init__(self)
        self.lado = int(math.sqrt(np+1))
    
    def es_solucion(self, nodo_actual):
    # print(f"Procesando nodo: {nodo_actual}")
        if nodo_actual == "1-2-3-4-5-6-7-8-0": return True
        return False

    def calcula_distanciaDst(self, nodo, nodo_destino):
        ###
        ### ????????? Aquí falta
        return 0







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
