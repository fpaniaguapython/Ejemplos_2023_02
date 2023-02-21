# Crear una lista de la compra con tres productos
cesta = ["Brócoli", "Huevos", "Gaseosa"]
print(cesta)
# Solicitar al usuario un producto y agregarlo a la lista
nuevo = input("Introduzca el producto a agregar: ")
list.append(cesta, nuevo) #Se podría sustituir por cesta.append(nuevo)
print(cesta)
# Ordenar la lista
list.sort(cesta) #Se podría sustituir por cesta.sort()
# Mostrar el contenido de la lista
print(cesta)
# Solicitar al usuario un producto e indicar si está o no está en la lista
verif = input("Introduzca el producto a verificar: ")
if verif in cesta:
    print("Producto ya está en cesta")
else:
    print("Producto NO está en cesta")
# Solicitar al usuario un producto (que esté en la lista) y eliminarlo de la lista
elim = input("Introduzca el producto a eliminar: ")
list.remove(cesta, elim) #Se podría sustituir por cesta.remove(elim)
print(cesta)
# Solicitar al usuario un producto e insertarlo en el centro de la lista
inser = input("Introduzca el producto a añadir en medio: ")
pos = len(cesta)//2
cesta.insert(pos, inser)
print(cesta)
#Solicitar al usuario un producto existente para sustituirlo por otro
exist=input("Introduzca el producto existente a sustituir: ")
sustituto=input("Introduzca el producto sustituto: ")
pos_exist=cesta.index(exist)
#Opción Javier
cesta.remove(exist)
cesta.insert(pos_exist,sustituto)
#Opción Fernando
#cesta[pos_exist]=sustituto
print(cesta)