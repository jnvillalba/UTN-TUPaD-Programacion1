# Práctico 6: Funciones

#
# 1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}


# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800


# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios

lista_frutas = list(precios_frutas.keys())


# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.
contactos = {"Juan": "123456", "Ana": "987654"}


def cargar_contactos(contactos, cantidad=5):
    """Permite al usuario cargar 'cantidad' contactos en el diccionario dado."""
    print("\n== Cargar contactos ==")
    for i in range(1, cantidad + 1):
        nombre = input(
            f"Ingrese el nombre del contacto ({i}/{cantidad}): ").strip()
        numero = input("Ingrese el número telefónico: ").strip()
        contactos[nombre] = numero
    return contactos


def consultar_contacto(contactos):
    """Consulta y muestra un contacto por nombre."""
    print("\n== Consultar contacto ==")
    nombre_buscar = input("Ingrese el nombre del contacto a buscar: ").strip()
    if nombre_buscar in contactos:
        print(f"El número de {nombre_buscar} es {contactos[nombre_buscar]}")
    else:
        print("Contacto no encontrado.")


# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.


def procesar_frase():
    frase = input("Introduce una frase: ").lower()

    palabras = frase.split()
    palabras_unicas = set(palabras)

    recuento_palabras = {}
    for palabra in palabras:
        if palabra in recuento_palabras:
            recuento_palabras[palabra] += 1
        else:
            recuento_palabras[palabra] = 1

    print("\n#Salida:")
    print(f"Palabras_únicas: {palabras_unicas}")
    print(f"Recuento: {recuento_palabras}")


# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

def ingresar_y_promediar_alumnos_simple():
    alumnos = {}

    for i in range(3):
        nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")

        nota1 = float(input(f"Ingrese la nota 1 para {nombre}: "))
        nota2 = float(input(f"Ingrese la nota 2 para {nombre}: "))
        nota3 = float(input(f"Ingrese la nota 3 para {nombre}: "))

        alumnos[nombre] = (nota1, nota2, nota3)

    print("\n--- Promedios de Alumnos ---")

    for nombre, notas in alumnos.items():
        promedio = sum(notas) / len(notas)
        print(f"El promedio de {nombre} es: {promedio:.2f}")


# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).


def procesar_aprobados():
    parcial1 = {31, 35, 33, 34, 35}
    parcial2 = {31, 32, 33, 34, 35}

    ambos_parciales = parcial1.intersection(parcial2)
    solo_un_parcial = parcial1.symmetric_difference(parcial2)
    al_menos_un_parcial = parcial1.union(parcial2)

    print("\n#Salida:")
    print(f"Aprobaron ambos parciales: {ambos_parciales}")
    print(f"Aprobaron solo uno de los dos parciales: {solo_un_parcial}")
    print(f"Aprobaron al menos un parcial: {al_menos_un_parcial}")


# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

def gestionar_stock_productos():
    stock = {"manzanas": 50, "naranjas": 30, "bananas": 20}

    while True:
        print("\n--- Gestión de Stock ---")
        print("1. Consultar stock de un producto")
        print("2. Agregar unidades a un producto existente")
        print("3. Agregar un nuevo producto")
        print("4. Mostrar todos los productos")
        print("5. Salir")

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            producto = input(
                "Ingrese el nombre del producto: ").strip().lower()
            if producto in stock:
                print(f"Stock de {producto}: {stock[producto]} unidades")
            else:
                print("El producto no existe en el inventario.")

        elif opcion == "2":
            producto = input(
                "Ingrese el nombre del producto: ").strip().lower()
            if producto in stock:
                cantidad = int(input("Ingrese la cantidad a agregar: "))
                stock[producto] += cantidad
                print(f"Nuevo stock de {producto}: {stock[producto]} unidades")
            else:
                print("El producto no existe. Use la opción 3 para agregarlo.")

        elif opcion == "3":
            producto = input(
                "Ingrese el nombre del nuevo producto: ").strip().lower()
            if producto in stock:
                print("El producto ya existe. Use la opción 2 para agregar unidades.")
            else:
                cantidad = int(input("Ingrese la cantidad inicial: "))
                stock[producto] = cantidad
                print(
                    f"Producto '{producto}' agregado con {cantidad} unidades.")

        elif opcion == "4":
            print("\n--- Stock Actual ---")
            for producto, cantidad in stock.items():
                print(f"{producto.capitalize()}: {cantidad} unidades")

        elif opcion == "5":
            print("Saliendo del sistema de gestión de stock...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Ejemplo:


agenda = {
    ("Lunes", "10:00"): "Reunión ",
    ("Martes", "15:00"): "Ingles",
}
# Permití consultar qué actividad hay en cierto día y hora.


def consultar_agenda(agenda, dia, hora):
    evento = agenda.get((dia, hora), "No hay eventos programados.")
    return evento


# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
}


def invertir_diccionario(diccionario):
    invertido = {capital: pais for pais, capital in diccionario.items()}
    print(invertido)


def main():
    invertir_diccionario(original)


if __name__ == "__main__":
    main()
