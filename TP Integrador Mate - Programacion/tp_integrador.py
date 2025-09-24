"""
SIMULADOR DE PUERTAS LÓGICAS BÁSICAS
=====================================

Este programa simula el funcionamiento de puertas lógicas digitales básicas:
- AND: Devuelve 1 solo si ambas entradas son 1
- OR: Devuelve 1 si al menos una entrada es 1  
- NOT: Invierte el valor de entrada (0->1, 1->0)

El diseño es escalable para agregar posteriormente:
- NAND: NOT AND (inverso de AND)
- NOR: NOT OR (inverso de OR)
- XOR: OR exclusivo (1 si las entradas son diferentes)
"""

# ============================================================================
# FUNCIONES PARA VALIDACIÓN DE ENTRADA
# ============================================================================


def validar_entrada_binaria(mensaje):
    """
    Valida que el usuario ingrese solo valores binarios (0 o 1).

    Parámetros:
    - mensaje (str): El mensaje a mostrar al usuario

    Retorna:
    - int: El valor binario validado (0 o 1)
    """
    while True:
        try:
            valor = int(input(mensaje))
            if valor in [0, 1]:
                return valor
            print("❌ Error: Solo se permiten valores 0 o 1")
        except ValueError:
            print("❌ Error: Ingrese solo números (0 o 1)")


def obtener_dos_entradas():
    """
    Obtiene dos valores binarios del usuario para puertas de dos entradas.

    Retorna:
    - tuple: Una tupla con los dos valores binarios (entrada1, entrada2)
    """
    print("\n📥 Ingrese los valores para las dos entradas:")
    entrada1 = validar_entrada_binaria("   Entrada A: ")
    entrada2 = validar_entrada_binaria("   Entrada B: ")
    return entrada1, entrada2


def obtener_una_entrada():
    """
    Obtiene un valor binario del usuario para puertas de una entrada.

    Retorna:
    - int: El valor binario ingresado
    """
    print("\n📥 Ingrese el valor para la entrada:")
    return validar_entrada_binaria("   Entrada: ")

# ============================================================================
# FUNCIONES DE PUERTAS LÓGICAS BÁSICAS
# ============================================================================


def puerta_and(a, b):
    """
    Implementa la puerta lógica AND.

    Parámetros:
    - a (int): Primera entrada binaria
    - b (int): Segunda entrada binaria

    Retorna:
    - int: Resultado de la operación AND (1 solo si ambas entradas son 1)
    """
    # Usando el operador lógico 'and' de Python
    # Se podría usar también: return a * b (multiplicación binaria)
    if a == 1 and b == 1:
        return 1
    else:
        return 0


def puerta_or(a, b):
    """
    Implementa la puerta lógica OR.

    Parámetros:
    - a (int): Primera entrada binaria
    - b (int): Segunda entrada binaria

    Retorna:
    - int: Resultado de la operación OR (1 si al menos una entrada es 1)
    """
    # Usando estructura condicional clara
    if a == 1 or b == 1:
        return 1
    else:
        return 0


def puerta_not(a):
    """
    Implementa la puerta lógica NOT.

    Parámetros:
    - a (int): Entrada binaria

    Retorna:
    - int: Resultado de la operación NOT (invierte el valor)
    """
    # Inversión simple usando condicional
    if a == 0:
        return 1
    else:
        return 0

# ============================================================================
# FUNCIONES PARA MOSTRAR RESULTADOS
# ============================================================================


def mostrar_tabla_verdad_dos_entradas(nombre_puerta, funcion_puerta):
    """
    Muestra la tabla de verdad completa para puertas de dos entradas.

    Parámetros:
    - nombre_puerta (str): Nombre de la puerta lógica
    - funcion_puerta (function): Función que implementa la puerta lógica

    """
    print(f"\n📊 Tabla de verdad - Puerta {nombre_puerta}")
    print("=" * 25)
    print("| A | B | Salida |")
    print("|---|---|--------|")

    # Generar todas las combinaciones posibles (00, 01, 10, 11)
    for a in [0, 1]:
        for b in [0, 1]:
            resultado = funcion_puerta(a, b)
            print(f"| {a} | {b} |   {resultado}    |")


def mostrar_tabla_verdad_una_entrada(nombre_puerta, funcion_puerta):
    """
    Muestra la tabla de verdad completa para puertas de una entrada.

    Parámetros:
    - nombre_puerta (str): Nombre de la puerta lógica
    - funcion_puerta (function): Función que implementa la puerta lógica

    """
    print(f"\n📊 Tabla de verdad - Puerta {nombre_puerta}")
    print("=" * 20)
    print("| A | Salida |")
    print("|---|--------|")

    # Solo dos posibilidades: 0 y 1
    for a in [0, 1]:
        resultado = funcion_puerta(a)
        print(f"| {a} |   {resultado}    |")


