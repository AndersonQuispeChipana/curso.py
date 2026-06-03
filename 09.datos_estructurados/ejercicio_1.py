# crear una lista de 5 vertebrados y 5 invertebrados el orden debe ser aleatorio, tendras que hacer las siguiente correciones
"""
1. modificar los 3 primero elementos por aves.
2. modificar el 6 y ultimo por reptiles
3, modificar el elemento 8 por gianfranco
4. mostrar toda la lista nueva con las modificaciones
"""
animales:list=["perro","araña","gato","pulpo","pez","caracol","caballo","medusa","rana","hormiga"]
#1
animales[0] = "Cóndor andino"
animales[1] = "Gallito de las rocas"
animales[2] = "Parihuana"
#2
animales[5] = "iguana"
animales[-1] = "anaconda"
#3
animales[7] = "gianfranco"
#4
print(f"mi nueva lista modificada es:{animales}")