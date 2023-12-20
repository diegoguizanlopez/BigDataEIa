from copy import deepcopy
import random
import time

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
    
    def genero_hijos(self,list):
        lista=[]

        for value in range(int(len(list)/2)):
            result=[]
            valorRandom=random.randint(0,int(len(list)-1))
            porcentajeTope=int((valorRandom*100)/len(list))
            temp1=list[valorRandom]
            temp2=list[random.randint(0,int(porcentajeTope*len(list)/100))]
            value = random.randint(-1,int(len(list[0])))
            newValues=temp2[:value]
            result=temp1[value:int(len(list[0]))]
            for value in newValues:
                valor=value
                if value in result:
                    for valor1Array in (result):
                        if value == valor1Array:
                            for i in range(len(list[0])):
                                if i not in result:
                                    valor=i
                                    break
                result.append(valor)
            lista.append(deepcopy(result))
        return lista
    
    def printar_tablero(self,array):
        total=[]
        for j in array:
            linea=[]
            for indexrot,rotation in enumerate(array):
                linea.append('| - |' if j!=indexrot else '| X |')
            total.append(linea)
        matriz=np.array(total)
        for i in range(len(matriz)):
            for j in matriz[i]:
                print(j, end='')
            print()

    def genero_anhadidos(self):
        lista=[]
        for index in range(128):
            fila=[]
            for i in range(self.nElementos):
                valor = random.randint(0,self.nElementos-1)
                while valor in fila:
                    valor = random.randint(0,self.nElementos-1)
                fila.append(deepcopy(valor))
            lista.append(fila)
        return lista


damas = NDamas(15)
start_time = time.time()
while True:
    listErrores={}
    fin=False
    damas.poblacion+=damas.genero_anhadidos()
    for indexC,array in enumerate(damas.poblacion):
        print(array)
        value = damas.valora_errores_posicion(array)
        listErrores[indexC]=deepcopy(value)
        if value == 0: 
            print("FIN")
            damas.printar_tablero(array)
            fin=True
            print("--- %s SEGUNDOS ---" % (time.time() - start_time))
            break
    if fin:
        break
    lista_ordenada = sorted(listErrores.items(), key=lambda x: x[1])
    v=[damas.poblacion[key] for key,value in lista_ordenada][:(int(128/2)+1)]
    damas.poblacion=damas.genero_hijos(v)+v