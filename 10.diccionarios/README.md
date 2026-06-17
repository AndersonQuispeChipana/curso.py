# DICCIONARIOS 📖
los diccionarios son la forma mas comun de almacenar datos estructurados de objetos que nos rodean en el mundo , al igual que las listas que guardan informacion en `elementos`, de igual manera los diccionarios alamcenar sus datos en `elementos` separados por comas.
la diferencia es que las listas almacenan los elementos por `indice` y `valor`.
y los diccionarios almacenan los eloementos por `clave : valor`
**ejemplo:**
```python
vocales:list[str]=['a','e','i','o','u']
# indices           0   1   2   3   4
# un elemento en una lista esta comformado por dos cositas en el indice y su valor
# pra acceder a un val9or en una lista
vocales[2] # i
alumno:dict={'nombre':'eduardo','edad':40}
# un elemento en un diccionario esta conformado por clave:valor
# para acceder aun dicconario
alumno['nombre'] # eduardo
```
## Acceder a elementos
- **por clave (forma directa)**
```python
persona:dict={
    "nombre":"celia",
    "edad":16,
    "ciudad":"cavo verde",
    "email":"celi@email.com"
}
print(persona["edad"]) #16
print(persona["email"]) #celi@email.com
```
- **por su metodo (forma mas segura)**
```python
persona:dict={
    "nombre":"celia",
    "edad":16,
    "ciudad":"cavo verde",
    "email":"celi@email.com"
}
print(persona.get("nombre")) #celia
# la diferncia de este metodo nos permite manejar errores
print(persona.get("telefono")) #none
print(persona.get("telefono","no disponoble")) # si la clave telefono no existe no mostrara none sino el segundo parametro que le pasemos al metod get.
```
## modificar un valor existente
**cambiar un valor existente**
```python
persona:dict={
    "nombre":"celia",
    "edad":16,
}
persona["persona"]=19
# agregar una nueva clave:valor
persona["carrera"]="agro"
# si la clave no existe se crea automaticamente. si existe se actualiza
```
## agrega/actualizar multiples elementos
para esto tenemos que hacer uso de el metodo `.update`
se puede agregar si lo pares de `clave:valor` existe.
```python
tienda:dict[str:str|int]={
    "razon_social":"bigote",
    "ruc":20102123241
}
# actualizar usando el metodo de update tengo dos maneras
# 1. diccionarios
tienda.update({"ruc":23456742134,"telefono":987654321})
# 2. pares clave:valor
tienda.update(h_atencion="9-12",gerente="kevin")
```

## eliminar elementos
```python
tienda:dict[str:str|int]={
    "razon_social":"bigote",
    "ruc":20102123241
}
el_eliminado=tienda.pop("ruc")
tienda.popitem() #eliminar el ultimo elemento
# para limpiar todo el diccionario
tienda.clear()
```