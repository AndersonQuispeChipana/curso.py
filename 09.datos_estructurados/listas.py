lista_vacia:list=[]
print(len(lista_vacia))
# por regla el nombre de la variable debe tener el tipo de dato que se va almacenar
amores:list[str]=['wicho','pococha','cesar']
print(f"la cantidad de elementos que tiene la variable amores es: {len(amores)}")

frutas:list[str]=['🍐','🍉','🍎','🍌']
# posicion o indice
# acceder al tercer elemento
print(frutas[2])
#  acceder al 2 elemento por su indice negativo
print(frutas[-3])

## modificar el ultimo elemento cin una cereza
frutas[-1]="🍒"
print(frutas)

### slicing
ciudades:list[str]=['lima','ica','chincha','pauza','urcus']
# se deseamos que los datos extraidos sean persistentes osea se mantengan almacenados durante la ejecucion de mi programa los almaceno en una variable
datos_extraidos:list[str]=ciudades[-2:]
# si so0lo deseo mostrar y no almacenar el slicing lo realizo en el print
print(ciudades[0:3])
print(datos_extraidos)
## reemplzo de elementos por slincing
num_pares:list[int]=[1,2,5,6,8,10]
print(num_pares)
num_pares[0:3]=[2,4]
print(f"mi lista modificada es:{num_pares}")