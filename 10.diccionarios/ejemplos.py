# modulos y libreria estandar
# libreria estandar typing tipar datos a listas y diccionarios para hacer mas optimo el codigo
# modulo es una porcion de codigo utilizable para poder usarlo necesitamos importa la parte del codigo que deseamos utilizar
# en este codigo esoty importanto desde la libreria typing la funcion union
# union me permite tipar una coleccion de tipos que si no sabes el tipo de dato con union le podemos pasar a una lista de los posibles tipos de datos que pueden tener mi valor
from typing import Union
#sin libreria
#alumno:dict[str:str|int]
alumno:dict[str:Union[str,int,float,bool]]={
    "id_alumno":1,
    "dni":76452354,
    "nombre":"mio",
    "edad":20,
    "matricula":True
}
# acceder
## clasica
print(alumno["dni"])
#print(alumno["tricula"])
## metodos
print(alumno.get("edad","valor no encontrado"))
# crear/modificar un valor
print(alumno)
alumno["nombre"]="otro" #si existe la clave actualiza
print(alumno)
alumno["ruc"]="12436578672" # si no existe la clave lo crea
print(alumno)

# crear/modificar varios
alumno.update({"nombre":"celia","edad":15})
alumno.update({"carrera":"agro","semestre":"III"})
print(alumno)
#eliminar
eliminado=alumno.pop("carrera")
print(f"el elemento eliminado es: {eliminado}")
print(f"mi nuevo diccionario {alumno}")