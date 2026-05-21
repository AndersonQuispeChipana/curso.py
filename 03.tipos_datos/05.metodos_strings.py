# metodos para convertitr un texto enmayuscula
texto:str="hola"
print(texto.upper())
# metodos para convertit un texto en minuscula
texto_mayuscula:str="HOLASSS"
print(texto_mayuscula.lower())
# metodo para convertit solo la primera letra en mayuscula
texto:str="buenos dias"
print(texto.capitalize())
# metodo para convertir la primeran letra de cada palabtra en mayuscula como un titulo
print(texto.title())

# metodo para quitar espacios
texto_espacios:str="       osos      "
print(texto_espacios)
# este metodo quita los espacios que estan a la derecha e izquierda . si deseamos quitar los espacios de la ezquierda usamos el nmetodo de lstrip() y si deseamos quitar los espacios solo de la derecha usamos rstrip()
print(texto_espacios.strip())

# metodo para buscar un caracter o conjunto de carateres
# find retorna el indice dond comienza el texto a buscar si el texto no se encuentra retornara -1
parrafo:str="mi mama me ama yo amo a mi mama de gianfranco"
print(parrafo.find("gianfranco"))
print(parrafo[35:])

# metodo para remplazar una parte de texto
texto_incorrecto:str=("gianfranco es malo")
print(texto_incorrecto.replace("malo","bueno"))

# (metodo) operador binario de existencia
# este operador verefica si cierto texto existe o no dentro de otro retorna true si existe y false si no
vocales:str="aeiouAEIOU"
print("A" in vocales)

# tarea averiguar que son y cuales son los operadores unarios,binarios,ternarios em python 

# ternario
# valor_si_verdadero if condicion else valor_si_falso
print ("es verdad" if 20>30 else "es falso")

## realaizar u progerama que nos pida la contraseña si la contraseña es correcta el usuario podra ingresar caso contrario dara un mensaje de contraseña incorrecta

password_user:str=input("ingresa tu contraseña:")
print("bienbenido al sistema" if password_user=="siuu7" else "contraseña incorrecta")
