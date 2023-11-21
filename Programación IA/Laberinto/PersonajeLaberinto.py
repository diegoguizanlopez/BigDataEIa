#Archivo personaje

from typing import Any


class PersonajeLaberinto:
    posicionY = 0
    posicionX = 0

    def __init__(self,x,y):
        self.posicionX = x
        self.posicionY = y
