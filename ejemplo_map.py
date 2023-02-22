numeros=[3,4,5]

def doble(numero):
    return numero*2

def muestra_doble(numero):
    print(numero*2)

#Uso de map con función con retorno (for)
for i in map(doble, numeros):
    print(i)

#Uso de map con función con retorno (transformación a lista)
print(list(map(doble,numeros)))

#Uso de map con función sin retorno y sin transformación
for i in map(muestra_doble, numeros):
    pass

