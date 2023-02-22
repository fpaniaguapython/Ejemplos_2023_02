#Uso de la función max con el comportamiento por defecto
lista = [1,3,8,150,4,1]
print(max(lista))

lista = ["Pila","Pendrive","Funda"]
print(max(lista))

#Uso de la función max indicando cómo calcular el tamaño
def calcular_tamanyo(cadena):
    return len(cadena)

print(max(lista, key=calcular_tamanyo))

#Uso de la función max indicando como calcular el tamaño a partir una lista de tuplas
def funcion3():
    print("F3")
def funcion4():
    print("F4")
def funcion8():
    print("F8")

def calcular_size(elemento):
    return elemento[0]

lista = [(4,funcion4),(8,funcion8),(3,funcion3)]
mayor = max(lista, key=calcular_size)
mayor[1]()