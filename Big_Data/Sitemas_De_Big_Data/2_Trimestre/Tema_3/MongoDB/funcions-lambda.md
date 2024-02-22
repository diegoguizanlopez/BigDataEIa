(sen rematar)
# Python e arrays. Funcións útiles e expresións lambda

Ao longo do curso deste curso de especialización en Intelixencia Artifical e Big Data, podes atopar algunhas expresións ou código que descoñezas ata agora, sobre todo se non tes empregado Python antes.

Imos ver de modo sinxelo e moi práctico algúns trucos ou [azúcre sintáctico](https://es.wikipedia.org/wiki/Az%C3%BAcar_sint%C3%A1ctico) tamén coñecido en inglés como [Syntactic sugar](https://en.wikipedia.org/wiki/Syntactic_sugar).

A diabetes non é escusa para evitar este dulce.

## Funcións lambda

As funcións lambda, tamén coñecidas como expresións lambda ou funcións anónimas (por non ter nome) son tanto asasinas de código coma superheroínas que veñen ao noso rescate.

### Función normal
Defínese coa palabra reservada `def`, **exemplo**:

    def suma(operando1, operando2):
        return operando1 + operando2        
        print (suma(1,2))

### Función lambda

Defínese coa palabra reservada `lambda`, coa sintaxe:

>       lambda parametros: expresión

A expresión inclúe normalmente a devolución dun parámetro.

**Exemplo**:

        lambda operando1,operando2: operando1+operando2

Aínda que a función non teña nome, esto non impide que poidamos almacenala nunha variable para empregala despois. Por **exemplo**:

        suma_anonima = lambda operando1,operando2: operando1+operando2
        print (suma_anonima(1,2))

Evidentemente poderíamola empregar directamente sen nomear nunha variable, por **exemplo**:

        (lambda op1, op2: op1 + op2) (1, 2)

Tamén se poden complicar un pouco máis, cunha condición con dúas partes, por **exemplo**:

        lambda_paridade = lambda numero: True if numero%2 == 0 else False
        lambda_paridade(3)
        lambda_paridade(4)

Realmente tamén poderíamos ter posto a versión abreviada:

        lambda_paridade = lambda numero: numero%2 == 0
        lambda_paridade(3)
        lambda_paridade(4)

Esta función de ordenación que veremos despois, tamén fai uso dunha función lambda para axudar a ordenaro os datos. O seguinte **exemplo** ordea os valores divisibles entre 11 antes que os que non o son:

        o_meu_dicionario = {"Peras": 11, 
            "Mazás": 21, 
            "Laranxas": 33, 
            "Pexegos": 55}
        sorted(o_meu_dicionario, key=lambda x: o_meu_dicionario[x]%11)

O resultado é:

    ['Peras', 'Laranxas', 'Pexegos', 'Mazás']

#### Cando son útiles

  - Cando é unha función breve (dunha liña de código) e non se precisa esa función en ningún sitio máis do módulo actual.
  - Para empregar coma **funcións integradas** dentro doutra función, por exemplo con: map(), filter() ou reduce(). Python dispón de 69 funcións que se poden empregar sen necesidade de importalas, de ahí o nome de integradas: <https://docs.python.org/es/3/library/functions.html>
  - Para empregar con estruturas de datos como listas e diccionarios.

Pódense empregar para reducir as liñas de código e expresar mellor unha idea. O límite é a imaxinación.

## Funcións para creación de arrays
  - `list` ()
  - `dict` ()
  - `tuple` ()
  - `set` ()

### `list`()

As listas son arrays dinámicos:

- Non precisan ser homexéneos, o cal fai delas un elemento moi potente. 
- Poden ser escritas como unha lista de valores separados por comas entre conchetes.
- Son mutables (poden mudar de tipo de dato).
- Poden almacenar calquer tipo de dato.

O construtor para listas, sen parámetros crea unha lista baleira.

**Sintaxe**:

>     variable = list()

**Sintaxe alternativa**:

>     variable = []

Se lle pasamos unha secuencia iterable, convírtea nunha lista (tamén podemos ser redundantes e crear unha lista dunha lista).

```
    lista0 = [] # [ ]
    lista1 = list() # [ ]
    lista2 = list(1,2,3,4,5,6) # 1, 2, 3, 4, 5, 6
    lista3 = list(range(6)) # 0, 1, 2, 3, 4, 5
```
### `dict`()

O construtor da clase diccionario. Sen parámetros crea un diccionario baleiro.

```
    dic0 = {} # {}
    dic1 = dict() # {}
```

No caso de non estar baleiro, o construtor debe recibir argumentos nomeados (tipo clave-valor) `{'clave': valor}`

**Exemplos**:

```
    dic2 = {'Italia': 1, 'España': 2, 'Portugal': 3, 'Grecia': 4}
    dic3 = dict({'Italia': 1, 'España': 2, 'Portugal': 3, 'Grecia': 4})
    print (dic3['Italia']) # 1
```

Se non atopa a clave, devolve un `KeyError`.

### `tuple`()

O construtor da clase tupla. Sen parámetros crea unha tupla baleira.
 Tuple is a collection of Python objects much like a list. The sequence of values stored in a tuple can be of any type, and they are indexed by integers. Values of a tuple are syntactically separated by ‘commas’. Although it is not necessary, it is more common to define a tuple by closing the sequence of values in parentheses. The main characteristics of tuples are – 

    Tuple is an immutable sequence in python.
    It cannot be changed or replaced since it is immutable.
    It is defined under parenthesis().
    Tuples can store any type of element.

```
    tupla0 = () # ()
    tupla1 = tuple() # ()
    tupla2 = tuple("Cada letra separada") # ('C', 'a', 'd', 'a'...
    tupla3 = tuple([1,2,3,4,5,6,7,8,9,0]) # (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
```

### `set`()

set() es el constructor de la clase set. Podemos usarlo sin argumentos para crear un set vacío, o pasarle un objeto iterable cuyos elementos no repetidos serán los elementos del set. En este sentido, podemos utilizar set() para filtrar los elementos repetidos de un string o una lista.
>>> set()
set()
>>> set("Python")
{'o', 't', 'h', 'P', 'n', 'y'}
>>> set([1, 1, 2, 2, 3, 3])
{1, 2, 3}

In Python, Set is an unordered collection of data type that is iterable, mutable, and has no duplicate elements. The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set. The main characteristics of set are –

    Sets are an unordered collection of elements or unintended collection of items In python.
    Here the order in which the elements are added into the set is not fixed, it can change frequently.
    It is defined under curly braces{}
    Sets are mutable, however, only immutable objects can be stored in it.

### Comparativa
| Tipo | Símbolo | Palabra clave |
| :--- | :---:   | ---           |
| Lista | []| `list` () |
| Diccionario | {}| `dict` () |
| Tupla | ()| `tuple` () |
| Set | ()| `set` ()| 


Generación de secuencias iterables
range()

La función range(fin) genera una secuencia de números enteros que podemos utilizar para iterar en un bucle. La secuencia generada empieza en 0 y termina en el entero anterior a fin. Es decir, el valor fin no forma parte de la secuencia. Alternativamente, podemos usar range(inicio, fin, paso), donde inicio indica el primer número de la secuencia y paso cada cuantos números se toman en cuenta para la secuencia. Los valores por defecto de parámetros inicio y paso son 0 y 1 respectivamente. A modo de ejemplo, range(4, 7, 2) genera una secuencia de enteros que empieza en 4, termina en 6 y toma sus valores de 2 en 2.
>>> for x in range(2):
...     print(x)
...
0
1
>>> list(range(4, 7))
[4, 5, 6]
>>> list(range(4, 7, 2))
[4, 6]
enumerate()

La función enumerate(iterable) toma una secuencia o un iterador y retorna objeto de tipo enumerate. Dicho objeto es una secuencia iterable de tuplas con sus respectivos índices. Cada una de estas tuplas tiene la forma (i, x) donde i es el índice del objeto x perteneciente a iterable, el parámetro de entrada de la función. Por defecto el primer índice es 0, aunque también podemos definir su valor usando la función enumerate(iterable, inicio).
>>> lenguajes = ["Python", "Java", "JavaScript", "C++"]
>>> list(enumerate(lenguajes))
[(0, 'Python'), (1, 'Java'), (2, 'JavaScript'), (3, 'C++')]
>>> for i, x in enumerate(lenguajes, 1):
...     print(i, "-", x)
...
1 - Python
2 - Java
3 - JavaScript
4 - C++
Operaciones con objetos iterables
len()

La función len(objeto) retorna el número de elementos que contiene un objeto. Dicho objeto puede ser tanto una secuencia (un string, una lista, una tupla, etc.) como una colección (un diccionario).
>>> len("Python")
6
>>> len([0, 1, 2])
3
>>> len({"a":0, "b":1, "c":2})
3
sum()

La función sum(iterable) retorna el total de sumar los elementos de la secuencia iterable. Para poder realizar la suma, los elementos de iterable tienen que ser números. Por defecto, el resultado de la suma empieza a contar en 0, pero podemos hacer que empiece en otro valor si lo pasamos como segundo argumento a la función.
>>> sum([1, 2, 3])
6
>>> sum([1, 2, 3], 4)
10
max()

La función max(iterable) retorna el elemento más grande del objeto iterable. También se pueden utilizar dos o más argumentos, en cuyo caso retorna el mayor de los argumentos.
>>> max([4, 2, 8, 5])
8
>>> max("python")
'y'
>>> max("a", "z", "A", "Z")
'z'
min()

La función min(iterable) retorna el elemento más pequeño del objeto iterable. También se pueden utilizar dos o más argumentos, en cuyo caso retorna el menor de los argumentos.
>>> min([4, 2, 8, 5])
2
>>> min("python")
'h'
>>> min("a", "z", "A", "Z")
'A'
Modificaciones de objetos iterables
sorted()

La función sorted(iterable) retorna una lista con los elementos de iterable ordenados de menor a mayor. También puede retornar los elementos ordenados de mayor a menor cuando se especifica el parámetro opcional reverse del siguiente modo: sorted(iterable, reverse=True).
>>> sorted([3, 2, 5, 1, 4])
[1, 2, 3, 4, 5]
>>> sorted([3, 2, 5, 1, 4], reverse=True)
[5, 4, 3, 2, 1]
reversed()

La función reversed(secuencia) retorna un iterador revertido de los valores de una secuencia como por ejemplo un string, una lista, una tupla, etc. Es decir, intercambia el primer elemento con el último, el segundo con el penúltimo, etc.
>>> list(reversed([1, 2, 3, 4]))
[4, 3, 2, 1]
>>> tuple(reversed((1, 2, 3, 4)))
(4, 3, 2, 1)

## Funcións para traballar con arrays
  - `map` ()
  - `filter` ()
  - `reduce` ()

### `zip`()

### map()
Aplica unha función a cada un dos elementos dunha lista.

**Sintaxe**:

>     map(función, lista)

Imaxinemos que queremos unha listaxe á que lle queiramos aplicar unha función: `f(x) = 2x + 30`

```
    listaxe = [5, 10, 20, 30, 40, 70]
    listaxe_formula = []

    for x in listaxe:
        listaxe_formula.append(2*x+30)
     
    print(listaxe_formula) # [40, 50, 70, 90, 110, 170]
```

Pero tantas liñas de código poden reducirse a só tres:

```
    listaxe = [5, 10, 20, 30, 40, 70]
    listaxe_formula = list(map(lambda x : 2*x+30, listaxe))
    print(listaxe_formula) # [40, 50, 70, 90, 110, 170]
```

E por qué non complicarse un pouco máis? Poderíamos incluso pasar unha listaxe de funcións

```
    listaxe = [5, 10, 20, 30, 40, 70]
    def formula1(x):
        return 2*x+30
    
    def formula2(x):
        return 3*x-30

    formulas = [formula1, formula2]
    for y in listaxe:
        valores = list(map(lambda x : x(y), formulas))
        print(valores)

    # [40, -15]
    # [50, 0]
    # [70, 30]
    # [90, 60]
    # [110, 90]
    # [170, 180]
```

## Bucles de moitos tipos


(cambiar)
## Estructuras de datos

Funciones aplicadas a iterables
map()

La función map(funcion, iterable) aplica funcion a cada uno de los elementos del objeto iterable y retorna el resultado en un objeto map. Dicho objeto se puede convertir a tipo lista con list(), a tipo tupla con tuple(), etc.
>>> mi_lista = [1, 2, 3, 4]
>>> def cuadrado(x):
...     return x * x
...
>>> lista_map = map(cuadrado, mi_lista)
>>> type(lista_map)
<class 'map'>
>>> list(lista_map)
[1, 4, 9, 16]
filter()

La función filter(funcion, iterable) extrae todos los elementos de una secuencia iterable para los cuales la funcion retorna True. El resultado es un objeto filter que se puede convertir a secuencias tipo lista con list(), a tipo tupla con tuple(), etc.
>>> mi_lista = [1, 2, 3, 4]
>>> def es_par(x):
...     if x % 2 == 0:
...             return True
...     return False
...
>>> iterador_num_pares = filter(es_par, mi_lista)
>>> type(iterador_num_pares)
<class 'filter'>
>>> list(iterador_num_pares)
[2, 4]
zip()

La función zip() toma como argumentos un número arbitrario de iteradores, y los agrega en un objeto de tipo zip. Dicho objeto es un iterador de tuplas, donde la primera tupla está compuesta por los primeros elementos de cada uno de los iteradores, la segunda tupla por los segundos elementos, etc. Esta operación de agregación se realiza hasta haberse completado todos los elementos del iterador más corto. Como el objeto zip es iterable, podemos iterar sus elementos en un bucle for. Alternativamente, podemos convertirlo a tipo lista con list(), aunque para iterar es más eficiente usar el objeto zip ya que la lista necesita memoria para cada uno de sus elementos, mientras que los elementos de zip se van generando de manera dinámica conforme se necesitan.
>>> lista_1 = [1, 2, 3]
>>> lista_2 = [4, 5, 6]
>>> lista_zip = zip(lista_1, lista_2)
>>> type(lista_zip)
<class 'zip'>
>>> list(lista_zip)
[(1, 4), (2, 5), (3, 6)]


## Librería NumPy

Útil para matrices, arrays, etc
>     conda install scipy

 - <https://www.programiz.com/python-programming/matrix>

## Bibliografía

 - <https://peps.python.org/pep-0008/>
