pos_actual = "0 0 0 0 0 0 0 0 0 -1 1000"
import numpy as np
from Grafos.TresEnRaya import Tres_en_Raya

while True:
    # genera un nuevo grafo partiendo de la posición actual y recórrelo hasta un nivel de max_level
    g = Tres_en_Raya()
    if g.es_posicion_final(pos_actual):
        print("Final de partida...")
        break
    ret = g.recorre_grafo(nodo_inicial=pos_actual, modo="anchura", max_level = 2)

    # selecciona la mejor jugada disponible, hazla y dibuja posición
    v,pos_actual = g.selecciona_mejor_jugada(pos_actual, 0)
    g.print_pos(pos_actual)
    if g.es_posicion_final(pos_actual):
        print("Final de partida...")
        break

    # le toca jugar al contrincante, pide su jugada y dibuja posción resultante
    pos_actual = np.fromstring(pos_actual, dtype=int, sep=' ')
    jugador = pos_actual[9]
    pos_actual[9] = -jugador
    la = pos_actual[:9].reshape(3,3)

    s = input("tu jugada...")
    ls = s.split(sep=" ")
    ls = list(map(int, ls))
    if len(ls) == 2:
        f = ls[0]//3; c = ls[0]%3; la[f][c] = 0
        ls.pop(0)
    if len(ls) == 1:
        f = ls[0]//3; c = ls[0]%3; la[f][c] = -1
    pos_actual = np.array2string(pos_actual)[1:-1]
    g.print_pos(pos_actual)