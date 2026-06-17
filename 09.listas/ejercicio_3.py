alumnos:list[str]=['deduardo','noemi','victor','emerson','yo']
print(alumnos)
# eliminar por valor
alumnos.remove('yo')
print(alumnos)
# eliminar el ultimo valor por defecto
alumnos.pop()
print(alumnos)
## pop tambien elimina elementos pór indice 
### el metodo pop tiene la caracteristica de recuperar el elemento eliminado eso quiere decir que podemos alamacenarlo en una variable
a=alumnos.pop(1)
print(f"elimine: {a}")
print(f"mi lista de desaprobados sera: {alumnos}")

## tengo una lista de marcas de vehiculos(toyota,nissan,datsun,daewod,simo mack,mazda,honda), crear un programa que realize lo siguiente:
"""
1. eliminar el quinto elemento
2. en su lugar agrega la marca mitsubishi
3. buscar nissan y mostrar su valor por terminal
4. mostrar si existe honda en mi lista de vehiculos
"""
#
vehiculos:list[str] = ["toyota", "nissan", "datsun", "daewod", "simo mack", "mazda", "honda"]
#1
vehiculos.pop(4)
#2
vehiculos.insert(4, "mitsubishi")
#3
posicion = vehiculos.index("nissan")
print("Nissan se encuentra en la posición:", posicion) 
#4
existe:bool="honda" in vehiculos
print(existe)

print(vehiculos)