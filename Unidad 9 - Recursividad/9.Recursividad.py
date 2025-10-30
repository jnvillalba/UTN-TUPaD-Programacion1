# Práctico 9: Recursividad

# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def mostrar_factorial():
    numero = int(input("Ingrese un número entero positivo: "))
    print(f"Factorial de {numero}: {factorial(numero)}")
    print("Factoriales de todos los números entre 1 y", numero)
    for i in range(1, numero + 1):
        print(f"Factorial de {i}: {factorial(i)}")

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def mostrar_fibonacci():
    numero = int(input("Ingrese un número entero positivo: "))
    print(f"Fibonacci de {numero}: {fibonacci(numero)}")
    print("Serie de Fibonacci hasta", numero)
    for i in range(numero + 1):
        print(f"Fibonacci de {i}: {fibonacci(i)}")


# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula n^m = n * n^(m-1). Prueba esta función en un algoritmo general.

def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia_recursiva(base, exponente - 1)


def probar_potencia():
    base = int(input("Ingresa la base (n): "))
    exponente = int(input("Ingresa el exponente (m, entero positivo): "))

    if exponente < 0:
        print("El exponente no debe ser negativo.")
        return

    resultado = potencia_recursiva(base, exponente)
    print(f"\nEl resultado de {base}^{exponente} es: {resultado}")

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.


def decimal_a_binario_recursivo(n):
    if n <= 1:
        return str(n)
    else:
        return decimal_a_binario_recursivo(n // 2) + str(n % 2)


def mostrar_decimal_a_binario():
    num_decimal = int(
        input("Ingresa un número entero positivo en base decimal: "))

    if num_decimal < 0:
        print("Por favor, ingresa un número entero positivo.")
        return

    if num_decimal == 0:
        # Manejo simple del 0, aunque la función lo resuelve, es más claro aquí.
        print(f"\nEl binario de {num_decimal} es: 0")
        return

    resultado_binario = decimal_a_binario_recursivo(num_decimal)
    print(
        f"\nEl número decimal {num_decimal} en binario es: {resultado_binario}")


# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
# lo es.
#  Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])


def mostrar_es_palindromo():
    palabra = input("Ingresa una palabra sin espacios ni tildes: ")
    if es_palindromo(palabra):
        print(f"La palabra '{palabra}' es un palíndromo.")
    else:
        print(f"La palabra '{palabra}' no es un palíndromo.")

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
#  Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)


def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)


def mostrar_suma_digitos(numero):
    resultado = suma_digitos(numero)
    print(f"6. La suma de los dígitos de {numero} es: {resultado}")


# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.
#  Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)


def mostar_contar_bloques(n):
    total_bloques = contar_bloques(n)
    print(
        f"7.Total de bloques necesarios para una pirámide con {n} bloques en la base: {total_bloques}")

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.
#  Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4
# contar_digito(123456, 7) → 0


def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)


def mostrar_contar_digito(numero, digito):
    cantidad = contar_digito(numero, digito)
    print(
        f"8.El dígito {digito} aparece {cantidad} veces en el número {numero}.")


def main():
    mostrar_factorial()
    mostrar_fibonacci()
    probar_potencia()
    mostrar_decimal_a_binario()
    mostrar_es_palindromo()
    mostrar_suma_digitos(1234)
    mostar_contar_bloques(4)
    mostrar_contar_digito(12233421, 2)


if __name__ == "__main__":
    main()