def mostrar_resultado_operacion(nombre_puerta, entradas, resultado):
    """
    Muestra el resultado de una operación específica de manera clara.

    Parámetros:
    - nombre_puerta (str): Nombre de la puerta lógica
    - entradas (list): Lista con los valores de entrada
    - resultado (int): Resultado de la operación
    """
    print(f"\n✅ Resultado de la puerta {nombre_puerta}:")
    print("=" * 35)

    if len(entradas) == 2:
        print(f"   {entradas[0]} {nombre_puerta} {entradas[1]} = {resultado}")
    else:
        print(f"   {nombre_puerta} {entradas[0]} = {resultado}")

    # Mostrar interpretación del resultado
    if resultado == 1:
        print("   🔴 Salida: ALTA (1) - La condición se cumple")
    else:
        print("   🔵 Salida: BAJA (0) - La condición no se cumple")

# ============================================================================
# MENÚ Y CONTROL DEL PROGRAMA
# ============================================================================


def mostrar_menu():
    """
    Muestra el menú principal de opciones del simulador.
    """
    print("\n" + "="*50)
    print("🔌 SIMULADOR DE PUERTAS LÓGICAS BÁSICAS")
    print("="*50)
    print("1. Puerta AND - Ambas entradas deben ser 1")
    print("2. Puerta OR  - Al menos una entrada debe ser 1")
    print("3. Puerta NOT - Invierte la entrada")
    print("4. Ver todas las tablas de verdad")
    print("5. Salir del programa")
    print("="*50)


def ejecutar_puerta_generica(nombre_puerta, descripcion, funcion_puerta, es_una_entrada=False):
    """
    Función genérica para ejecutar cualquier puerta lógica.

    Parámetros:
    - nombre_puerta (str): Nombre de la puerta (ej: "AND", "OR", "NOT")
    - descripcion (str): Descripción de cómo funciona la puerta
    - funcion_puerta (function): Función que implementa la puerta lógica
    - es_una_entrada (bool): True si la puerta tiene una entrada, False si tiene dos
    """
    print(f"\n🔧 PUERTA {nombre_puerta} SELECCIONADA")
    print(descripcion)

    # Obtener entradas según el tipo de puerta
    if es_una_entrada:
        # Para puertas de una entrada (como NOT)
        entrada = obtener_una_entrada()
        entradas = [entrada]
        resultado = funcion_puerta(entrada)
    else:
        # Para puertas de dos entradas (como AND, OR)
        a, b = obtener_dos_entradas()
        entradas = [a, b]
        resultado = funcion_puerta(a, b)

    # Mostrar el resultado
    mostrar_resultado_operacion(nombre_puerta, entradas, resultado)

    # Preguntar si quiere ver la tabla de verdad
    ver_tabla = input(
        "\n¿Desea ver la tabla de verdad completa? (s/n): ").lower()
    if ver_tabla == 's' or ver_tabla == 'si':
        if es_una_entrada:
            mostrar_tabla_verdad_una_entrada(nombre_puerta, funcion_puerta)
        else:
            mostrar_tabla_verdad_dos_entradas(nombre_puerta, funcion_puerta)


def ejecutar_puerta_and():
    """
    Ejecuta la simulación de la puerta AND usando la función genérica.
    """
    ejecutar_puerta_generica(
        nombre_puerta="AND",
        descripcion="La puerta AND devuelve 1 solo si AMBAS entradas son 1",
        funcion_puerta=puerta_and,
        es_una_entrada=False
    )


def ejecutar_puerta_or():
    """
    Ejecuta la simulación de la puerta OR usando la función genérica.
    """
    ejecutar_puerta_generica(
        nombre_puerta="OR",
        descripcion="La puerta OR devuelve 1 si AL MENOS UNA entrada es 1",
        funcion_puerta=puerta_or,
        es_una_entrada=False
    )


def ejecutar_puerta_not():
    """
    Ejecuta la simulación de la puerta NOT usando la función genérica.
 """
    ejecutar_puerta_generica(
        nombre_puerta="NOT",
        descripcion="La puerta NOT invierte la entrada: 0->1, 1->0",
        funcion_puerta=puerta_not,
        es_una_entrada=True
    )


def mostrar_todas_las_tablas():
    """
    Muestra todas las tablas de verdad de las puertas disponibles.
    """
    print("\n📚 TODAS LAS TABLAS DE VERDAD")
    print("="*50)

    # Mostrar tabla de verdad de cada puerta
    mostrar_tabla_verdad_dos_entradas("AND", puerta_and)
    mostrar_tabla_verdad_dos_entradas("OR", puerta_or)
    mostrar_tabla_verdad_una_entrada("NOT", puerta_not)


