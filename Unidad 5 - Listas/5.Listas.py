# Práctico 5: Listas
import random
# 1)--
"""
Crear una lista con las notas de 10 estudiantes.
• Mostrar la lista completa.
• Calcular y mostrar el promedio.
• Indicar la nota más alta y la más baja.
"""

notas = [1, 3, 5, 3, 7, 1, 9, 5, 3, 10]
# Mostrar la lista completa.
print("Lista de notas:")
for nota in notas:
    print(nota)

#  Calcular y mostrar el promedio.
suma = 0
for nota in notas:
    suma += nota
promedio = suma / len(notas)
print("Promedio:", promedio)

# Indicar la nota más alta y la más b
mayor = notas[0]
menor = notas[0]
for nota in notas:
    if nota > mayor:
        mayor = nota
    if nota < menor:
        menor = nota
print("Nota más alta:", mayor)
print("Nota más baja:", menor)


# 2)--
"""
Pedir al usuario que cargue 5 productos en una lista.
• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
• Preguntar al usuario qué producto desea eliminar y actualizar la lista.
"""
productos = []
for i in range(5):
    prod = input(f"Ingrese el producto {i+1}: ")
    productos.append(prod)

# Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
print("\nLista ordenada alfabéticamente:")
for prod in sorted(productos):
    print(prod)

# Preguntar al usuario qué producto desea eliminar y actualizar la lista.
eliminar = input("\nIngrese el producto que desea eliminar: ")
if eliminar in productos:
    productos.remove(eliminar)
    print("Producto eliminado.")
else:
    print("El producto no estaba en la lista.")

print("\nLista actualizada:")
for prod in productos:
    print(prod)


# 3)--
"""
Generar una lista con 15 números enteros al azar entre 1 y 100.
• Crear una lista con los pares y otra con los impares.
• Mostrar cuántos números tiene cada lista.
"""
numeros = []
for i in range(15):
    numeros.append(random.randint(1, 100))

print("Lista de números generados:")
for num in numeros:
    print(num, end=" ")
print("\n")

# Crear una lista con los pares y otra con los impares.
pares = []
impares = []
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

# Mostrar cuántos números tiene cada lista.
print("Cantidad de pares:", len(pares))
print("Cantidad de impares:", len(impares))


# 4)--
"""
Dada una lista con valores repetidos:
• Crear una nueva lista sin elementos repetidos.
• Mostrar el resultado.
"""

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

# Crear una nueva lista sin elementos repetidos.
sin_repetidos = []
for item in datos:
    if item not in sin_repetidos:
        sin_repetidos.append(item)

# Mostrar el resultado.
print("Lista sin elementos repetidos:")
for item in sin_repetidos:
    print(item)

# 5)--
"""
Crear una lista con los nombres de 8 estudiantes presentes en clase.
• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
• Mostrar la lista final actualizada.
"""

estudiantes = []
for i in range(8):
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
    estudiantes.append(nombre)

while True:
    print("\nLista de estudiantes:")
    for est in estudiantes:
        print(est)
    opcion = input(
        "\n¿Desea agregar (A) o eliminar (E) un estudiante? (O para salir): ").upper()
    if opcion == "A":
        nuevo = input("Ingrese el nombre del nuevo estudiante: ")
        estudiantes.append(nuevo)
    elif opcion == "E":
        eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
        if eliminar in estudiantes:
            estudiantes.remove(eliminar)
        else:
            print("El estudiante no está en la lista.")
    elif opcion == "O":
        break
    else:
        print("Opción no válida.")

print("\nLista final de estudiantes:")
for est in estudiantes:
    print(est)


# 6)--
"""
Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).
"""
numeros = [1, 2, 3, 4, 5, 6, 7]

rotado = [numeros[-1]] + numeros[:-1]
for num in rotado:
    print(num)

# 7)--
"""
Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
• Calcular el promedio de las mínimas y el de las máximas.
• Mostrar en qué día se registró la mayor amplitud térmica.
"""
temperaturas = [
    [12, 22],
    [10, 20],
    [14, 24],
    [11, 19],
    [13, 25],
    [9, 18],
    [15, 27]
]

