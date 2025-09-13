
# Práctico 4: Estructuras repetitivas
import random
# 1)
"""Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos),
 en orden creciente, mostrando un número por línea.
"""

for i in range(101):
    print(i)

# 2)
"""
Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
"""
numero = int(input("Ingresa un número entero: "))

if numero == 0:
    cantidad_digitos = 1
else:
    cantidad_digitos = 0
    while numero > 0:
        numero = numero // 10
        cantidad_digitos += 1

print(f"El número tiene {cantidad_digitos} dígitos")


# 3)
"""
Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.
"""
valor_inferior = int(input("Ingresa el valor inferior: "))
valor_superior = int(input("Ingresa el valor superior: "))

suma = 0
for i in range(valor_inferior + 1, valor_superior):
    suma += i

print(
    f"La suma de los números entre {valor_inferior} y {valor_superior} es: {suma}")

# 4)
"""
) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.
"""
suma_total = 0
while True:
    numero = int(input("Ingresa un número entero (0 para terminar): "))
    if numero == 0:
        break
    suma_total += numero

print(f"La suma total es: {suma_total}")

# 5)
"""
Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
"""


numero_secreto = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1
    if intento == numero_secreto:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break
    elif intento < numero_secreto:
        print("El número es mayor.")
    else:
        print("El número es menor.")

# 6)
"""
) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente.
"""

for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

# 7)

"""
Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.
"""

numero = int(input("Ingresa un número entero positivo: "))
suma = 0
for i in range(numero + 1):
    suma += i

print(f"La suma de los números entre 0 y {numero} es: {suma}")

# 8)
"""
Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).
"""


cantidad_numeros = 100
pares = 0
impares = 0
negativos = 0
positivos = 0

for i in range(cantidad_numeros):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero < 0:
        negativos += 1
    else:
        positivos += 1

print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números negativos: {negativos}")
print(f"Números positivos: {positivos}")

# 9)

"""
Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).
"""

cantidad_numeros = 100
suma = 0
for i in range(cantidad_numeros):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    suma += numero

media = suma / cantidad_numeros
print(f"La media de los números ingresados es: {media}")

# 10)

"""
Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. 
Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
"""

numero = int(input("Ingresa un número entero: "))
numero_invertido = 0

while numero > 0:
    ultimo_digito = numero % 10
    numero_invertido = numero_invertido * 10 + ultimo_digito
    numero = numero // 10

print(f"El número invertido es: {numero_invertido}")
