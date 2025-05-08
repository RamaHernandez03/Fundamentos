

def equal_password(invented_password):

    while True:
        print("Introduci la contraseña correcta")
        user_password = input("Introduzca la contraseña: ")
        if user_password == invented_password:
            print("Contraseña aceptada :)")
            return False
        
'''Escribir una función que reciba un número natural e imprima todos los números
impares que hay hasta ese número.'''

def n_primos(natural):

    cant_numeros = int(natural)
    numeros_printear = []

    for i in range(0, cant_numeros + 1):
        if (i%2 != 0):
            numeros_printear.append(i)
    
    print(numeros_printear)

'''a) Indique si la segunda cadena es una subcadena de la primera. Por ejemplo, 'cadena'
    es una subcadena de 'subcadena'.
    b) Devuelva la que sea anterior en orden alfábetico. Por ejemplo, si recibe 'kde' y 'gnome'
    debe devolver 'gnome'.'''

def es_subcadena(str1, str2):

    if str2 in str1:
        print("Es una subcadena")
    else:
        print("No es una subcadena")

    if str1 < str2:
        print(f"La que va primero alfabéticamente es: '{str1}'")
        return str1
    else:
        print(f"La que va primero alfabéticamente es: '{str2}'")
        return str2
    
'''Ejercicio 7.3. Campaña electoral
a) Escribir una función que reciba una tupla con nombres, y para cada nombre imprima
el mensaje Estimado <nombre>, vote por mí.
b) Escribir una función que reciba una tupla con nombres, una posición de origen p y una
cantidad n, e imprima el mensaje anterior para los n nombres que se encuentran a partir
de la posición p.
c) Modificar las funciones anteriores para que tengan en cuenta el género del destinatario,
para ello, deberán recibir una tupla de tuplas, conteniendo el nombre y el género.'''

#a,c)

def vote_por_mi(tupla):

    for nombre, genero in tupla:
        if genero == 'f':
            print(f'Estimada, Vote por mi {nombre}')
        else:
            print(f'Estimado, Vote por mi {nombre}')

#b,c)

def mensaje_anterior(tupla, p, n):

    cantidad = int(n)
    posicion = int(p)

    for i in range(posicion, cantidad + posicion):
        if i < len(tupla):
            nombre, genero = tupla[i]
            if genero == 'f':
                print(f'Estimada, Vote por mi {nombre}.')
            else:
                print(f'Estimado, Vote por mi {nombre}.')

'''Ejercicio 7.9. Escribir una función empaquetar para una lista, donde epaquetar significa indicar
la repetición de valores consecutivos mediante una tupla (valor, cantidad de repeticiones). Por
ejemplo, empaquetar([1, 1, 1, 3, 5, 1, 1, 3, 3]) debe devolver [(1, 3), (3, 1), (5, 1)
, (1, 2), (3, 2)].'''

def empaquetar(lista):

    resultado = []
    contador = 1
    elemento_actual = lista[0]

    for i in range(lista[1:]):
        if i == elemento_actual:
            contador += 1
        else:
            resultado.append((elemento_actual, contador))
            elemento_actual == i
            contador = 1
    
    resultado.append((elemento_actual, contador))
    return resultado

'''Ejercicio 7.5. Dada una lista de números enteros, escribir una función que:
a) Devuelva una lista con todos los que sean primos.
b) Devuelva la sumatoria y el promedio de los valores.
c) Devuelva una lista con el factorial de cada uno de esos números.'''

# a)

