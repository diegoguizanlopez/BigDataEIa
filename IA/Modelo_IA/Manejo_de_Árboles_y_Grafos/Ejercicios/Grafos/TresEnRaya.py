import numpy as np
from Grafos.Grafo import GrafoAvanzado

class Tres_en_Raya(GrafoAvanzado):
    def __init__(self):
        GrafoAvanzado.__init__(self)
        self.nsec = 1000


    # evaluo la pos para el jugador de pos[9]
    # le tocaría jugar al adversario
    # cuanto más alto, mejor
    def eval_posicion(self, pos):
        pos = np.fromstring(pos, dtype=int, sep=' ')
        jugador = pos[9]
        la = pos[:9].reshape(3,3)

        acum = 0
        #       en las diagonales....
        for step in (-1,1):
            s1 = np.sum(np.trace(la[::step]))
            s1abs = np.abs(s1)
            # si el jugador o el adv. tiene 3 en raya:
            if s1abs == 3: return np.inf*la[1][1]*jugador
            # si el adv. queda para culminar
            if s1 == -2*jugador: acum -= 500
            #si no acumulamos quien domina la línea
            else: acum += (s1 * jugador)
        # en las horizontales y verticales:
        for axis in (0,1):
            s1 = np.sum(la, axis=axis)
            s1abs = np.abs(s1)
            if 3 in s1abs: return (np.inf if 3*jugador in s1 else -np.inf)
            if -2*jugador in s1: acum -= 500
            else: acum += np.sum(s1 * jugador)
        return acum


    def es_posicion_final(self, nodo):
        ret = self.eval_posicion(nodo)
        return (True if (ret == np.inf or ret == -np.inf) else False)


    # devuelve una lista de nodos hijo
    def genera_sucesores(self, nodo):
        hijos = []

        if self.es_posicion_final(nodo): return hijos # es partida finalizada!!!
        ll = np.fromstring(nodo, dtype=int, sep=' ')

        # convertir la cadena en una lista
        jugador = -ll[9]
        ll[9] = jugador
        l = ll[:9]
        if np.count_nonzero(l == jugador) < 3: # la primera posición libre
            for i in np.where(l==0)[0]:
                ll[10] = self.nsec; self.nsec += 1
                l[i] = jugador; hijos.append(np.array2string(ll)[1:-1]); l[i] = 0
        else:
            # mueve cada pieza a todas las posiciones libres
            for b in np.where(l==jugador)[0]:
                for i in np.where(l==0)[0]:
                    ll[10] = self.nsec; self.nsec += 1
                    l[i] = jugador; l[b] = 0; hijos.append(np.array2string(ll)[1:-1]); l[i] = 0; l[b] = jugador

        return hijos

    def selecciona_mejor_jugada(self, nodo, nivel=0):
        hijos = [h for h in self.adj(nodo)]

        # buscamos la mejor juagada entre todos los hijos
        ganancia = -np.inf; rnodo = None
        if len(hijos) == 0 or self.es_posicion_final(nodo) or nivel > self.nvMax:
            ganancia = self.eval_posicion(nodo)
            rnodo = None

        else:

            for h in hijos:
                vdst, _ = self.selecciona_mejor_jugada(h, nivel+1)
                if vdst >= ganancia: ganancia = vdst; rnodo = h
                if vdst == np.inf: break
        # el mejor de los hijos es nuestra ganancia inversa
            ganancia = -ganancia
        return ganancia, rnodo
    
    
    def str_pos(self,pos):
        pos = np.fromstring(pos, dtype=int, sep=' ')
        la = pos[:9].reshape(3,3)
        s = ""
        for f in range(3):
            for c in range(3):
                if la[f][c] == 0: s = s + "-"
                if la[f][c] == 1: s = s + "O"
                if la[f][c] == -1: s = s + "X"
            s = s + "/"
        s = s + "="
        s = s + ("O" if pos[9] == 1 else "X")
        return s

    def print_pos(self,pos):
            pos = np.fromstring(pos, dtype=int, sep=' ')
            la = pos[:9].reshape(3,3)
            for f in range(3):
                for c in range(3):
                    if la[f][c] == 0: print("\t.", end="")
                    if la[f][c] == 1: print("\tO", end="")
                    if la[f][c] == -1: print("\tX", end="")
                print("")
            print("")


    def recorre_grafo(self, nodo_inicial = None,nodo_destino=None,modo='A*',**kargs):   

        # si no se proporciona inicial escojo el primero que se creó
        if nodo_inicial is None: nodo_inicial = list(self.nodos.keys())[0]
        if nodo_inicial not in self.nodos:
            self.add_node(nodo_inicial, distanciaOrg = 0,  distanciaDst = np.inf)
        self.nvMax=kargs.get("max_level",np.inf)



    # poner en todos los nodos un atributo distanciaOrg = inf
    # excepto en el inicial que es 0
        for n in self.nodos:
          self.set_node_atributtes(n, distanciaOrg=np.inf)
          self.set_node_atributtes(n, antecesor=None)
        self.set_node_atributtes(nodo_inicial, distanciaOrg=0)

        #%%%% poner en nodo_inicial distancia a destino

        # metemos en abiertos el nodo inicial
        self.abiertos.append(nodo_inicial)

        while len(self.abiertos) > 0: # mientras en abiertos existan nodos
          # quitar un nodo
          actual = self.pop_abiertos(modo,avaricioso=kargs.get("avaricioso",0.5),dijkstra=kargs.get("djkistra",0.5))

          # mirar si es una solución
          # si tal CAMBIAMOS A RETURN
          if self.es_solucion(actual,max_level=kargs.get('max_level',np.inf)):
            return actual

          # actual a cerrado
          self.cerrados.append(actual)

          # generar sucesores
          hijos = self.genera_sucesores(actual)


          # para cada hijo,
          # Si (distanciaOrg de actual + coste hacia el hijo )   <    distanciaOrg del hijo
          #       distanciaOrg del hijo = (distanciaOrg de actual + coste hacia el hijo )
          d_actual = self.get_node_attributtes(actual, "distanciaOrg", 0)
          for hijo in hijos:
            if hijo not in self.nodos:
                self.add_node(hijo, distanciaOrg = d_actual+1,  distanciaDst = np.inf)
                self.set_node_atributtes(hijo, antecesor=actual)
            self.add_edge(actual, hijo, weight=1)
            c_hijo = self.get_edge_atributtes(actual, hijo, "weight", 0)
            d_hijo = self.get_node_attributtes(hijo, "distanciaOrg", 0)
            if (c_hijo + d_actual) < d_hijo:
              self.set_node_atributtes(hijo, distanciaOrg=(c_hijo+d_actual))
              self.set_node_atributtes(hijo, antecesor=actual)
          # calcular la distancia a destino de cada hijo y anotarla en él
            if nodo_destino:
              d_destino = self.calcula_distanciaDst(hijo, nodo_destino)
              # actualizar en hijo esta distancia
              self.set_node_atributtes(hijo, distanciaDst=d_destino)

          # que hacer con los repetidos
          hijos = self.procesa_repetidos(hijos)


          # insertar los hijos en abiertos
          for hijo in hijos:
            self.abiertos.append(hijo)

    def es_solucion(self, nodo_actual,max_level=np.inf):
        if nodo_actual[:17].split(' ').count(1)==9: return True
        if nodo_actual[:17].split(' ').count(-1)==9: return True
        if max_level == self.get_node_attributtes(nodo_actual,'distanciaOrg',np.inf): return True
        return False