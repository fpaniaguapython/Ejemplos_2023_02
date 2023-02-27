#Función sin parámetros ni retorno
def hacer_nada():
    pass

#Función sin parámetros ni retorno
def saludar():
    print("Hola")

#Función con retorno
def generar_numero():
    return 2

#Función con parámetros sin retorno
def muestra_suma(sumando1, sumando2):
    print(sumando1+sumando2)

#Función con parámetros y retorno
def sumar(sumando1, sumando2):
    return (sumando1+sumando2)

#Función con parámetros, retorno y 'sugerencias' de tipos
def restar(sumando1: int, sumando2: int) -> int:
    return (sumando1-sumando2)

#Función sin parámetros que hace uso de variables 'globales'
#NO ES RECOMENDABLE
x=1
y=2
def sumar_globales():
    print(x+y)#Estas x e y son las variables 'globales'

#Ámbito de las funciones
def sumar_locales(x,y):
    print(x+y)#Estas x e y son los parámetros de la función
















