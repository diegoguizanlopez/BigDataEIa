class GrafoBase():
    def __init__(self) -> None:
        self.nodos = {}
        self.abiertos=[]
        self.cerrados=[]
        self.nodosVistos={}
    
    def add_node(self,nodo,**kargs) -> None:
        if nodo in self.nodos: raise pe("YA EXISTE EL NODO")
        self.nodos[nodo] = {"edges":{}}
        for k,v in kargs.items(): self.nodos[nodo][k]=v
            
    def remove_node(self,nodo) -> None:
        if nodo not in self.nodos: raise pe("NO SE ENCONTRÓ EL NODO A BORRAR")
        for n in self.nodos[nodo]["edges"]:
            self.nodos[n]["edges"].pop(nodo)
        self.nodos.pop(nodo)

    def add_edge(self,nodo1,nodo2,**kargs) -> None :
        if nodo1 not in self.nodos or nodo2 not in self.nodos: raise pe("ERROR UNO DE LOS BORDES NO ENCONTRADOS")
        self.nodos[nodo1]["edges"][nodo2]=kargs
        self.nodos[nodo2]["edges"][nodo1]=kargs

    def remove_edge(self,nodo1,nodo2):
        if nodo1 not in self.nodos or nodo2 not in self.nodos: raise pe("BORDE NO ENCONTRADO")
        self.nodos[nodo1]["edges"].pop(nodo2, None)
        self.nodos[nodo2]["edges"].pop(nodo1, None)

    def set_node_atributtes(self,nodo,**kargs):
        for k,v in kargs.items():
            self.nodos[nodo][k]=v

    def get_node_attributtes(self,nodo,attributte,default=None):
        return self.nodos[nodo].get(attributte,default)
    
    def set_edge_atributtes(self,nodo1,nodo2,**kargs):
        for k,v in kargs.items():
            self.nodos[nodo1]["edges"][nodo2][k]=v

    def get_edge_atributtes(self,nodo1,nodo2,attributte,default=None):
        return self.nodos[nodo1]["edges"][nodo2].get(attributte,default)
    
    def adj(self, nodo):
        adyacentes = [n for n in self.nodos[nodo]["edges"]]
        return adyacentes
    
    def dibuja(self):
        fig, ax = plt.subplots(figsize=[20,20])
        # para cada nodo, dibuja un circulo en la posicion Xn, Yn
        for n in self.nodos:
          Xn = self.get_node_attributtes(n, "x", 0)
          Yn = self.get_node_attributtes(n, "y", 0)
          ax.scatter(Xn, Yn, s=300)
          ax.text(Xn,Yn, n)
          # para cada arista
          for arista in self.nodos[n]["edges"]:
            # mira la posicion del nodo destino Xd, Yd
            Xd = self.get_node_attributtes(arista, "x", 0)
            Yd = self.get_node_attributtes(arista, "y", 0)
            ax.plot([Xn, Xd], [Yn, Yd], color="b", linewidth=0.5)
            # Escribe el coste en la mitad de camino entre los dos nodos
            ax.text((Xn+Xd)/2, (Yn+Yd)/2, self.get_edge_atributtes(n, arista, "weight", 0), alpha=0.5)




    def pop_abiertos(self,modo="djkstra"):
        ret = None
        if modo == "profundidad":
          ret = self.abiertos.pop()
        elif modo == "anchura":
          ret = self.abiertos.pop(0)
        elif modo == "djkstra":
            values = {}
            for x in self.abiertos:
                values[x] = self.get_node_attributtes(x,"peso",np.inf)
            ret = self.abiertos.pop(self.abiertos.index(min(values)))
        elif modo == "avaricioso":
            # escoger de todos los de abiertos el que tenga menor
            # valor de distanciaDst %%%%%
            listaV={}
            for x in self.abiertos:
                listaV[x] = self.get_node_attributtes(x,"distanciaDst",np.inf)
            ret = self.abiertos.pop(self.abiertos.index(min(listaV)))
        return ret

      # si el nodo es una solución del problema devuelve TRUE
    def es_solucion(self, nodo_actual):
        print(f"Procesando nodo: {nodo_actual}")
        return False

  # devuelve una lista con todos los nodos conectados al nodo actual
    def genera_sucesores(self, nodo_actual):
        return self.adj(nodo_actual)

    # devuelve una lista con los hijos, decidiendo que hacer si ya están en abiertos o cerrados
    def procesa_repetidos(self, hijos_iniciales):
      # print(f"procesa_repetidos: {hijos_iniciales}")
      hijos = [h for h in hijos_iniciales if h not in self.abiertos and h not in self.cerrados]
      return hijos