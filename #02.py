#funciones
print('<------>')
print('Funciones básicas')
def saludar():
    print('Hola soy una funcion')
print(saludar)

print('Funcion de sumar')
def suma(a, b):
    return a + b
print("La suma de 10 + 20 es de:", suma(10,20))

#FUNCION COMPLEJA
def imprimir_numeros(texto1, texto2):
    contador = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(texto1 + texto2)
            contador += 1
        elif i % 3 == 0:
            print(texto1)
            contador += 1
        elif i % 5 == 0:
            print(texto2)
            contador += 1
        else:
            print(i)
    return contador
print('Imprimir numeros',imprimir_numeros('Roy','Mustang'))