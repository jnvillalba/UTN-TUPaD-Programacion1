import csv

ARCHIVO = "paises.csv"

# Funciones de archivos


def cargar_paises():
    paises = []
    try:
        with open(ARCHIVO, newline='', encoding='utf-8') as f:
            lector = csv.DictReader(f)
            for fila in lector:
                fila["poblacion"] = int(fila["poblacion"])
                fila["superficie"] = int(fila["superficie"])
                paises.append(fila)
    except FileNotFoundError:
        print("No se encontró el archivo CSV, se creará uno nuevo al guardar.")
    except Exception as e:
        print("Error al leer el archivo:", e)
    return paises


def guardar_paises(paises):
    with open(ARCHIVO, "w", newline='', encoding="utf-8") as f:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(paises)

# Funciones del sistema


def normalizar_texto(texto):
    return ' '.join(texto.strip().split()).lower()


def pais_existe(paises, nombre):
    nombre_normalizado = normalizar_texto(nombre)
    for pais in paises:
        if normalizar_texto(pais["nombre"]) == nombre_normalizado:
            return True
    return False


def agregar_pais(paises):
    while True:
        nombre = input("Nombre del país: ").strip()
        if not nombre:
            print("Error: El nombre no puede estar vacío. Intente nuevamente.")
            continue

        if pais_existe(paises, nombre):
            print(
                f"Error: El país '{nombre}' ya existe en el sistema. Intente con otro nombre.")
            continue

        break

    while True:
        try:
            poblacion = int(input("Población: "))
            if poblacion < 0:
                print("Error: La población no puede ser negativa. Intente nuevamente.")
                continue
            break
        except ValueError:
            print(
                "Error: Debe ingresar un número válido para la población. Intente nuevamente.")

    while True:
        try:
            superficie = int(input("Superficie (km²): "))
            if superficie <= 0:
                print("Error: La superficie debe ser mayor a 0. Intente nuevamente.")
                continue
            break
        except ValueError:
            print(
                "Error: Debe ingresar un número válido para la superficie. Intente nuevamente.")

    while True:
        continente = input("Continente: ").strip()
        if not continente:
            print("Error: El continente no puede estar vacío. Intente nuevamente.")
            continue
        break

    paises.append({
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    })
    print("País agregado con éxito.")


def actualizar_pais(paises):
    nombre = input("Ingrese el nombre del país a actualizar: ").strip()
    nombre_normalizado = normalizar_texto(nombre)

    pais_encontrado = None
    for pais in paises:
        if normalizar_texto(pais["nombre"]) == nombre_normalizado:
            pais_encontrado = pais
            break

    if not pais_encontrado:
        print("País no encontrado.")
        return

    print(f"Actualizando datos de: {pais_encontrado['nombre']}")

    while True:
        try:
            poblacion = int(input("Nueva población: "))
            if poblacion < 0:
                print("Error: La población no puede ser negativa. Intente nuevamente.")
                continue
            break
        except ValueError:
            print(
                "Error: Debe ingresar un número válido para la población. Intente nuevamente.")

    while True:
        try:
            superficie = int(input("Nueva superficie (km²): "))
            if superficie <= 0:
                print("Error: La superficie debe ser mayor a 0. Intente nuevamente.")
                continue
            break
        except ValueError:
            print(
                "Error: Debe ingresar un número válido para la superficie. Intente nuevamente.")

    pais_encontrado["poblacion"] = poblacion
    pais_encontrado["superficie"] = superficie
    print("Datos actualizados con éxito.")


def buscar_pais(paises):
    nombre = input("Buscar país (nombre o parte): ").strip()
    nombre_normalizado = normalizar_texto(nombre)
    encontrados = [
        p for p in paises if nombre_normalizado in normalizar_texto(p["nombre"])]
    if encontrados:
        print(f"\nSe encontraron {len(encontrados)} resultado(s):")
        for p in encontrados:
            print(p)
    else:
        print("No se encontraron coincidencias.")


