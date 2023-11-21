#AHORCADO Con una lista de palabras
import random as rnd
import re

def ejercicio_1_ahorcado():
    monigoteMap = mapa_monigote()
    palabras_brutas="Un volcán es una formación geológica con forma de montaña y una abertura en su cima, llamada chimenea. Los volcanes provocan erupciones, es decir, emisiones de lava, gases y cenizas procedentes del núcleo de la Tierra. Un volcán se genera a partir de las roturas en la corteza terrestre por las que sale el magma, roca fundida procedente del interior de la tierra. El material que se acumula con cada erupción es el que da forma de montaña al volcán"
    palabras_brutas = re.sub('[^A-Za-z0-9 \'áéíóúñ]+', '', palabras_brutas)
    listado_de_palabras = [palabras.upper() for palabras in palabras_brutas.split(" ") if len(palabras)>5]
    palabraSeleccionada = rnd.choice(listado_de_palabras)
    tablero=["-" for x in palabraSeleccionada]
    palabraArray = [letra for letra in palabraSeleccionada]
    jugar(tablero,palabraArray,monigoteMap)


def jugar(tablero,palabraArray,mapMonigote):
    intentos = 7
    letrasDichas = set()
    while intentos != 0:
        printar_set(tablero," ")
        value = input("Dime una letra\n").upper()
        if(value not in letrasDichas and value.__len__()==1):
            letrasDichas.add(value)
            counter = 0
            algunAcierto = False
            for v2 in palabraArray:
                if(v2==value):
                    tablero[palabraArray.index(v2,counter)]=v2
                    algunAcierto = True
                counter+=1
            if (not(algunAcierto)):
                intentos-=1
            if(tablero.count("-")==0):
                print("GANÓ")
                printar_set(tablero," ")
                break
        print(mapMonigote[intentos])
        print(f"Le quedan {intentos}\nLetras dichas:")
        printar_set(letrasDichas,", ")
    if(intentos == 0 ):
        print(f"La respuesta era: ")
        printar_set(palabraArray,"")

def printar_set(Tablero,Separator):
    for x in Tablero:
        print(f"{x}{Separator}",end=" ",flush=True)
    print("")


def mapa_monigote():
    return {
        0: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / \\
               |
           """,
        1: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / 
               |
            """,
        2: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |          
               |
            """,
        3: """
                ___________
               | /        | 
               |/        ( )
               |          
               |          
               |
            """,
        4: """
                ___________
               | /        | 
               |/        
               |          
               |          
               |
            """,
        5: """
                ___________
               | /        
               |/        
               |          
               |          
               |
            """,
        6: """
               |
               |
               |
               |
               |
            """,
        7: "",}

ejercicio_1_ahorcado()