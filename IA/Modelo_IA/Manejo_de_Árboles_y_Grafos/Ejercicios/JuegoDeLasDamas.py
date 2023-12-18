from Grafos.LasDamas import GrafoDamas

gDamas = GrafoDamas(5)
gDamas.recorre_grafo(nodo_inicial=''.join(str(v) for v in gDamas.poblacion),modo="anchura")