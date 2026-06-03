# Datos Estructurados 🎗️
- tenemos tres tipos de datos primarios (string, numerico, boleano)
- tenemos 2 tipos de datos estructurados (listas, diccionarios)
## Listas📖
son la manera e como python puede organizar multiples tipos de datos en una sola variable.
se puede tener :
- listas de tipo numerica
- lista de tipo texto
- listas de tipo mixto
python nos pernmite acceder a estas listas a traves de indices, los indices son ascendentes empesando del numero 0.
### Creacion de listas📖
para crear listas solo basta encerrar los elementos que deseamos almacenar con corchetes `[]` inmediatamente despues del operador de asignacion `=`
```python
# creando una lsita vacia
lista:list=[] #lista vacia
# lista mumerica
## OJON😮‍💨: los elementos de una lista se separan
lista_numerica:list[int]=[3,8,4] # listas de numeos enteros
lista_numb_mixto:list[int|float]=[3.6,7.7]
# lista de texto
amigos:list[str]=['eduardo','kevin']
# lista mixta
lista_mixta:list=['pedro',20,False,1.67]
```
### Acceder y modificar los elementos de una lista📖
para poder accerder a un elemento de la lista trabajamos con los indices que pytho le asigna a cada elemento tenemos:
- los indices positivos (comienzan de 0 y van de izquierda a derecha)
- los indices negativos(comienzan de -1 y van de derecha a izquierda)
con estos indices podemos acceder al valor del elemento y tambien podemos modificarlos
tenemos dos formas de acceder a los elementos
- acceder y modificar por indice (posicion)
```python
frutas:list[str]=["🍐","🍉","🍎","🍌"]
# posicion o indice
# acceder al tercer elemento
print(frutas[2])
#  acceder al 2 elemento por su indice negativo
print(frutas[-3])
## modificar
frutas[3]="naranja"
```
- acceder y modificar por rango (slicing)
```python
vocales:str=["a","e","i","o","u"]
# acceder a elementos por slicing
# esta tecnica nos permite acceder a mas de un elemento en una sola linea de codigo
vocales[0:3]
## reemplazar elementos por slicing
vocales[0:3]=['A','E','I']
```
## Diccionarios📖 