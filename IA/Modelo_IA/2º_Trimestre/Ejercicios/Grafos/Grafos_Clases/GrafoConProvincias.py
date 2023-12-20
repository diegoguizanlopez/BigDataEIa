import math

import numpy as np
from Grafos_Clases.Grafo import GrafoAvanzado

class GrafoConProvincias(GrafoAvanzado):
        
    def calcula_distanciaDst(self, destino, origen):
        return math.sqrt((self.get_node_attributtes(origen,"x",0)-self.get_node_attributtes(destino,"x",0))**2
                       +(self.get_node_attributtes(origen,"y",0)-self.get_node_attributtes(destino,"y",0))**2)*111
    
    def proximo(self,final,numeros):
        def el_menor(numeros):
         menor = numeros[0]
         retorno = 0
         for x in range(len(numeros)):
          if numeros[x]<menor:
           menor = numeros[x]
           retorno = x
         return retorno

        diferencia = []
        for x in range(len(numeros)):
         diferencia.append(abs(final - numeros[x]))
        return numeros[el_menor(diferencia)]
    
    def genera_ruta(self, inicial, puntero="antecesor"):
        """
        Este genera ruta funciona de manera que si tiene un tope máximo y no llego a esa ruta pueda llegar al punto más cercano que encontró por coordenadas
        :param inicial nodo: Nodo inicial
        :param puntero str: lo que se va buscar
        """
        listasucesos=[]
        nodo = inicial
        while nodo is not None and nodo not in listasucesos:
            listasucesos.append(nodo)
            nodo=self.get_node_attributtes(nodo,puntero)
        if len(listasucesos)==1:
            nodoFinal=listasucesos[0]
            listaNodosNum=[]
            listaNodosNom=[]
            for hijos in self.nodos:
              if(self.get_node_attributtes(hijos,puntero,None) is not(None) and self.nvMax>=self.get_node_attributtes(hijos,"nivel",np.inf)):
                listaNodosNom.append(hijos)
                listaNodosNum.append(self.calcula_distanciaDst(nodoFinal,hijos))
            listasucesos=self.genera_ruta(listaNodosNom[listaNodosNum.index(min(listaNodosNum))])
        return listasucesos