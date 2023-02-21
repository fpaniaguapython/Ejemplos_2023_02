#Limpiar el fichero de videojuegos de Atari
#Dada esta entrada: 3D-Asteroids--1987---Atari--la.PNG
#Generar esta salida: 3D Asteroids 1987 Atari

fichero = open("ficheros_atari7800.txt", "r", encoding="utf-8")
nombres_fichero=fichero.readlines()
fichero.close()

def limpiar_nombre(nombre):
    nombre = nombre[:-1].replace('a','@').upper()
    return nombre

nombres_fichero_limpios = [limpiar_nombre(nombre_fichero) for nombre_fichero in nombres_fichero]
for nombre_fichero in nombres_fichero_limpios:
    print(nombre_fichero)

#nombre.replace('-',' ') Reemplaza - por espacio en blanco
