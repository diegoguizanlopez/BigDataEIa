class Nodo:
    def __init__(self,texto) -> None:
        self.si = None
        self.no = None
        self.texto = texto
    
class ArbolBinario:
    """
    Arbol binario con tipos de plantas
    :param Nodo root: El root del árbol
    """
    def __init__(self,root=None) -> None:
        self.root = root

    def preguntar(self,nodo):
        if nodo.si is None and nodo.no is None: print(f"LA RESPUESTA ES : {nodo.texto}")
        else:
            if True if checker_input(((input(f"{nodo.texto}\nS/N\n"))[0]).upper(),"S","N")=="S" else False:
                self.preguntar(nodo.si)
            else: self.preguntar(nodo.no)

def get_data():
    """
    Genera la data del árbol
    """
    raiz = Nodo("¿Tiene forma de aguja?")

    raiz.si = Nodo("¿Aciculas largas?")
    raiz.si.si = Nodo("PINO")
    raiz.si.no = Nodo("¿Reunidas en grupos?")
    raiz.si.no.si = Nodo("CEDRO")
    raiz.si.no.no = Nodo("ABETO")
    raiz.no = Nodo("¿Hojas pequeñas y como tejas?")
    raiz.no.si = Nodo("CIPRÉS")
    raiz.no.no = Nodo("¿Hojas compuestas?")
    raiz.no.no.si = Nodo("¿Hojas palmado compuestas?")
    raiz.no.no.si.si = Nodo("CASTAÑO DE INDIAS")
    raiz.no.no.si.no = Nodo("¿Fruto en legumbre?")
    raiz.no.no.si.no.si = Nodo("FALSA ACACIA")
    raiz.no.no.si.no.no = Nodo("FRESNO")
    raiz.no.no.no = Nodo("¿Hojas duras?")
    raiz.no.no.no.si = Nodo("¿El fruto es una bellota?")
    raiz.no.no.no.si.si = Nodo("ENCIMA")
    raiz.no.no.no.si.no = Nodo("MADROÑO")
    raiz.no.no.no.no = Nodo("¿Hoja Penninervia?")
    raiz.no.no.no.no.si = Nodo("¿Hoja dos veces más larga que ancha?")
    raiz.no.no.no.no.si.si = Nodo("SAUCE LLORÓN")
    raiz.no.no.no.no.si.no = Nodo("¿Borde inferior asimétrico?")
    raiz.no.no.no.no.si.no.si = Nodo("OLMO")
    raiz.no.no.no.no.si.no.no = Nodo("CHOPO")
    raiz.no.no.no.no.no= Nodo("¿Fruto con dos alas en ángulo?")
    raiz.no.no.no.no.no.si = Nodo("ARCE")
    raiz.no.no.no.no.no.si = Nodo("PLÁTANO DE SOMBRA")
    return raiz

def checker_input(value,result1,result2):
    """
    Controla el input de valores booleanos con lanzamiento de excepción
    :param str value: Valor que tenemos que controlar
    :param var result1: Posibilidad 1
    :param var result2: Posibilidad 2
    """
    if value == result1: return result1
    elif value == result2: return result2
    else: raise Exception("VALOR NO VALIDO")

t = ArbolBinario(get_data())
try: 
    t.preguntar(t.root)
except Exception as e:
    print(e)

