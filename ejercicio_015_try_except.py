#Ejercicio
#Existe un error que se produce cuando se divide un número entre 0
#1-Averiguar qué tipo de error es (nombre)
#2-Pedir al usuario dos números y a dividirlos. Si el divisor es 0, capturar
#la exception y volver a pedir otro par de números.
while True:
    try:
        dividendo = int(input("Introduce el dividendo:"))
        divisor = int(input("Introduce el divisor:"))
        resultado = dividendo/divisor
        print("El resultado es",resultado)
        break
    except ZeroDivisionError:
        print("El divisor no puede ser cero")
    except ValueError:
        print("El dividendo y el divisor deben ser números")