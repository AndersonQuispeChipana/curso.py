



nombre:str = "noemi"
apellido= "carrasco"
nombre_completo:str 



print(nombre,apellido)

## f-strings (tarea)
# formato de string esto sirve para formatear string con variables de python y para sus se requiere de un f antes de escrtibir un string se debe encerrar entre llaves {}
nombre:str = "gianfranca"
edad:int = 14
# mensaje de salida me diga hola mi nombre es {} y tengo
print (f"hola mi nombre es {nombre} y tengo {edad}")

## plantillas de string
nombre_cliente:str=input("ingrese tu nombre")
ruc_cliente:int=int(input("ingrese ruc: "))
direcion_cliente:str=input("digite direccion: ")
codigo_producto:str=input("ingrese codigo producto: ")
nombre_producto:str=input("ingrese nombre producto: ")
precio_unidad:float=float(input("el precio del producto: "))
cantidad_producto:float=float(input("cantidad a comprar: "))
precio_total:float=precio_unidad*cantidad_producto

plantilla:str=f"""
cliente: {nombre_cliente}......RUC: {ruc_cliente}

"""