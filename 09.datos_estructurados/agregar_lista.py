## deseamos agregar en una lsita vacia los nombres e los paises que participaran en el mundial, desarrolar el programa que haga posible esta tarea
# primera forma
paises:list[str]=[]
paises.append("peru")
paises.append("bolivia")
paises.append("chile")
print(paises)
# segundaa forma
pais:str=input("ingrese el nombre del pais: ")
paises.append(pais)
print(paises)
# terceraa forma
rango:int=int(input("ingrese la cantidad de pais que desea agregar: "))
for i in range(rango):
    nuevos_paises:str=input("ingrese un pais: ")
    paises.append(nuevos_paises)
print(paises)