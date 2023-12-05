import pprint
from Grafos.Canibales import CanibalesGrafo
from Clases.PersonalizedException import PersonalizedException as pe

try:
    g = CanibalesGrafo()
    g.recorre_grafo(nodo_inicial = "0000000", modo="anchura")
    ruta = g.genera_ruta("1111111")
    print(ruta)
except pe:
    pe.getErrorMessage()