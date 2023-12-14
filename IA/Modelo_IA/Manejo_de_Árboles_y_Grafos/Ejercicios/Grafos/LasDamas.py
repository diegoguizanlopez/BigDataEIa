from Grafos.Grafo import GrafoAvanzado

class GrafoDamas(GrafoAvanzado):
    
    def genera_elementos(self,nColumn):
        v=[]
        for x in range(nColumn):
            v.append([i for i in range(nColumn)])
            