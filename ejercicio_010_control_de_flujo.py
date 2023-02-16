from comunes import dias_semana
from comunes import clientes

#pass -> Es el comodín (no hace nada) para cuando hay que poner código y no hay código que poner
edad=18
if edad>=18:
    pass

#if
MAYORIA_EDAD=18
edad=21
if edad>=MAYORIA_EDAD:
    print("Es mayor de edad")
    print("Pasa")
print("Final del proceso")

if (edad>=MAYORIA_EDAD):
    print("Es mayor de edad")
    print("Pasa")
else:
    print("Es menor de edad")
    print("Fuera")

if (edad>=MAYORIA_EDAD):
    print("Es mayor de edad")
    print("Pasa")
elif (edad>=16):
    print("Anda ahí, ahí")
    print("Me lo pienso")
else:
    print("Es menor de edad")
    print("Fuera")

if (edad>=MAYORIA_EDAD):
    print("Es mayor de edad")
    print("Pasa")
    if(edad>=65):
       print("Entra gratis")
elif (edad>=16):
    print("Anda ahí, ahí")
    print("Me lo pienso")
else:
    print("Es menor de edad")
    print("Fuera")

#if notación compacta
if (edad>=MAYORIA_EDAD): print("Autorizado");print("Puedes pasar") #Notación en una sóla línea

#if notación ternaria
anyos_experiencia = 5
#if con notación 'normal'
if anyos_experiencia>4:
    salario1=20000
else:
    salario1=18000
print(salario1)
#if con notación ternaria
salario2 = 20000 if anyos_experiencia>4 else 18000
print(salario2)
#Pequeño ejercicio de ternaria
#Solicitar al usuario un nombre de fichero que incluye su extensión
#Crear una variable que tenga el valor "FICHERO PNG" si la extensión es .png
# o el valor "FICHERO JPG" si la extensión es .jpg
#Utilizar input, notación ternaria, slicing.
#(los ficheros tienen extensiones de 3 caracteres)
nombre_fichero = input("Introduce el nombre del fichero:")
x=nombre_fichero[-3:]
extension = "FICHERO PNG" if nombre_fichero[-3:]=="png" else ("FICHERO JPG" if nombre_fichero[-3:]=="jpg" else "EXTENSION DESCONOCIDA")
print(extension)
#while
contador=0
print("PRIMER BUCLE:",end="-")
while contador<10:
    print(contador,end="-")
    contador+=1
print("Final del bucle")

contador=0
print("SEGUNDO BUCLE (USA BREAK):",end="-")
while contador<10:
    print(contador,end="-")
    if (contador==5): 
        break
    contador+=1
print("Final del bucle")

contador=0
print("SEGUNDO BUCLE (USA CONTINUE):",end="-")
while contador<10:
    contador+=1
    if (contador==5): 
        continue
    print(contador,end="-")

print("Final del bucle")

#for
#Gracias la importación de las primeras líneas, disponemos de las lista dias_semana
for dia in dias_semana:
    print(dia)

for dia_laborable in dias_semana[:5]:
    print(dia_laborable)

"""
range(10) #Entre 0 y 10
range(1,10) #Entre 1 y 10
range(1,10,2) #Entre 1 y 10 de 2 en 2
"""
print("\nfor x in range(1,10,2):")
for x in range(1,10,2):
    print(x,end="--")

print("\nfor numero in range(0,100):")
for numero in range(0,100):
    print(numero,end="-")

print("\nfor numero in range(10,1,-1):")
for numero in range(10,1,-1):#OJO, QUE RECORRE DESDE 10 HASTA 2
    print(numero,end="-")

#CREACIÓN DE LISTAS CON BUCLE FOR -- LIST COMPREHENSION
#lista_numeros_pares = list(range(0,101,2))
lista_numeros_pares=[x for x in range(0,101,2)]#Una lista con los números pares entre 0 y 100
nueva_list_clientes=[cliente for cliente in clientes]#Creando una lista a partir de los elementos de otra 

#match
print("EJEMPLO DE MATCH")
edad=12
match edad:
    case 0:
        print("0")
    case 19:
        print("19")
    case 25:
        print("25")
    case _:
        print("Otra cosa")
    
#try
#with
