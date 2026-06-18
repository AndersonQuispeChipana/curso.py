# libreria estandar de python
La biblioteca estándar de Python es un conjunto de módulos y paquetes que vienen incluidos con la instalación de Python. Proporciona herramientas para realizar tareas comunes sin necesidad de instalar dependencias externas.
## cuales son los más utilizados
| Módulo | Descripción |
|---------|-------------|
| `os` | Interacción con el sistema operativo |
| `sys` | Acceso a parámetros y funciones del intérprete |
| `pathlib` | Manejo moderno de rutas y archivos |
| `datetime` | Gestión de fechas y horas |
| `time` | Funciones relacionadas con el tiempo |
| `math` | Operaciones matemáticas |
| `random` | Generación de números aleatorios |
| `json` | Lectura y escritura de datos JSON |
| `csv` | Lectura y escritura de archivos CSV |
| `re` | Expresiones regulares |
| `collections` | Estructuras de datos especializadas |
| `itertools` | Herramientas para iteradores |
| `functools` | Funciones de orden superior y decoradores |
| `statistics` | Cálculos estadísticos |
| `sqlite3` | Base de datos SQLite integrada |
| `logging` | Registro y seguimiento de eventos |
| `urllib` | Trabajo con URLs y recursos web |
# y las formas de incluir en nuestros archivos de pýthon
# Formas de incluir módulos en Python
Python ofrece varias maneras de importar módulos y sus elementos en nuestros archivos.
## 1. Importar un módulo completo
```python
import math
resultado = math.sqrt(25)
print(resultado)
```
**Ventaja:** deja claro de qué módulo proviene cada función o variable.
---
## 2. Importar varios módulos
```python
import os
import sys
import json
```
---
## 3. Importar elementos específicos
```python
from math import sqrt
print(sqrt(25))
```
Permite utilizar directamente la función importada sin anteponer el nombre del módulo.
---
## 4. Importar varios elementos específicos
```python
from math import sqrt, pi
print(sqrt(16))
print(pi)
```
---
## 5. Importar usando alias
```python
import datetime as dt
hoy = dt.date.today()
print(hoy)
```
Los alias ayudan a escribir código más corto o evitar conflictos de nombres.
---
## 6. Importar elementos específicos con alias
```python
from math import sqrt as raiz
print(raiz(36))
```
---
## 7. Importar todos los elementos (no recomendado)
```python
from math import *
```
Aunque permite acceder directamente a todas las funciones y constantes, puede generar conflictos de nombres y dificultar la lectura del código.
---
## 8. Importar módulos propios
### Archivo: `utilidades.py`
```python
def saludar(nombre):
    return f"Hola {nombre}"
```
# modulos en python
Un módulo es un archivo con extensión `.py` que contiene código reutilizable, como funciones, clases, variables y constantes. Los módulos permiten organizar mejor el código y reutilizar funcionalidades en diferentes programas.
## Ventajas de utilizar módulos
- Favorecen la reutilización del código.
- Mejoran la organización de los proyectos.
- Facilitan el mantenimiento y la escalabilidad.
- Evitan la duplicación de código.
- Permiten dividir aplicaciones grandes en componentes más pequeños.
## Tipos de módulos
### Módulos de la biblioteca estándar
Son los módulos incluidos con Python.
Ejemplos:
```python
import math
import datetime
import json
import pathlib
```