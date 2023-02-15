cadena = "Esto es una cadena $ 34"
#Inmutable
#Admite slicing
#Admite el uso con la función len
numero_caracteres = len(cadena)

# print, len, type, str, int, float, bin, ...

#Función input --> Obtiene la cadena de caracteres (str) introducida por teclado
nombre = input("Introduce tu nombre:")
edad = input("Introduce tu edad:")
edad = int(edad)
#Alternativamente podríamos hacer en una única línea edad = int(input("Introduce tu edad:"))
print(type(edad))

#Solicitar un nombre de fichero por pantalla y mostrarlo sustituyendo el . por #####
#Se debe utilizar SLICING, el parámetro sep de la función print y el método index de str
nombre_fichero = input("Introduce el nombre del fichero con su extensión:")
print("El nombre del fichero es:",nombre_fichero)
posicion = nombre_fichero.index(".")
izquierda = nombre_fichero[:posicion]
derecha = nombre_fichero[posicion+1:]
print(izquierda, derecha, sep="#####")