def es_primo(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def lista_primos(lista):
    lista_primos = []
    for numero in lista:
        if es_primo(numero) == True:
            lista_primos.append(numero)
    return lista_primos

# b)

def sumatoria_y_promedio(lista):
    
    resultado = []
    largo = len(lista)
    sumatoria = 0

    for elemento in lista:
        sumatoria += elemento
    
    promedio = sumatoria / largo

    resultado.append((sumatoria, promedio))
    return resultado

# c)

def factoriales(lista):

    resultado = []

    for elemento in lista:
        temporal = 1
        if elemento < 2:
            resultado.append(1)
        else:
            for i in range(2, elemento + 1):
                temporal = temporal * i
        resultado.append(temporal)

'''Ejercicio 7.6. Dada una lista de números enteros y un entero k, escribir una función que:
a) Devuelva tres listas, una con los menores, otra con los mayores y otra con los iguales a
k.
b) Devuelva una lista con aquellos que son múltiplos de k.'''

# a)

def lista_de_tres(list,k):
    menores = []
    mayores = []
    iguales = []
    param = k

    for element in list:
        if element > param:
            mayores.append(element)
        elif element < param:
            menores.append(element)
        else:
            iguales.append(element)

    return [mayores,menores,iguales]

# b)

def multiplos_k(lista, k):
    son_multiplos = []

    for elemento in lista:
        if elemento%k == 0:
            son_multiplos.append(elemento)
    
    return son_multiplos

'''Ejercicio 7.8. Inversión de listas
a) Realizar una función que, dada una lista, devuelva una nueva lista cuyo contenido sea
igual a la original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'],
deberá devolver ['papa', 'a', 'día', 'buen', 'Di'].

b) Realizar otra función que invierta la lista, pero en lugar de devolver una nueva, modi-
fique la lista dada para invertirla, sin usar listas auxiliares.'''

def reverse_list(list):
    new_list = []
    for elemento in list:
        new_list.append(elemento)
    new_list.reverse()
    return new_list

#b) 


'''Ejercicio 7.10. Matrices.
a) Escribir una función que reciba dos matrices y devuelva la suma.
b) Escribir una función que reciba dos matrices y devuelva el producto.

c) ⋆ Escribir una función que opere sobre una matriz y mediante eliminación gaussiana de-
vuelva una matriz triangular superior.

d) ⋆ Escribir una función que indique si un grupo de vectores, recibidos mediante una
lista, son linealmente independientes o no.'''

# a)

def suma_matrix(m1,m2):
    resultado = []

    for fila1, fila2 in zip(m1,m2):
        fila_suma = []
        for elem1, elem2 in zip(fila1,fila2):
            fila_suma.append(elem1 + elem2)
        resultado.append(fila_suma)

    return resultado

# b)

def producto_matrix(m1,m2):
    resultado = []

    for fila1, fila2 in zip(m1,m2):
        fila_suma = []
        for elem1, elem2 in zip(fila1,fila2):
            fila_suma.append(elem1 * elem2)
        resultado.append(fila_suma)

    return resultado

# c)

def gauss(matrix):

    filas = len(matrix)
    columnas = len(matrix[0])

    for i in range(min(filas,columnas)):
        if matrix[i][i] == 0:
            for k in range(i+1, filas):
                if matrix[k][i] != 0:
                    matrix[i], matrix[k] = matrix[k], matrix[i]
                    break
            else:
                continue

        for j in range(i + 1, filas):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i, columnas):
                matrix[j][k] -= factor * matrix[i][k]
    return matrix

'''

Ejercicio 8.1. Escribir una función que reciba una lista desordenada y un elemento, que:

a) Busque todos los elementos coincidan con el pasado por parámetro y devuelva la can-
tidad de coincidencias encontradas.
b) Busque la primera coincidencia del elemento en la lista y devuelva su posición.
c) Utilizando la función anterior, busque todos los elementos que coincidan con el pasado
por parámetro y devuelva una lista con las posiciones.

'''

#a)

def find(list, elem):
    n_coincidencias = 0
    for e in list:
        if e == elem:
            n_coincidencias += 1
    
    return n_coincidencias

#b)

def pos(list, elem):
    found = ""
    larger = len(list)
    for i in range(larger):
        if list[i] == elem:
            found = i
            return int(found)

#c) Busque todos los elementos que coincidan con el pasado por parámetro y devuelva una lista con las posiciones.

def more_pos(list, elem):
    res = []
    larger = len(list)
    for i in range(larger):
        if list[i] == elem:
            res.append(i)
    return res

'''
Ejercicio 8.2. Escribir una función que reciba una lista de números no ordenada, que:
a) Devuelva el valor máximo.
b) Devuelva una tupla que incluya el valor máximo y su posición.
c) ¿Qué sucede si los elementos son cadenas de caracteres?
Nota: no utilizar lista.sort()
'''

#a)

def higher(list):
    max = list[0]
    larger = len(list)
    for i in range(larger):
        if list[i] > max:
            max = list[i]
    return max

#b)

def a_tuple(list):
    max = list[0]
    max_pos = 0
    larger = len(list)
    for i in range(larger):
        if list[i] > max:
            max = list[i]
            max_pos = i
    return tuple (max, max_pos)


