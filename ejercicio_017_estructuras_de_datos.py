#Crear una lista de la compra con tres productos
cesta = ["Brócoli","Huevos","Gaseosa"]
print(cesta)
#Solicitar al usuario un producto y agregarlo a la lista
nuevo_producto = input("Introduce nuevo producto:")
cesta.append(nuevo_producto)
print(cesta)
#Ordenar la lista
cesta.sort()
print(cesta)
#Mostrar el contenido de la lista
for producto in cesta:
    print("Producto:",producto)
#Solicitar al usuario un producto e indicar si está o no está en la lista
producto_buscado = input("Introduce el nombre del producto a buscar:")
if producto_buscado in cesta:
    print("El producto",producto_buscado,"se encuentra en la cesta")
else:
    print(f"El producto {producto_buscado} no se encuentra en la cesta")#Utilizando f-string
#Solicitar al usuario un producto (que esté en la lista) y eliminarlo de la lista
producto_buscado = input("Introduce el nombre del producto a eliminar:")
cesta.remove(producto_buscado)
print(cesta)
#Solicitar al usuario un producto e insertarlo en el centro de la lista
posicion_central = len(cesta)//2
nuevo_producto = input("Introduce el nombre del producto a insertar en el medio:")
cesta.insert(posicion_central, nuevo_producto)
print(cesta)
#Solicitar al usuario un producto existente para sustituirlo por otro
producto_a_reemplazar = input("Introduce el nombre del producto a reemplazar:")
producto_reemplazo = input("Introduce el nombre del producto de reemplazo:")
cesta[cesta.index(producto_a_reemplazar)]=producto_reemplazo
print(cesta)