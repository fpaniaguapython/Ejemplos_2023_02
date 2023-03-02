#Existe la posibilidad de que las funciones tengan parámetros opcionales

"""
def sumar(n1, n2, n3):
    resultado=n1+n2+n3
    print(resultado)
"""

def sumar(n1, n2, n3=0):
    resultado=n1+n2+n3
    print(resultado)

sumar(3,2,1)
sumar(3,2)

def calcular(n1=0, n2=0):
    print(n1+n2)

calcular()

#Los parámetros opcionales deben ser los últimos
#def obtener(n1=1, n2, n3, n4):#ERROR
#    print("Obteniendo...") 

#Los parámetros por defecto pueden ser none
def calcular(n1=0, n2=None):
    print(n1+n2)


#Paso de parámetros por REFERENCIA (las estructuras por referencia). Se modifica el original y la copia local.
def agregar_elemento_a_lista(lista):
    lista.append("Nuevo elemento")

mi_lista = ["Elemento 1", "Elemento 2"]
agregar_elemento_a_lista(mi_lista)
print(mi_lista)


#Paso de parámetro por VALOR (los tipos básicos pasan por valor). Se modifica la copia local.
def poner_a_cero(numero):
    numero=0

mi_numero=14
poner_a_cero(mi_numero)
print(mi_numero)

#Función con parámetros variables
def funcion_variable(*parametros):
    print(type(parametros))
    for elemento in parametros:
        print(elemento)

funcion_variable(1,"Python",4,"Zaragoza")

#Función con parámetros variables + parámetro con palabra clave
def funcion_variable_2(*parametros, nombre_ciudad):
    print(type(parametros))
    for elemento in parametros:
        print(elemento)
    print("Ciudad:",nombre_ciudad)

#Función con parámetros variables + parámetro con palabra clave y valor por defecto
def funcion_variable_3(*parametros, nombre_ciudad="Madrid"):
    print(type(parametros))
    for elemento in parametros:
        print(elemento)
    print("Ciudad:",nombre_ciudad)

funcion_variable(1,"Python",4,"Zaragoza")
funcion_variable_2(1,"Python",4,nombre_ciudad="Zaragoza")
funcion_variable_3(1,"Python",4)

#Función con parámetros variables de tipo diccionario
def generar_ccaa(**kwargs): #El nombre kwargs se suele utilizar en este tipo de parámetros
    for k,v in kwargs.items():
        print(k,v)

generar_ccaa(nombre="Aragón",capital="Zaragoza",poblacion=1_321_000, superficie=47_720)



