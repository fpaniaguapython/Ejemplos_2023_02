#Incorporando un diccionario para almacenar la relación entre las operaciones y las funciones

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
    operacion = input("Introduce la operacion (Sumar; Restar; Multiplicar; Dividir; Elevar):")
    
    #Pedir los operandos
    operando_1 = float(input("Introduce el primer operando:"))
    operando_2 = float(input("Introduce el segundo operando:"))

    #Hacer la llamada a la función:
    funciones_calculadora = {"Sumar":sumar, "Restar":restar, "Multiplicar":multiplicar, "Dividir":dividir, "Elevar":elevar}

    resultado = funciones_calculadora[operacion](operando_1, operando_2)
    print(resultado)
#Ha introducido un número de operación que no existe
except IndexError:
    print("La operación elegida no existe")
#Ha introducido una letra en lugar de un número en la selección de la operación 
#Ha introducido una letra en lugar de un número en alguno de los operandos
except ValueError:
    print("Ha introducido un valor no númerico")
    traceback.print_exc() #Muestra la traza del error
