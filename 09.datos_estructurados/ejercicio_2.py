# crear un programa que me permita agregar a mi lista de compras los siguientes ingredientes(trucha,cebolla,limon,culandro,pinguita de mono,papa,cancha)

# entrada de datos
ingredientes:list[str] =[]
# desarrollo
for i in range(7):
    ingrediente:str=input("ingresa tu ingrediente: ")
    ingredientes.append(ingrediente)
# datos de salida
print(ingredientes)