def filtrar_por_continente(paises):
    cont = input("Ingrese continente: ").strip()
    cont_normalizado = normalizar_texto(cont)
    filtrados = [p for p in paises if normalizar_texto(
        p["continente"]) == cont_normalizado]
    if filtrados:
        print(f"\nPaíses encontrados en '{cont}':")
    mostrar_lista(filtrados)


def filtrar_por_rango(paises, campo):

    while True:
        try:
            minimo = int(input(f"Ingrese {campo} mínimo: "))
            if minimo < 0:
                print(
                    "Error: El valor mínimo no puede ser negativo. Intente nuevamente.")
                continue
            break
        except ValueError:
            print("Error: Debe ingresar un número válido. Intente nuevamente.")

    while True:
        try:
            maximo = int(input(f"Ingrese {campo} máximo: "))
            if maximo < minimo:
                print(
                    f"Error: El valor máximo ({maximo}) no puede ser menor que el mínimo ({minimo}). Intente nuevamente.")
                continue
            break
        except ValueError:
            print("Error: Debe ingresar un número válido. Intente nuevamente.")

    filtrados = [p for p in paises if minimo <= p[campo] <= maximo]
    if filtrados:
        print(f"\nPaíses con {campo} entre {minimo} y {maximo}:")
    mostrar_lista(filtrados)


def ordenar_paises(paises):
    print("1. Nombre  2. Población  3. Superficie")
    op = input("Ordenar por: ")
    desc = input("¿Descendente? (s/n): ").lower() == "s"
    if op == "1":
        clave = "nombre"
    elif op == "2":
        clave = "poblacion"
    elif op == "3":
        clave = "superficie"
    else:
        print("Opción inválida.")
        return
    ordenados = sorted(paises, key=lambda x: x[clave], reverse=desc)
    mostrar_lista(ordenados)


def mostrar_estadisticas(paises):
    if not paises:
        print("No hay datos cargados.")
        return
    mayor = max(paises, key=lambda x: x["poblacion"])
    menor = min(paises, key=lambda x: x["poblacion"])
    prom_pob = sum(p["poblacion"] for p in paises) / len(paises)
    prom_sup = sum(p["superficie"] for p in paises) / len(paises)
    print(
        f"País con mayor población: {mayor['nombre']} ({mayor['poblacion']})")
    print(
        f"País con menor población: {menor['nombre']} ({menor['poblacion']})")
    print(f"Promedio de población: {prom_pob:.2f}")
    print(f"Promedio de superficie: {prom_sup:.2f}")

    continentes = {}
    for p in paises:
        cont = p["continente"]
        continentes[cont] = continentes.get(cont, 0) + 1
    print("Cantidad de países por continente:")
    for c, cant in continentes.items():
        print(f"  - {c}: {cant}")


def mostrar_lista(lista):
    if not lista:
        print("No se encontraron resultados.")
        return
    for p in lista:
        print(p)

# Menú principal


def menu():
    paises = cargar_paises()
    while True:
        print("\n" + "*"*40)
        print("\n===== GESTIÓN DE PAISES =====")
        print("1. Agregar país")
        print("2. Actualizar país")
        print("3. Buscar país")
        print("4. Filtrar por continente")
        print("5. Filtrar por rango de población")
        print("6. Filtrar por rango de superficie")
        print("7. Ordenar países")
        print("8. Mostrar estadísticas")
        print("9. Guardar y salir")
        print("\n" + "*"*40)
        opcion = input("Ingrese opcion: ").strip()

        if opcion == "1":
            agregar_pais(paises)
        elif opcion == "2":
            actualizar_pais(paises)
        elif opcion == "3":
            buscar_pais(paises)
        elif opcion == "4":
            filtrar_por_continente(paises)
        elif opcion == "5":
            filtrar_por_rango(paises, "poblacion")
        elif opcion == "6":
            filtrar_por_rango(paises, "superficie")
        elif opcion == "7":
            ordenar_paises(paises)
        elif opcion == "8":
            mostrar_estadisticas(paises)
        elif opcion == "9":
            guardar_paises(paises)
            print("Datos guardados. Saliendo...")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()

# Ejemplo de país nuevo: Chile,19001000,756626,América
