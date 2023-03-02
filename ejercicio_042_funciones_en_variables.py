from time import sleep
#Asignación de una función a una variable
def funcion1(funcion):
    print("En función 1:")
    funcion()

def funcion2():
    print("F2")

x = funcion2 #Asignación de una función a una variable
x()
funcion1(x)

#Construcción de un flujo de trabajo con funciones
def calcular_importe():
    print("Calculando importe...")
    sleep(1)

def calcular_impuesto():
    print("Calculando impuesto...")
    sleep(1)

def calcular_factura():
    print("Calculando factura...")
    sleep(2)

def generar_pdf():
    print("Generando pdf...")
    sleep(0.5)

#Almacenamiento y ejecución de funciones
procesos = [calcular_importe, calcular_impuesto, calcular_factura, generar_pdf]

for proceso in procesos:
    proceso()