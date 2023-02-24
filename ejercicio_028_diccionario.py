#Creación
diccionario = {"Perro":"Dog","Gato":"Cat","Ratón":"Mouxe","Casa":"House","Naranja":"Orange"}

#Acceso por clave exitosa
print(diccionario["Ratón"])

#Acceso por clave inexistente --> GENERA ERROR
#print(diccionario[1])#Produce error si no existe la clave 1

#Acceso por clave inexistente --> NO GENERAR ERROR Y DEVUELVE NONE (o un valor por defecto)
traduccion = diccionario.get(input("Introduce una palabra:"))
if (traduccion==None):
    print("No existe esa palabra en nuestro diccionario")
else:
    print("La traducción de esa palabra es:",traduccion)

#Modificar un elemento
diccionario["Ratón"]="Mouse"
print(diccionario["Ratón"])

#Creación un elemento (inserción)
diccionario["Piña"]="Pineapple"

#Creación de elemento (solo si el elemento no existe)
diccionario.setdefault("Piña","Fruit")
print("setdefault:",diccionario["Piña"])
diccionario.setdefault("Sandía","Fruit")
print("setdefault:",diccionario["Sandía"])

#Eliminar con el operador del
del diccionario["Casa"]
print("Diccionario después de borrar casa:", diccionario)

#Eliminar de un elemento con obtención del valor -- método pop
gato_ingles = diccionario.pop("Gato")
print(gato_ingles)
print("Diccionario después de hacer pop de gato:", diccionario)

#Método pop con valor por defecto
elemento_inexistente = diccionario.pop("Frambuesa", "Inexistente")
print("Elemento inexistente:", elemento_inexistente)

#Elimina el último elemento del diccionario
print("Antes del popitem:", diccionario)
ultimo_elemento = diccionario.popitem()
print("Elemento obtenido con popitem:", ultimo_elemento)
print("Después del popitem:", diccionario)

#Recorrer todas las claves de un diccionario
for k in diccionario.keys():
    print("Clave:", k)

#Recorrer todos los valores de un diccionario
for v in diccionario.values():
    print("Valor:", v)

#Recorrer todos los elementos de un diccionario
for k,v in diccionario.items():
    print("Clave y valor:",k,v)

#Eliminar el contenido de un diccionario
print("Antes del clear:")
for k,v in diccionario.items():
    print("Clave y valor:",k,v)
diccionario.clear()
print("Después del clear:")
for k,v in diccionario.items():
    print("Clave y valor:",k,v)

#Construcción un diccionario a partir de dos iterables
claves = ("clave1","clave2","clave3","clave4") #tupla
valores = ["valor1","valor2","valor3","valor4"] #lista
claves_y_valores = zip(claves, valores)
nuevo_diccionario = dict(claves_y_valores)
print(nuevo_diccionario)



