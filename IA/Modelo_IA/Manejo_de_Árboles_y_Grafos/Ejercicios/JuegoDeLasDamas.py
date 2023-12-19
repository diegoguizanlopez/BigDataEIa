from Grafos.LasDamas import GrafoDamas

gDamas = GrafoDamas(4)
gDamas.recorre_grafo(nodo_inicial=''.join(str(v) for v in gDamas.poblacion),modo="anchura")
gDamas.pinta_tablero()
#gDamas.recorre_grafo(nodo_inicial='[0, 0, 1, 0, 0][0, 1, 0, 0, 0][1, 0, 0, 0, 0][0, 0, 0, 0, 1][0, 0, 0, 1, 0]',modo="anchura")