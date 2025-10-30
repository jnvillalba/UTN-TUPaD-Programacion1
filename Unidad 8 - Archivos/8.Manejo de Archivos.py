# Práctico 8: Archivos

#
# 1) Crear archivo inicial con productos: Crear un archivo de texto llamado
# productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

def crear_archivo_productos():
    productos = [
        "Lapicera,120.5,30\n",
        "Mouse,250,50\n",
        "Teclado,450,30\n"
    ]
    with open("productos.txt", "w") as archivo:
        archivo.writelines(productos)

# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
# formato:


def mostrar_productos():

    with open("productos.txt", "r") as archivo:
        print("\n--- Lista de Productos ---")
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            print(
                f"Producto: {nombre}, Precio: ${precio}, Cantidad: {cantidad} unidades")

# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# cantidad) y lo agregue al archivo sin borrar el contenido existente.


def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ").strip()
    precio = input("Ingrese el precio del producto: ").strip()
    cantidad = input("Ingrese la cantidad del producto: ").strip()

    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")
    print(f"Producto '{nombre}' agregado exitosamente.")

# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
# una lista llamada productos, donde cada elemento sea un diccionario con claves:
# nombre, precio, cantidad.


def cargar_productos():
    productos = []
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            producto = {
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
            }
            productos.append(producto)
    return productos


# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
# no existe, mostrar un mensaje de error.

def buscar_producto(productos):
    nombre = input("Ingrese el nombre del producto a buscar: ").strip()
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            print(f"Producto encontrado: {producto}")
            return
    print("Error: Producto no encontrado.")

# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
# productos actualizados desde la lista.


def sobrescribir_productos(productos):
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            archivo.write(linea)


def main():
    crear_archivo_productos()
    mostrar_productos()
    agregar_producto()
    mostrar_productos()
    productos = cargar_productos()
    buscar_producto(productos)
    sobrescribir_productos(productos)
    mostrar_productos()


if __name__ == "__main__":
    main()