''' Ejercicio 6.5. Escribir una función que dada una cadena de caracteres, devuelva:
a) La primera letra de cada palabra. Por ejemplo, si recibe Universal Serial Bus debe
devolver USB.
b) Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe
república argentina debe devolver República Argentina.
c) Las palabras que comiencen con la letra A. Por ejemplo, si recibe Antes de ayer
debe devolver 'Antes ayer '''
        

# a)

def primera_letra(str):
    aux = ""
    entrada = str.strip().split(" ")
    for palabra in entrada:
        aux = aux + palabra[0]
    return aux

# b)

def primera_mayusc(str):
    aux = ""
    entrada = str.strip().split()
    for palabra in entrada:
        aux += palabra.capitalize() + " "
    return aux.strip()

# c) 

def letras_con_a(str):
    aux = ""
    entrada = str.strip().split()
    for palabra in entrada:
        if palabra[0] == "a" or palabra[0] == "A":
            aux += palabra + " "
    return aux.strip()

'''

Ejercicio 8.4. Sistema de facturación simplificado

Se cuenta con una lista ordenada de productos, en la que uno consiste en una tupla de (identi-
ficador, descripción, precio), y una lista de los productos a facturar, en la que cada uno consiste

en una tupla de (identificador, cantidad).

Se desea generar una factura que incluya la cantidad, la descripción, el precio unitario y el pre-
cio total de cada producto comprado, y al final imprima el total general.

Escribir una función que reciba ambas listas e imprima por pantalla la factura solicitada.

'''


def facturas(lista1, lista2):
    total_general = 0
    for id_compra, cantidad in lista2:
        for id, desc, precio in lista1:
            if id_compra == id:
                total = precio * cantidad
                total_general += total
                print(f"{cantidad} {desc} {precio:} {total}")
    print(total_general)


'''

Ejercicio 8.5. Escribir una función que reciba una lista ordenada y un elemento. Si el elemento
se encuentra en la lista, debe encontrar su posición mediante búsqueda binaria y devolverlo. Si
no se encuentra, debe agregarlo a la lista en la posición correcta y devolver esa nueva posición.
(No utilizar lista.sort().)

'''

def binary_search(list, e):
    inicio = 0
    fin = len(list) - 1
    medio = (inicio + fin) // 2

    while inicio <= fin:
        if list[medio] == e:
            return medio
        elif list[medio] < e:
            inicio = medio + 1
        elif list[medio] > e:
            fin = medio - 1
    
    list.insert(inicio, e)
    return inicio

'''

Ejercicio 9.1. Escribir una función que reciba una lista de tuplas, y que devuelva un diccionario
en donde las claves sean los primeros elementos de las tuplas, y los valores una lista con los
segundos.
Por ejemplo:
>>> l = [ ('Hola', 'don Pepito'), ('Hola', 'don Jose'),

('Buenos', 'días') ]
>>> print(tuplas_a_diccionario(l))
{ 'Hola': ['don Pepito', 'don Jose'], 'Buenos': ['días'] }

'''

def tuplas_a_diccionarios(list):
    new_dic = {}
    for primero, segundo in list:
        if primero not in new_dic:
            new_dic[primero] = []
        new_dic[primero].append(segundo)
    return new_dic


'''

Escribir una funcion que pida al usuario una frase y luego imprima las palabras en orden inverso,
asumir que no hay signos de puntuacion.
El programa debe repetirse hasta que el usuario ingrese una cadena vacia.

Ej:

Ingrese una frase: Estoy cursando programacion
programacion cursando estoy
Ingrese una frase: Hola como estas
estas como Hola
Ingrese una frase: 
Fin

'''

def todos_invertidos():
    while True:
        entrada = input("Ingrese un frase: ").strip()
        if entrada == '':
            print("Fin")
            break
        palabras = entrada.split()
        frase_invertida = ''
        for palabra in palabras:
            frase_invertida = palabra + ' ' + frase_invertida
        print(frase_invertida.strip())