def validar_opcion_menu():
    """
    Valida que el usuario seleccione una opción válida del menú.

    Retorna:
    - int: Opción válida seleccionada (1-5)
    """
    while True:
        try:
            opcion = int(input("\n👉 Seleccione una opción (1-5): "))
            if 1 <= opcion <= 5:
                return opcion
            else:
                print("❌ Error: Seleccione una opción entre 1 y 5")
        except ValueError:
            print("❌ Error: Ingrese solo números")

# ============================================================================
# FUNCIÓN PRINCIPAL DEL PROGRAMA
# ============================================================================


def main():
    """
    Función principal que controla el flujo del programa.
    """
    # Mensaje de bienvenida
    print("🎯 ¡Bienvenido al Simulador de Puertas Lógicas!")
    print("Este programa te ayudará a entender cómo funcionan las puertas lógicas básicas.")

    # Bucle principal del programa
    while True:
        # Mostrar menú de opciones
        mostrar_menu()

        # Obtener opción del usuario
        opcion = validar_opcion_menu()

        # Ejecutar la opción seleccionada usando estructura condicional
        if opcion == 1:
            ejecutar_puerta_and()
        elif opcion == 2:
            ejecutar_puerta_or()
        elif opcion == 3:
            ejecutar_puerta_not()
        elif opcion == 4:
            mostrar_todas_las_tablas()
        elif opcion == 5:
            # Salir del programa
            print("\n👋 ¡Gracias por usar el simulador!")
            print("🎓 Espero que hayas aprendido sobre puertas lógicas.")
            break

        # Pausa para que el usuario pueda leer los resultados
        input("\n⏸️  Presione Enter para continuar...")

# ============================================================================
# EXTENSIBILIDAD FUTURA - COMENTARIOS PARA AGREGAR MÁS PUERTAS
# ============================================================================


"""
CÓMO AGREGAR NUEVAS PUERTAS LÓGICAS (NAND, NOR, XOR):

Con la nueva estructura genérica, agregar puertas es AÚN MÁS FÁCIL:

1. Agregar la función de la nueva puerta en la sección de funciones:
   
   def puerta_nand(a, b):
       # NAND es NOT AND: invierte el resultado de AND
       return puerta_not(puerta_and(a, b))
   
   def puerta_nor(a, b):
       # NOR es NOT OR: invierte el resultado de OR
       return puerta_not(puerta_or(a, b))
   
   def puerta_xor(a, b):
       # XOR devuelve 1 solo si las entradas son diferentes
       if a != b:
           return 1
       else:
           return 0

2. Agregar opciones en el menú (modificar mostrar_menu()):
   print("6. Puerta NAND - NOT AND")
   print("7. Puerta NOR  - NOT OR")
   print("8. Puerta XOR  - OR exclusivo")

3. Agregar funciones ejecutoras SÚPER SIMPLES usando la función genérica:
   
   def ejecutar_puerta_nand():
       ejecutar_puerta_generica(
           nombre_puerta="NAND",
           descripcion="La puerta NAND es NOT AND: invierte el resultado de AND",
           funcion_puerta=puerta_nand,
           es_una_entrada=False
       )
   
   def ejecutar_puerta_nor():
       ejecutar_puerta_generica(
           nombre_puerta="NOR", 
           descripcion="La puerta NOR es NOT OR: invierte el resultado de OR",
           funcion_puerta=puerta_nor,
           es_una_entrada=False
       )
   
   def ejecutar_puerta_xor():
       ejecutar_puerta_generica(
           nombre_puerta="XOR",
           descripcion="La puerta XOR devuelve 1 solo si las entradas son diferentes",
           funcion_puerta=puerta_xor,
           es_una_entrada=False
       )

4. Modificar main() para incluir las nuevas opciones:
   elif opcion == 6:
       ejecutar_puerta_nand()
   elif opcion == 7:
       ejecutar_puerta_nor()
   elif opcion == 8:
       ejecutar_puerta_xor()

5. Actualizar mostrar_todas_las_tablas() para incluir las nuevas puertas.

VENTAJAS DE LA NUEVA ESTRUCTURA GENÉRICA:
- Menos código duplicado (DRY - Don't Repeat Yourself)
- Más fácil de mantener y menos propenso a errores
- Agregar nuevas puertas requiere solo 3-4 líneas de código
- Consistencia automática en la interfaz de usuario
- Facilita testing y debugging
"""

# ============================================================================
# EJECUCIÓN DEL PROGRAMA
# ============================================================================

if __name__ == "__main__":
    main()
