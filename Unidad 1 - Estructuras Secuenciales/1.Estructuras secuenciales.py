# Estructuras secuenciales
# 1)
"""Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”."""

print("Hola Mundo!")

# 2)
"""Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
realizar la impresión por pantalla."""

nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}!")

# 3)
"""Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
la impresión por pantalla.
"""

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
lugar = input("Ingresa tu lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}.")

# 4)
""" 
Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
"""

radio = float(input("Ingresa el radio del círculo: "))
pi = 3.141592653589793
area = pi * radio**2
perimetro = 2 * pi * radio

print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")

# 5)
"""
Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
"""

segundos = int(input("Ingresa una cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas.")

# 6)
"""
Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
"""
numero = int(input("Ingresa un número: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# 7)
"""
Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
"""

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")
print(f"División: {num1 / num2}")

# 8)
"""
Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. 
Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:
"""
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = peso / (altura**2)

print("Su índice de masa corporal (IMC) es:", imc)

# 9)
"""
Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
"""
celsius = float(input("Ingresa la temperatura en grados Celsius: "))

fahrenheit = (9 / 5) * celsius + 32

print("La temperatura en grados Fahrenheit es:", fahrenheit)

# 10)
"""10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números.
"""
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

promedio = (num1 + num2 + num3) / 3

print("El promedio de los tres números es:", promedio)
