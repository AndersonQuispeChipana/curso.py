## una ferreteria tiene separada en dos listas los suiguientes productos
"""
1. lista de productos de limpieza (10 productos)
2.lista de materilaes de construccion (10 productos)
-------------------------------------------------
el dueño desea realizar las suiguientes acciones:
1. en su lista de productos de limpieza existe un material de construccion,debes eliminarlo y pasar a la lista que corresponde
2.indicar si en la lista de materiales de construccion existe cemento
3. en la lista de P.L buscar el producto de lejia y  cambiar su valorpor lejia sapolio
4.mostrar un mensaje donde se detalla cual es la lsita de M.C y la lista de P.L formateado

"""
productos_limpieza:list[str]=["lejia","detergente","jabon","desinfectante","escoba","trapeador","limpiavidrios","esponja","cemento","cera"]
materiales_construccion:list[str] = ["arena","ladrillo","fierro","yeso","pintura","madera","grava","clavos","tubos","ceramica"]
#1
elemento_retirado=productos_limpieza.pop(productos_limpieza.index("cemento"))
materiales_construccion.append(elemento_retirado)
print(materiales_construccion)
#2
existe:bool="cemento" in materiales_construccion
print(existe)
#3
productoL= productos_limpieza.index("lejia")
productos_limpieza[productoL]="lejia sapolio"
print(productos_limpieza)
#4
mensaje:str=f"""
  ======================================
  === LISTA DE PRODUCTOS DE LIMPIEZA ===
  {productos_limpieza}

  ===========================================
  === LISTA DE MATERIALES DE CONSTRUCCIÓN ===
  {materiales_construccion}
"""
print(mensaje)
