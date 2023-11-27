import random as rnd

#El ordenador genera un número aleatorio del 1-100 y que la persona adivine el número
def Ejercicio1():
    value = rnd.randint(1,100)
    actualValue=0
    while value != actualValue:
        try:
            actualValue = int(input("Dime un valor:\n"))    #Castea el valor a int
            print("ACERTASTE" if actualValue == value else ("Mayor" if actualValue<value else "Menor")) #Ternaria que checkea valores para saber si se acertó
        except:
            print("Formato no valido")


#Tu piensas en un número y la computadora piensa en el número y le dices mayor o menor para que se acerque
def Ejercicio2():
    oldMin,oldMay = 1,100
    value = rnd.randint(oldMin,oldMay)
    while True:
        try:
            trueValue=input(f"Tu número es el : {value} ?  = / > / <\n")
            if(trueValue=="="):
                break
            elif(trueValue==">"):
                oldMin=value+1
            elif(trueValue=="<"):
                oldMay=value-1
            else:                
                raise Exception("Resultado no valido")
            value = rnd.randint(oldMin,oldMay)
        except Exception as e:
            print(e)


#Piedra, papel, tijera EJERCICIO
def Ejercicio3():
    listaValores = ["Pi","Pa","Ti"]
    rondasParaGanar,J1,J2=3,0,0
    while(J1!=rondasParaGanar and J2!=rondasParaGanar):
        try:
            valueMaquina=rnd.choice(listaValores)
            valuePlayer=input("Que has elegido? Pi/Pa/Ti\n").capitalize()
            resultado=CheckResultado(valuePlayer,valueMaquina)
            if(valueMaquina==valuePlayer):
                print("IGUALES")
            elif(resultado):
                print("GANASTE")
                J1+=1
            elif(resultado==False):
                print("GANE YO")
                J2+=1
        except Exception as e:
            print(e.args)
        print(f"{J1} - {J2}")
    print("FIN DE JUEGO")

def Ganador(boleano,v1,v2,J1,J2):
    if(boleano):
        if(J2 == v1):
            return False
        elif(J2 == v2):
            return True
    else:
        if(J1 == v1):
            return True
        elif(J1 == v2):
            return False


def CheckResultado(J1,J2):
    if(J1!=J2):
        if(J1=="Pi" or J2=="Pi"):
            return Ganador(J1 =="Pi","Pa","Ti",J1,J2)
        elif(J1=="Pa" or J2=="Pa"):
            return Ganador(J1 =="Pa","Ti","Pi",J1,J2)
        elif(J1=="Ti" or J2=="Ti"):
            return Ganador(J1 =="Ti","Pi","Pa",J1,J2)
        


#Pintar un tablero de ajedrez con un bucle
import string
def Ejercicio4():
    listaFichasNegras = ("♖","♘","♗","♔","♕","♗","♘","♖")
    listaFichasBlancas = ("♜","♞","♝","♛","♚","♝","♞","♜")
    peonBlanco = "♟"
    peonNegro = "♙"
    Mapa =  [[0 for x in range(8)] for y in range(8)] 
    Mapa = CheckLista(listaFichasNegras,Mapa,0,peonNegro,1)
    Mapa = RellenarEspacios(Mapa)
    Mapa = CheckLista(listaFichasBlancas,Mapa,7,peonBlanco,6)
    MostrarMapaOrdenado(Mapa)
    Jugar(Mapa)
        

def CheckLista(lista,Mapa,v,peon,pPosicion):
    for i,value in enumerate(lista):
        Mapa[v][i] = f" {value} "
    for i in range(8):
        Mapa[pPosicion][i] = f" {peon} "
    return Mapa

def RellenarEspacios(Mapa):
    for x in range(5):
        for y in range(8):
            Mapa[x+2][y] = f" - "
    return Mapa

def MostrarMapaOrdenado(Mapa):
    for x in range(9):
        if(x == 0):
            print("           ",end=" ",flush=True)
        else:
            print(f" #   {string.ascii_uppercase[x-1]}   # ",end=" ",flush=True)
    print("")
    for index,x in enumerate(Mapa):
        print(f" #   {index+1}   # ",end=" ",flush=True)
        for y in x:
            print(f" |  {y}  | ",end=" ",flush=True)
        print("")

def Jugar(Mapa):
    while True:
        try:
            fichaAMover = input("Dime la posición de la ficha\n").lower()
            if(fichaAMover == "exit"):
                break
            fichaDondeMover = input("Dime a donde se va mover\n").lower()
            if(fichaDondeMover == "exit"):
                break
            xFichaMovida=string.ascii_lowercase.index(fichaAMover[0])
            xFichaDondeMover=string.ascii_lowercase.index(fichaDondeMover[0])
            TempValue = Mapa[int(fichaAMover[1])-1][xFichaMovida]
            GestorDeJuego(TempValue,fichaAMover,fichaDondeMover)
            Mapa[int(fichaDondeMover[1])-1][xFichaDondeMover] = TempValue
            Mapa[int(fichaAMover[1])-1][xFichaMovida] = " - "
        except Exception as e:
            print("POSICIÓN NO VALIDA")
            print(e)
        MostrarMapaOrdenado(Mapa)

def GestorDeJuego(Ficha,colocacionActual,colocacionNueva):
    if (Ficha == "♖" or Ficha=="♜"):
        if(colocacionActual[1]!=colocacionNueva[1] and colocacionActual[0]!=colocacionNueva[0]):
            raise Exception
    if (Ficha == "♗" or Ficha=="♝"):
        if(colocacionActual[1]==colocacionNueva[1] or colocacionActual[0]==colocacionNueva[0]):
            raise Exception




#Ejercicio1()
#Ejercicio2()
#Ejercicio3()
Ejercicio4()