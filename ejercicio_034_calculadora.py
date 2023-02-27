#Crear una calculadora que implemente en funciones
#las operaciones:
#- sumar, restar, dividir, multiplicar, potencia
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

#Pedir al usuario qué operación quiere realizar
operacion = input("Introduce la operacion (1-Sumar; 2-Restar; 3-Multiplicar; 4-Dividir; 5-Elevar):")
#Pedir los operandos
operando_1 = float(input("Introduce el primer operando:"))
operando_2 = float(input("Introduce el primer operando:"))

"""
######################
#Solución de Alexander
######################
#Hacer la llamada a la función:
resultado = None
match operacion:
    case "1":
        resultado = sumar(operando_1, operando_2)
    case "2":
        resultado = restar(operando_1, operando_2)
    case "3":
        resultado = multiplicar(operando_1, operando_2)
    case "4":
        resultado = dividir(operando_1, operando_2)
    case "5":
        resultado = elevar(operando_1, operando_2)
    case _:
        print("Hay un error en la selección de la operación")
if resultado!=None:
    print(resultado)
"""

##################### 
#Solución de Fernando
#####################
#Hacer la llamada a la función:
match operacion:
    case "1":
        resultado = sumar(operando_1, operando_2)
    case "2":
        resultado = restar(operando_1, operando_2)
    case "3":
        resultado = multiplicar(operando_1, operando_2)
    case "4":
        resultado = dividir(operando_1, operando_2)
    case "5":
        resultado = elevar(operando_1, operando_2)

try:
    print(resultado)
except NameError:
    print("La operación no se ha podido realizar")