'''

Sea un archivo CSV que contiene info de transferencias bancarias, con el formato
Fecha,origen,destino,monto

Por ej:

2025-06-04,Mauro,Mati,1000
2025-06-02,Juani,Mauro,12000
2025-06-06,Mauro,Mati,9000

Implementar una funcion que reciba la ruta del archivo CSV y el nombre
de una cuenta de origen y devuelva una tupla (destino,monto_total) indicando la cuenta destino
que recibio la mayor cantidad de dinero en la cuenta de origen.

En el ej anterior seria: para "Mauro" el resultado seria ("Mati", 10000)

'''


import csv

def quien_envio_mas_a_quien(arch, name):
    dic = {}
    with open(arch, 'r') as file:
        reader = csv.reader(file)
        for fecha, origen, destino, monto in reader:
            if origen == name:
                monto = float(monto)
                dic[destino] = dic.get(destino, 0) + monto
    maximo = max(dic.items(), key=lambda x: x[1])
    return maximo


'''

Escribir una funcion que reciba 2 numeros naturales n y m y devuelva una matriz de n filas y m columnas
compuesta por un patron similar a un tablero de ajedrez, intercalando ceros y unos. Por ejemplo para:
n=3 y m=6

[[0, 1, 0, 1, 0, 1],
 [1, 0, 1, 0, 1, 0],
 [0, 1, 0, 1, 0, 1]]

'''

def building_matrix(filas, columnas):
    matrix = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append((i + j) % 2)
        matrix.append(fila)
    return matrix


'''

Ejercicio 12.1.
a) Implementar la clase Intervalo(desde, hasta) que representa un intervalo entre dos
instantes de tiempo (números enteros expresados en segundos), con la condición desde
< hasta.
b) Implementar el método duracion que devuelve la duración en segundos del intervalo.

c) Implementar el método interseccion que recibe otro intervalo y devuelve un nuevo in-
tervalo resultante de la intersección entre ambos, o lanzar una excepción si la intersección
es nula.

d) Implementar el método union que recibe otro intervalo. Si los intervalos no son adya-
centes ni intersectan, debe lanzar una excepción. En caso contrario devuelve un nuevo
intervalo resultante de la unión entre ambos.

'''

class Intervalo:
    def __init__(self, desde, hasta):
        if desde >= hasta:
            raise ValueError("Error Desde debe ser < Hasta")
        self.desde = desde
        self.hasta = hasta
    
    def __str__(self):
        return f"El intervalo {self.desde} hasta {self.hasta}"
    
    def duracion(self):
        return self.hasta - self.desde
    
    def interseccion(self, otro):
        nuevo_desde = max(self.desde, otro.desde)
        nuevo_hasta = min(self.hasta, otro.hasta)
        if nuevo_desde >= nuevo_hasta:
            raise ValueError("La interseccion es nula")
        return Intervalo(nuevo_desde, nuevo_hasta)
    
    def union(self, otro):
        if self.hasta < otro.desde or otro.hasta < self.desde:
            raise ValueError("Los intervalos no se solapan ni son adyacentes")
        nuevo_desde = min(self.desde, otro.desde)
        nuevo_hasta = max(self.hasta, otro.hasta)
        return Intervalo(nuevo_desde, nuevo_hasta)
    

'''

Ejercicio 12.2.
a) Crear una clase Fraccion, que cuente con dos atributos: dividendo y divisor, que se
asignan en el constructor, y se imprimen como X/Y en el método __str__.
b) Implementar el método __add__ que recibe otra fracción y devuelve una nueva fracción
con la suma de ambas.
c) Implementar el método __mul__ que recibe otra fracción y devuelve una nueva fracción
con el producto de ambas.
d) Crear un método simplificar que modifica la fracción actual de forma que los valores
del dividendo y divisor sean los menores posibles.

'''

#a)
class Fraccion():
    def __init__(self, dividendo, divisor):
        if divisor == 0:
            raise ValueError("ERROR: No se puede dividir por 0")
        self.dividendo = dividendo
        self.divisor = divisor
    
    def __str__(self):
        return f"{self.dividendo}/{self.divisor}"
    
    def __add__(self, otra_fraccion):
        nuevo_dividendo = self.dividendo * otra_fraccion.divisor + otra_fraccion.dividendo * self.divisor
        nuevo_divisor = self.divisor * otra_fraccion.divisor
        return Fraccion(nuevo_dividendo, nuevo_divisor)
    
    def __mul__(self, nueva):
        nuevo_dividendo = self.dividendo * nueva.dividendo
        nuevo_divisor = self.divisor * nueva.divisor
        return nuevo_dividendo/nuevo_divisor
    
    def simplificar(self):
        def mcd(a , b):
            while b != 0:
                a, b = b, a % b
                return a
        divisor_comun = mcd(self.dividendo, self.divisor)
        self.dividendo //= divisor_comun
        self.divisor //= divisor_comun


