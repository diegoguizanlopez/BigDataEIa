class Persona:
    """
    Clase Persona que será propietaria de la cuenta
        :param Str nombre: Nombre de la persona
        :param Int edad: Edad de la persona
        :param Str dni: Dni correspondiente a la persona 
    """
    def __init__(self,nombre,edad,dni):
        self._nombre=nombre
        self._edad=edad
        self._dni= dni if self.dniChecker(dni) else "\033[91mDNI NO VALIDO\033[0m"
    
    @property
    def Nombre(self):
        return self._nombre

    @Nombre.setter
    def Nombre(self,v):
        self._nombre = v

    @property
    def Edad(self):
        return self._edad

    @Edad.setter
    def Edad(self,v):
        self._edad = v

    @property
    def Dni(self):
        return self._dni

    @Dni.setter
    def Dni(self,v):
        self._dni = v
    
    def mostrar(self):
        print(f"""Persona:
        Nombre: {self._nombre}
        Edad: {self._edad}
        DNI: {self._dni}""")
    
    def esMayorDeEdad(self):
        return self._edad >=18
    
    def dniChecker(self,value):
        map={
            0:"T",
            1:"R",
            2:"W",
            3:"A",
            4:"G",
            5:"M",
            6:"Y",
            7:"F",
            8:"P",
            9:"D",
            10:"X",
            11:"B",
            12:"N",
            13:"J",
            14:"Z",
            15:"S",
            16:"Q",
            17:"V",
            18:"H",
            19:"L",
            20:"C",
            21:"K",
            22:"E",
        }
        return map[int(value.replace(value[-1],""))%23] == value[-1]
        

class Cuenta:
    """
    Clase Cuenta tendrá un titular y cantidad
        :param Persona titular: Titular de la cuenta
        :param Float cantidad: Cantidad de dinero en la cuenta
    """
    def __init__(self,titular,cantidad=0):
        self._titular=titular
        self._cantidad=cantidad

    @property
    def Titular(self):
        return self._titular

    @Titular.setter
    def Titular(self,v):
        self._titular = v

    @property
    def Cantidad(self):
        return self._cantidad

    @Cantidad.setter
    def Cantidad(self,v):
        self._cantidad = v

    def mostrar(self):
        print(f"""Cuenta:
        Cantidad: {self._cantidad}""")
        self._titular.mostrar()

    def ingresar(self,cantidad):
        self._cantidad += cantidad if cantidad>0 else 0 

    def retirar(self,cantidad):
        self._cantidad -= cantidad if cantidad>0 else 0


class CuentaJoven(Cuenta):
    """
    Clase CuentaJoven tendrá un titular y cantidad a parte de una bonificación, el titular debe ser >=18 y <25
        :param Persona titular: Titular de la cuenta
        :param Float bonificación: Cantidad de dinero de bonificación por joven
        :param Float cantidad: Cantidad de dinero en la cuenta
    """
    def __init__(self, titular,bonificacion,cantidad=0):
        super().__init__(titular, cantidad)
        self._bonificacion=bonificacion

    @property
    def Bonificacion(self):
        return self._bonificacion

    @Bonificacion.setter
    def Bonificacion(self,v):
        self._bonificacion = v
    
    def esTitularValido(self):
        return self._titular._edad >= 18 and self._titular._edad <25

    def retirar(self, cantidad):
        return super().retirar(cantidad) if self.esTitularValido() and self._cantidad-cantidad>=0 else print(f"\033[91mNO ES VALIDO\033[0m")
    
    def mostrar(self):
        print(f"""CUENTA JOVEN:
        Bonificación: {self._bonificacion}% """)
        return super().mostrar()
    

titular = Persona("Juan",22,"78345612E")
titular.mostrar()
print(titular.esMayorDeEdad())


print("#########################")
c = Cuenta(titular,100)
c.ingresar(100)
c.mostrar()
print("----------------")
c.retirar(150)
c.mostrar()
print("----------------")
c.retirar(-10)
c.mostrar()
print("----------------")


print("#########################")
c = CuentaJoven(titular,40,200)
print(c.esTitularValido())
c.retirar(300)
c.mostrar()
