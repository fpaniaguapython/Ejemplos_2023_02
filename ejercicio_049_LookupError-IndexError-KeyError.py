lista = [1,2,3]
diccionario = {1:"Uno",2:"Dos",3:"Tres"}

try:
    print(lista[5])
except IndexError:
    print("No existe esa posición en la lista")

try:
    print(diccionario[5])
except KeyError:
    print("No existe esa entrada en el diccionario")


#El primero que de el error hace saltar al except
try:
    print(lista[5])
    print(diccionario[5])
except LookupError as le:#La clase base de IndexError y KeyError
    print("Estás intentando acceder a un elemento inexistente:", le)