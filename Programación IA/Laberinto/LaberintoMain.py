"""
Laberinto
    -Según una entrada y una salida 
"""



import copy
import time
from PersonajeLaberinto import PersonajeLaberinto


def ejercicio_laberinto():
    persona = PersonajeLaberinto(0,0)
    laberinto = [
        [persona,'X','X','X','X'],
        [' ','X',' ',' ',' '],
        [' ',' ',' ','X',' '],
        [' ','X',' ','X',' '],
        [' ','X','X','X',' '],
        ['X','X','X','X','END'],
    ]
    laberinto_jugador=copy.deepcopy(laberinto)
    end=False
    last_move = ""
    while not(end):
        end,last_move=movimiento(persona,laberinto,laberinto_jugador,last_move)
    print("LLEGUÉ AL FINAL")

def movimiento(persona,laberinto,laberinto_jugador,last_move):
    end = False
    if(laberinto_jugador[persona.posicionX+1][persona.posicionY]!='X'):
        if(last_move=="-X" and laberinto_jugador[persona.posicionX][persona.posicionY-1]!='X'):
            laberinto_jugador,persona,end=check_movimiento(laberinto,persona.posicionX,persona.posicionY-1,persona,laberinto_jugador)
        elif(last_move=="-X" and laberinto_jugador[persona.posicionX][persona.posicionY+1]!='X'):
            laberinto_jugador,persona,end=check_movimiento(laberinto,persona.posicionX,persona.posicionY+1,persona,laberinto_jugador)
        elif(last_move=="-X" and laberinto_jugador[persona.posicionX-1][persona.posicionY]!='X'):
            laberinto_jugador,persona,end=check_movimiento(laberinto,persona.posicionX-1,persona.posicionY,persona,laberinto_jugador)
        else:
            laberinto_jugador,persona,end=check_movimiento(laberinto,persona.posicionX+1,persona.posicionY,persona,laberinto_jugador)
            last_move = "+X"
    elif(laberinto_jugador[persona.posicionX][persona.posicionY+1]!='X'):
        laberinto_jugador,persona,end=check_movimiento(laberinto,persona.posicionX,persona.posicionY+1,persona,laberinto_jugador)
        last_move = "+Y"
    elif(laberinto_jugador[persona.posicionX-1][persona.posicionY]!='X'and persona.posicionX-1>=0):
        if(last_move=="-X" and laberinto_jugador[persona.posicionX+1][persona.posicionY]!='X'):
            laberinto_jugador,persona,end=check_movimiento(laberinto,persona.posicionX+1,persona.posicionY,persona,laberinto_jugador)
        else:
            laberinto_jugador,persona,end=check_movimiento(laberinto,persona.posicionX-1,persona.posicionY,persona,laberinto_jugador)
            last_move = "-X"
    elif(laberinto_jugador[persona.posicionX][persona.posicionY-1]!='X' and persona.posicionY-1>=0):
        laberinto_jugador,persona,end=check_movimiento(laberinto,persona.posicionX,persona.posicionY-1,persona,laberinto_jugador)
        last_move = "-Y"
    printar_laberinto(laberinto)
    time.sleep(1)
    return end,last_move

def check_movimiento(laberinto,x,y,persona,laberinto_jugador):
    end = False
    esquina=0
    if(not(persona.posicionX==0 and persona.posicionY==0)):
        if(persona.posicionX+1<=len(laberinto_jugador[0]) and laberinto_jugador[persona.posicionX+1][persona.posicionY]=="X"):
            esquina+=1
        if(laberinto_jugador[persona.posicionX-1][persona.posicionY]=="X" or persona.posicionX-1<0):
            esquina+=1
        if(persona.posicionY+1<len(laberinto_jugador[0]) and laberinto_jugador[persona.posicionX][persona.posicionY+1]=="X"):
            esquina+=1
        if(laberinto_jugador[persona.posicionX][persona.posicionY-1]=="X" or persona.posicionY-1<0):
            esquina+=1
    if(laberinto_jugador[x][y]=="END"):
        end = True
    laberinto_jugador[x][y]=persona
    laberinto[x][y]=persona
    laberinto_jugador[persona.posicionX][persona.posicionY]=' '
    laberinto[persona.posicionX][persona.posicionY]=' '
    if(esquina>=3):
        laberinto_jugador[persona.posicionX][persona.posicionY]="X"
    persona.posicionX=x
    persona.posicionY=y
    return laberinto_jugador,persona,end

def printar_laberinto(laberinto):
    for y in laberinto:
        for x in y:
            print(f" {x} " if not(isinstance(x,PersonajeLaberinto)) else " # ",end=" ",flush=True)
        print("")
    print("---------------------------------------------")

ejercicio_laberinto()
