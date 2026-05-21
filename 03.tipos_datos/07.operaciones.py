# operaciones aritmetica con numeros en python
# 1, suma - operador binario
# variables globales
## son daros que se pueden utilizar en cualquier parte del software que este construyendo
# variables locales
## son datos que solo son accesibles en pequeñas porciones de codigo o "scope"
firts_numb:int|float=20 
second_numb:int|float=5

print(f"la suma de {firts_numb}+{second_numb} = {firts_numb+second_numb}")
print(f"la resta de {firts_numb}-{second_numb} = {firts_numb-second_numb}")
#divi
print(f"la division de {firts_numb}/{second_numb} = {firts_numb/second_numb}")
#multiplicacion
print(f"la multiplicacion de {firts_numb}*{second_numb} = {firts_numb*second_numb}")
#divicion exacta
print(f"la diviexac de {firts_numb}//{second_numb} = {firts_numb//second_numb}")
## incremento(++,+=) OJO :esta es una abrebiatura de una expresion u operacion aretmetica no es un operador de incremento(numero=numero+1)
print(f"el incremento de {firts_numb} es {++second_numb} ")
## decremento(--, +=) (numero=numero+1)
print(f"el decremento de {firts_numb} es {--second_numb} ")
## potenciacion
print(f"la poten de {firts_numb}**{second_numb} = {firts_numb**second_numb}")