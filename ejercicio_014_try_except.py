lista = ['Cero', 'Uno', 'Dos']
#Tratamiento genérico
try:
    i = int(input("Introduce un número entre 0 y 2:"))#ValueError
    print(lista[i])#IndexError
except:
    print("Ha ocurrido un error")

#Tratamiento genérico (con BaseException)
try:
    i = int(input("Introduce un número entre 0 y 2:"))#ValueError
    print(lista[i])#IndexError
except BaseException:
    print("Ha ocurrido un error:")

#Tratamiento específico
print("Programa de gestión de números")
try:
    i = int(input("Introduce un número entre 0 y 2:"))#ValueError
    print(lista[i])#IndexError
    print("Esta línea se ejecuta solo si no ha ocurrido ningún error antes")
except ValueError:
    print("Ha ocurrido un error: debes introducir un dígito numérico")
except IndexError:
    print("Ha ocurrido un error: debes introducir un número entero entre 0 y 2")
except BaseException:
    print("Ha ocurrido un error desconocido. Contacte el administrador.")

