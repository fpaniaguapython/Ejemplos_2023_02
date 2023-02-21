#######################################################################
#Igual que el ejercicio 18 pero ignorando si es mayúsculas o minúsculas
#######################################################################

fichero = open("palabras_castellano_100.txt", "r", encoding="utf-8")
#contenido=fichero.read()#Lee todo el fichero
#contenido=fichero.readline()#Lee una línea
contenido=fichero.readlines()
print(contenido)
fichero.close()
#Limpiar el fichero de saltos de línea
palabras_limpias = [palabra[:-1].upper() for palabra in contenido]
print(palabras_limpias)
#Si la contraseña coincide con alguna palabra, se debe pedir otra hasta que no coincida
while True:
    #Pedir al usuario que introduzca una contraseña
    password = input("Introduce la contraseña:")
    #Comprobamos que la contraseña no se encuentra en el fichero
    if password.upper() not in palabras_limpias:
        print("La password es válida")
        break
    else:
        print("La password no es válida")