######################
#else aplicado a while
######################
numero_secreto = 8
numero_candidato = int(input("Introduce un número entre 1 y 9:"))
numero_intentos = 1
while (numero_candidato!=numero_secreto):
    print("No has acertado en este intento")
    if (numero_intentos==3):
        print("No has acertado el número secreto en el total de intentos")
        break 
    numero_candidato = int(input("Introduce un número entre 1 y 9:"))
    numero_intentos+=1
else:
    #Sólo se ejecuta cuando la condición del while ha dejado de cumplirse.
    print("Has acertado el número secreto")
print("Fin de la ejecución")
######################
#else aplicado a for
######################
numero_secreto = 8
for numero_intentos in range(3):#0,1,2
    numero_candidato = int(input("Introduce un número entre 1 y 9:"))
    if (numero_candidato==numero_secreto):
        print("Has acertado el número secreto")
        break    
    else:
        print("No has acertado el número secreto")
else:
    #Sólo se ejecuta cuando el bucle se haya ejecutado completamente
    print("No has acertado el número secreto en el total de intentos")
print("Fin de la ejecución")



