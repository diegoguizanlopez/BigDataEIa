from copy import deepcopy
import random

import numpy as np


class NDamas():
    def __init__(self, n):
        self.nElementos = n
        self.poblacion = []
        self.solucion = []
        pass

    def genera_nelementos(self):
        elementos=[]
        for index in range(128):
            fila=[]
            for i in range(self.nElementos):
                valor = random.randint(0,self.nElementos-1)
                while valor in fila:
                    valor = random.randint(0,self.nElementos-1)
                fila.append(deepcopy(valor))
            elementos.append(fila)
        return elementos
    
    def es_solucion(self):
        for value in self.poblacion:
            return self.valora_errores_posicion(value)==0
        return False

    def valora_errores_posicion(self,array):
        errorHijo=0
        print(array)
        total=[]
        for j in array:
            linea=[]
            for indexrot,rotation in enumerate(array):
                linea.append(0 if j!=indexrot else 1)
            total.append(linea)

        matriz=np.array(total)

        for i in range(-matriz.shape[0] + 1, matriz.shape[1]):
          errorHijo+=self.countV(list(matriz.diagonal(i)))

        for i in range(-np.fliplr(matriz).shape[0] + 1, np.fliplr(matriz).shape[1]):
          errorHijo += self.countV(list(np.fliplr(matriz).diagonal(i)))
        if errorHijo==0:
            self.solucion=array
            return 0
        return errorHijo
    

    def countV(self,pos):
        if pos.count(1)>1 : 
            return pos.count(1)
        return 0
    
    def genero_hijos(self):
        for value in range(int(len(self.poblacion)/2)):
            result=[]
            temp1=self.poblacion[2*value]
            temp2=self.poblacion[2*value+1]
            
            #result+=temp1[:int(len(self.poblacion[0])/2)]
            #result+=temp2[int(len(self.poblacion[0])/2):int(len(self.poblacion[0]))]
            self.poblacion.append(result)
        return self.poblacion

damas = NDamas(5)
elementos=damas.genera_nelementos()
damas.poblacion=elementos
while damas.es_solucion() == False:
    listErrores={}
    for indexC,array in enumerate(damas.poblacion):
        listErrores[indexC]=deepcopy(damas.valora_errores_posicion(array))
    min_values = sorted(listErrores.values())
    min_keys = [key for key, value in listErrores.items() if value in min_values]
    v=[damas.poblacion[x] for x in min_keys][:int(len(min_keys)/2)]
    damas.poblacion = damas.genero_hijos()