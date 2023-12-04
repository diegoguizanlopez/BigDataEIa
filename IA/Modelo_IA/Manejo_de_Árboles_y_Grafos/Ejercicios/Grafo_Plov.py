from Grafos.Plov import Plov
from Clases.PersonalizedException import PersonalizedException as pe

try:
    g = Plov()
    g.recorre_grafo(nodo_inicial = "0000", modo="anchura")
    ruta = g.genera_ruta("1111")
    print(ruta)
except pe:
    pe.getErrorMessage()