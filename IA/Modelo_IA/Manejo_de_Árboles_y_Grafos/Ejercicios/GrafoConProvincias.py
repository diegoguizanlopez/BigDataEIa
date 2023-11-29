import math
from Grafo import GrafoAvanzado

class GrafoConProvincias(GrafoAvanzado):
        
    def calcula_distanciaDst(self, destino, origen):
        return math.sqrt((self.get_node_attributtes(origen,"x",0)-self.get_node_attributtes(destino,"x",0))**2
                       +(self.get_node_attributtes(origen,"y",0)-self.get_node_attributtes(destino,"y",0))**2)*111