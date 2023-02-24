numeros=[3,4,5]

def doble(numero):
    return numero*2

def muestra_doble(numero):
    print("muestra_doble:",numero*2)

#Uso de map con función con retorno (for)
for numero_doble in map(doble, numeros):
    print(numero_doble)

#Uso de map con función con retorno (transformación a lista)
lista_numeros_doble = list(map(doble,numeros))
print(lista_numeros_doble)

#Uso de map con función sin retorno y sin transformación
for valor_sin_uso in map(muestra_doble, numeros):
    pass

