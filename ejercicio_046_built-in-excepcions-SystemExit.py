import sys

try:
    while(True):
        print("1. Saludar")
        print("2. Despedir")
        print("0. Salir")
        opcion=int(input("Introduce una opción:"))
        if opcion==1:
            print("Hola")
        elif opcion==2:
            print("Hasta mañana")
        elif opcion==0:
            sys.exit(-1)    
        else:
            print("No entiendo")
    else:
        print("Fin del bucle while") #Código muerto
except SystemExit as se:#El objeto se contiene el código del sys.exit
    print("La aplicación por llamar sys.exit con el código:",se)