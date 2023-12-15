from Grafos.Grafo import GrafoAvanzado

class GrafoDamas(GrafoAvanzado):

    def __init__(self, n):
        self.poblacion = []
        pass

    # generar nelem individuos al azar
    def genera_nelementos(self, nelem):
      elementos=[]
      for i in range(nelem):
        elementos.append(range(0,2))
      return elementos

    # valora cuantos errores tiene la posición
    # 0 es ningún error, cualquier otro valor es positivo
    def valora_errores_posicion(self, pos):
      nerrores = 0

      return nerrores


#Generar una población inicial
#durante un número máximo de iteraciones:
#  ordenar la poblacion
#  quedarse con los mejores
#  si alguno es solucion acabar
#  cruzar individuos
#  añadir hijos a la población
            