#Incorporando el uso de la función eval para ejecutar las funciones a partir de cadenas

import traceback #Para obtener la traza de ejecución

def sumar(operando_1:float, operando_2:float) -> float :
    return operando_1+operando_2
    
def restar(operando_1:float, operando_2:float) -> float :
    return operando_1-operando_2
    
def multiplicar(operando_1, operando_2):
    return operando_1*operando_2
    
def dividir(operando_1, operando_2):
    return operando_1/operando_2

def elevar(operando_1, operando_2):
    return operando_1**operando_2

try:
    #Pedir al usuario qué operación quiere realizar
    operacion = input("Introduce la operacion (sumar; restar; multiplicar; dividir; elevar):")
    
    #Pedir los operandos
    operando_1 = float(input("Introduce el primer operando:"))
    operando_2 = float(input("Introduce el segundo operando:"))

    #Hacer la llamada a la función:
    cadena_operacion = operacion + "(" + str(operando_1) + "," + str(operando_2) + ")"#p.e. sumar(3,2) de tipo str
    #cadena_operacion = f"{operacion}({operando_1},{operando_2})" #Lo mismo, con f-string
    resultado = eval(cadena_operacion)
    print(resultado)
#Ha introducido un número de operación que no existe
except IndexError:
    print("La operación elegida no existe")
#Ha introducido una letra en lugar de un número en la selección de la operación 
#Ha introducido una letra en lugar de un número en alguno de los operandos
except ValueError:
    print("Ha introducido un valor no númerico")
    traceback.print_exc() #Muestra la traza del error