# Calcular el promedio de las mínimas y el de las máximas.
suma_min = 0
suma_max = 0
for dia in temperaturas:
    suma_min += dia[0]
    suma_max += dia[1]

prom_min = suma_min / len(temperaturas)
prom_max = suma_max / len(temperaturas)

print("Promedio de mínimas:", prom_min)
print("Promedio de máximas:", prom_max)

# Mostrar en qué día se registró la mayor amplitud térmica.
mayor_amplitud = temperaturas[0][1] - temperaturas[0][0]
dia_amplitud = 1

for i in range(len(temperaturas)):
    amplitud = temperaturas[i][1] - temperaturas[i][0]
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_amplitud = i + 1

print("Mayor amplitud térmica en el día:", dia_amplitud)


# 8)--
"""
Crear una matriz con las notas de 5 estudiantes en 3 materias.
• Mostrar el promedio de cada estudiante.
• Mostrar el promedio de cada materia.
"""
notas = [
    [7, 8, 6],
    [5, 6, 7],
    [9, 8, 10],
    [4, 7, 6],
    [8, 9, 7]
]

# Mostrar el promedio de cada estudiante.
print("\nPromedio por estudiante:")
for i in range(len(notas)):
    suma = 0
    for j in range(len(notas[i])):
        suma += notas[i][j]
    prom = suma / len(notas[i])
    print(f"Estudiante {i+1}: {prom}")

# Mostrar el promedio de cada materia.
print("\nPromedio por materia:")
materias = len(notas[0])
for j in range(materias):
    suma = 0
    for i in range(len(notas)):
        suma += notas[i][j]
    prom = suma / len(notas)
    print(f"Materia {j+1}: {prom}")


# 9)--
"""
Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
• Inicializarlo con guiones "-" representando casillas vacías.
• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
• Mostrar el tablero después de cada jugada.
"""

tablero = [["-", "-", "-"],
           ["-", "-", "-"],
           ["-", "-", "-"]]

for fila in tablero:
    print(" ".join(fila))
print()

for turno in range(5):
    if turno % 2 == 0:
        jugador = "X"
    else:
        jugador = "O"

    print("Turno del jugador", jugador)
    fila = int(input("Ingrese fila (0-2): "))
    col = int(input("Ingrese columna (0-2): "))

    if tablero[fila][col] == "-":
        tablero[fila][col] = jugador
    else:
        print("Casilla ocupada")

    for fila in tablero:
        print(" ".join(fila))
    print()


# 10)--
"""
10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
• Mostrar el total vendido por cada producto.
• Mostrar el día con mayores ventas totales.
• Indicar cuál fue el producto más vendido en la semana.
"""
ventas = [
    [10, 11, 12, 13, 14, 15, 16],
    [20, 18, 17, 19, 21, 22, 3],
    [5, 7, 6, 8, 9, 10, 11],
    [30, 25, 28, 32, 27, 29, 1]
]
# Mostrar el total vendido por cada producto.
print("\nTotal vendido por cada producto:")
for i in range(len(ventas)):
    total = 0
    for j in range(len(ventas[i])):
        total += ventas[i][j]
    print(f"Producto {i+1}: {total}")

# Mostrar el día con mayores ventas totales.
max_dia = 0
max_ventas = 0
for j in range(7):
    suma = 0
    for i in range(4):
        suma += ventas[i][j]
    if suma > max_ventas:
        max_ventas = suma
        max_dia = j + 1
print("\nDía con mayores ventas totales:", max_dia)

# Indicar cuál fue el producto más vendido en la semana.
mas_vendido = 0
max_total = 0
for i in range(len(ventas)):
    total = 0
    for j in range(7):
        total += ventas[i][j]
    if total > max_total:
        max_total = total
        mas_vendido = i + 1
print("Producto más vendido en la semana:", mas_vendido)
