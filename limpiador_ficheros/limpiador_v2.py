#Limpiar el fichero de videojuegos de Atari
#Dada esta entrada: 3D-Asteroids--1987---Atari--la.PNG
#Generar esta salida: 3D Asteroids 1987 Atari

fichero = open("ficheros_atari7800.txt", "r", encoding="utf-8")
nombres_fichero=fichero.readlines()
fichero.close()

def limpiar_nombre(nombre_original):
    nombre=nombre_original

    #Alternativamente a la solucion limpiador.py aquí se utilizan listas y bucles para no duplicar código    
    lista_cadenas_inutiles = ["--la","--USA"]
    for cadena_inutil in lista_cadenas_inutiles:
        posicion_cadena_inutil = nombre.find(cadena_inutil)
        if posicion_cadena_inutil!=-1:
            nombre=nombre[:posicion_cadena_inutil]
    
    nombre = nombre.replace("-"," ")
    while nombre.find("  ")!=-1:
        nombre = nombre.replace("  "," ")
    #NOTA: nombre = " ".join(nombre.replace('-',' ').split()) reemplaza todos los guiones, incluso duplicados, por un espacio
    return nombre

nombres_fichero_limpios = [limpiar_nombre(nombre_fichero) for nombre_fichero in nombres_fichero]

#SALIDA, POR CADA UNO DE LOS REGISTROS:
# {"title":"1000cc Turbo","image":"1000ccTurbo_v1.0.jpg"},

#Fichero de escritura con "w"
fichero_salida = open("atari7800.json", "w", encoding="utf-8")
#Disponemos de nombres_fichero_limpios y nombres_fichero
info_videojuegos = list(zip(nombres_fichero_limpios, nombres_fichero))
fichero_salida.write("[")
for videojuego in info_videojuegos:
    fichero_salida.write("{\"title\":\""+videojuego[0]+"\",\"image\":\""+videojuego[1][:-1]+"\"}")
    if (videojuego[0]!=info_videojuegos[len(info_videojuegos)-1][0]):
        fichero_salida.write(",\n")
fichero_salida.write("]")
fichero_salida.close()