'''

Ejercicio 12.3.
a) Crear una clase Vector, que en su constructor reciba una lista de elementos que serán
sus coordenadas. En el método __str__ se imprime su contenido con el formato [x,y,z]
b) Implementar el método __add__ que reciba otro vector, verifique si tienen la misma
cantidad de elementos y devuelva un nuevo vector con la suma de ambos. Si no tienen la
misma cantidad de elementos debe levantar una excepción.
c) Implementar el método __mul__ que reciba un número y devuelva un nuevo vector, con
los elementos multiplicados por ese número.

'''

class Vector():
    def __init__(self, coordenadas):
        self.coordenadas = coordenadas
    
    def __str__(self):
        return str(self.coordenadas)
    
    def __add__(self, vector):
        if len(self.coordenadas) != len(vector.coordenadas):
            raise ValueError("ERROR: Distinta cantidad de coordenadas")
        suma = []
        for i in range(len(self.coordenadas)):
            suma_aux = self.coordenadas[i] + vector.coordenadas[i]
            suma.append(suma_aux)
        return Vector(suma)
    
    def __mul__(self, numero):
        new_vec = []
        for i in range(len(self.coordenadas)):
            aux = self.coordenadas[i] * numero
            new_vec.append(aux)
        return Vector(new_vec)
    

'''

Ejercicio 7.8. Inversión de listas
a) Realizar una función que, dada una lista, devuelva una nueva lista cuyo contenido sea
igual a la original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'],
deberá devolver ['papa', 'a', 'día', 'buen', 'Di'].

b) Realizar otra función que invierta la lista, pero en lugar de devolver una nueva, modi-
fique la lista dada para invertirla, sin usar listas auxiliares.

'''

def reversed(lista):
    return list(reversed(lista))


'''

Ejercicio 12.4. Escribir una clase Caja para representar cuánto dinero hay en una caja de un
negocio, desglosado por tipo de billete (por ejemplo, en el quiosco de la esquina hay 6 billetes
de 500 pesos, 7 de 100 pesos y 4 monedas de 2 pesos). Las denominaciones permitidas son 1, 2,
5, 10, 20, 50, 100, 200, 500 y 1000 pesos. Debe comportarse según el siguiente ejemplo:
>>> c = Caja({500: 6, 300: 7, 2: 4})
ValueError: Denominación "300" no permitida
>>> c = Caja({500: 6, 100: 7, 2: 4})
>>> str(c)
'Caja {500: 6, 100: 7, 2: 4} total: 3708 pesos'
>>> c.agregar({250: 2})
ValueError: Denominación "250" no permitida
>>> c.agregar({50: 2, 2: 1})
>>> str(c)
'Caja {500: 6, 100: 7, 50: 2, 2: 5} total: 3810 pesos'
>>> c.quitar({50: 3, 100: 1})
ValueError: No hay suficientes billetes de denominación "50"
>>> c.quitar({50: 2, 100: 1})
200
>>> str(c)
'Caja {500: 6, 100: 6, 2: 5} total: 3610 pesos'

'''



'''

Ejercicio 12.5. Crear las clases Materia y Carrera, que se comporten según el siguiente ejemplo:
>>> analisis2 = Materia("61.03", "Análisis 2", 8)
>>> fisica2 = Materia("62.01", "Física 2", 8)
>>> algo1 = Materia("75.40", "Algoritmos 1", 6)
>>> c = Carrera([analisis2, fisica2, algo1])
>>> str(c)
Créditos: 0 -- Promedio: N/A -- Materias aprobadas:
>>> c.aprobar("95.14", 7)
ValueError: La materia 75.14 no es parte del plan de estudios
>>> c.aprobar("75.40", 10)
>>> c.aprobar("62.01", 7)
>>> str(c)
Créditos: 14 -- Promedio: 8.5 -- Materias aprobadas:
75.40 Algoritmos 1 (10)
62.01 Física 2 (7)

'''
    









        
        













        



    



    
    







    




    







