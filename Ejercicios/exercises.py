"""
1- Definir una función max() que tome como argumento dos números y 
devuelva el mayor de ellos. 
(Es cierto que python tiene una función max() incorporada, 
pero hacerla nosotros mismos es un muy buen ejercicio.
"""

print('<---exercises1--->')
def defMax(a,b):
    if a > b:
        return a
    elif b > a:
        return b
    elif a == b:
        return b

print('El numero mayor es:', defMax(1, 5))
print('El numero mayor es:', defMax(3, 6))
print('El numero mayor es:', defMax(2, 2))

print('<---exercises2--->')
"""
2- Definir una función max_de_tres(), que tome tres números como argumentos 
y devuelva el mayor de ellos.
"""
a = 3
b = 1
c = 5

n = defMax(a , b)
nf = defMax(n, c)

print(f'El numero mayor entre {a} {b} {c} es el: {nf}')


"""
3- Escribir una función que tome un carácter y 
devuelva True si es una vocal, de lo contrario devuelve False.
"""
print('<---exercises3--->')
def is_vocal(caracter):
    vocales = ['a','e','i','o','u']
    if caracter in vocales:
        return True
    else:
        return False
    
caracter = "a"

print(f'El carácter {caracter} es una vocal?:', is_vocal(caracter))

"""
4- Escribir una función sum() y una función multip() 
que sumen y multipliquen respectivamente todos los números 
de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 
y multip([1,2,3,4]) debería devolver 24.
"""
print('<---exercises4--->')

def sumar(array):
    result = 0
    for n in array:
        result = result + (n)
    return result

array = [1,2,3,4]
print('El array sumado', sumar(array))

def multi(array):
    result = array[0]
    for n in array:
        result = result * (n)
    return result

print('El array sumado', multi(array))

"""
- Definir una función inversa() que calcule la inversión de una cadena. 
Por ejemplo la cadena "estoy probando" debería devolver la cadena 
"odnaborp yotse"
"""


def inversa(cadena):
    longitud = -(len(cadena)-1)
    nueva_cadena = str()
    for n in range(longitud,1):
        n = abs(n)
        nueva_cadena += cadena[n]
    return nueva_cadena



inversa('estoy probando')


"""
7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.
"""
def es_palindromo(cadena):
    nueva_cadena = inversa(cadena)
    if nueva_cadena == cadena:
        return True
    
print(es_palindromo('arenera'))


def es_palindromo(cadena):
    return cadena == cadena[::-1]

cadena = "reconocer"
print(es_palindromo(cadena))
