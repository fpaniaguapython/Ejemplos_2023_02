import random
#Problema consiste en obtener 100_000_000 de nombres y procesarlos.
#Sin generador -> Generamos una lista de 100_000_000 cadenas de caracteres
"""
def get_nombres():
    tupla_nombres = ("Javier","Alexander","Víctor","Vanesa","Paul","Miguel Ángel")
    nombres = []
    for i in range(100_000_000):
        nuevo_nombre = random.choice(tupla_nombres)#Elige un elemento al azar de la tupla nombres
        nombres.append(nuevo_nombre)#Potencialmente colapsamos el sistema por ocupar la memoria
    return nombres
        
for nombre in get_nombres():
    print("Procesando...", nombre)
"""    

#Con generador -> Los nombres se generan de uno en uno
def get_nombres():
    print("Entrando en get_nombres")
    input("Pulsa Enter para continuar...")
    nombres = ("Javier","Alexander","Víctor","Vanesa","Paul","Miguel Ángel")
    for i in range(100_000_000):
        yield random.choice(nombres)#Elige un elemento al azar de la tupla nombres

for nombre in get_nombres():
    print("Procesando...", nombre)

