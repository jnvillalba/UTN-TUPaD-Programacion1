# README del TPI - Gestión de Países

## Descripción del programa
Este programa permite gestionar información sobre países con las siguientes funcionalidades:
- **Agregar país**: Permite añadir nuevos países con datos de población, superficie y continente
- **Actualizar país**: Modifica los datos de un país existente
- **Buscar país**: Busca países por nombre ((coincidencia parcial o exacta)
- **Filtrar por continente**: Muestra todos los países de un continente específico
- **Filtrar por rango de población**: Filtra países dentro de un rango poblacional
- **Filtrar por rango de superficie**: Filtra países dentro de un rango de superficie
- **Ordenar países**: Ordena los países por nombre, población o superficie (ascendente/descendente)
- **Mostrar estadísticas**: Muestra estadísticas generales (mayor/menor población, promedios, países por continente)
- **Guardar y salir**: Guarda los cambios en el archivo CSV y cierra el programa

Los datos se almacenan en un archivo CSV (`paises.csv`).

## Instrucciones de uso
1. Asegúrate de tener el archivo `paises.csv` en el mismo directorio que el script
2. Ejecuta el script `tpi.py` para iniciar el programa
3. Sigue las instrucciones en pantalla para interactuar con el sistema
4. Selecciona una opción del menú (1-9)
5. Sigue los prompts específicos de cada funcionalidad

## Ejemplos de entradas y salidas

### 1. Agregar país
```
Ingrese opcion: 1
Nombre del país: Chile
Población: 19000000
Superficie (km²): 756626
Continente: América
País agregado con éxito.
```

### 2. Actualizar país
```
Ingrese opcion: 2
Ingrese el nombre del país a actualizar: chile
Actualizando datos de: Chile
Nueva población: 19001000
Nueva superficie (km²): 756626  
Datos actualizados con éxito.
```

### 3. Buscar país
```
Ingrese opcion: 3
Buscar país (nombre o parte): chile

Se encontraron 1 resultado(s):
{'nombre': 'Chile', 'poblacion': 19001000, 'superficie': 756626, 'continente': 'América'}
```

### 4. Filtrar por continente
```
Ingrese opcion: 4
Ingrese continente: América 

Países encontrados en 'América':
{'nombre': 'Argentina', 'poblacion': 45376763, 'superficie': 2780400, 'continente': 'América'}
{'nombre': 'Brasil', 'poblacion': 213993437, 'superficie': 8515767, 'continente': 'América'}
{'nombre': 'Chile', 'poblacion': 19001000, 'superficie': 756626, 'continente': 'América'}
```

### 5. Filtrar por rango de población
```
Ingrese opcion: 5
Ingrese poblacion mínimo: 20001000
Ingrese poblacion máximo: 200000000

Países con poblacion entre 20001000 y 200000000:
{'nombre': 'Argentina', 'poblacion': 45376763, 'superficie': 2780400, 'continente': 'América'}
{'nombre': 'Japón', 'poblacion': 125800000, 'superficie': 377975, 'continente': 'Asia'}
{'nombre': 'Alemania', 'poblacion': 83149300, 'superficie': 357022, 'continente': 'Europa '}
```

### 6. Filtrar por rango de superficie
```
Ingrese opcion: 6
Ingrese superficie mínimo: 8515767  
Ingrese superficie máximo: 8515768

Países con superficie entre 8515767 y 8515768:
{'nombre': 'Brasil', 'poblacion': 213993437, 'superficie': 8515767, 'continente': 'América'}
```

### 7. Ordenar países
```
Ingrese opcion: 7
1. Nombre  2. Población  3. Superficie
Ordenar por: 3
¿Descendente? (s/n): s
{'nombre': 'Brasil', 'poblacion': 213993437, 'superficie': 8515767, 'continente': 'América'}
{'nombre': 'Argentina', 'poblacion': 45376763, 'superficie': 2780400, 'continente': 'América'}
{'nombre': 'Chile', 'poblacion': 19001000, 'superficie': 756626, 'continente': 'América'}
{'nombre': 'Japón', 'poblacion': 125800000, 'superficie': 377975, 'continente': 'Asia'}
{'nombre': 'Alemania', 'poblacion': 83149300, 'superficie': 357022, 'continente': 'Europa '}
```

### 8. Mostrar estadísticas
```
Ingrese opcion: 8
País con mayor población: Brasil (213993437)
País con menor población: Chile (19001000)
Promedio de población: 97464100.00
Promedio de superficie: 2557558.00
Cantidad de países por continente:
  - América: 3
  - Asia: 1
  - Europa : 1
```

### 9. Guardar y salir
```
Ingrese opcion: 9
Datos guardados. Saliendo...
```

## Manejo de errores
El programa incluye validación de datos:
- Validación de números para población y superficie
- Búsqueda insensible a mayúsculas/minúsculas
- Mensajes de error claros cuando se ingresa un valor inválido

## Participación de los integrantes
- Joaquín Villalba — Desarrollo de código principal, pruebas, documentación.
