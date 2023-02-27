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
    operacion = int(input("Introduce la operacion (1-Sumar; 2-Restar; 3-Multiplicar; 4-Dividir; 5-Elevar):"))
    
    #Pedir los operandos
    operando_1 = float(input("Introduce el primer operando:"))
    operando_2 = float(input("Introduce el segundo operando:"))

    #Hacer la llamada a la función:
    funciones_calculadora = (sumar, restar, multiplicar, dividir, elevar)

    resultado = funciones_calculadora[operacion-1](operando_1, operando_2)
    print(resultado)
#Ha introducido un número de operación que no existe
except IndexError:
    print("La operación elegida no existe")
#Ha introducido una letra en lugar de un número en la selección de la operación 
#Ha introducido una letra en lugar de un número en alguno de los operandos
except ValueError:
    print("Ha introducido un valor no númerico")
    traceback.print_exc() #Muestra la traza del error
