# crear un programa que me permita agregar a mi lista de compras los siguientes ingredientes(trucha,cebolla,limon,culandro,pinguita de mono,papa,cancha)

# entrada de datos
ingredientes:list[str] =[]
# desarrollo
for i in range(7):
    ingrediente:str=input("ingresa tu ingrediente: ")
    ingredientes.append(ingrediente)
# datos de salida
print(ingredientes)

## crear un programa que agregue al princio de la lista del grupo a de los paises participantes en el mundial
grupo_a:list[str]=[]
grupo_a.insert(0,"REP.checa")
grupo_a.insert(0,"corea del sur")
grupo_a.insert(0,"sudafrica")
grupo_a.insert(0,"mexico")
print(grupo_a)