with open("datos_factura.txt","r",encoding="utf-8") as fichero:
    items = fichero.readlines()
items = [item[0:-1]   for item in items]
for item in items:
    partes = item.split("$")
    supplier_data = dict() #o podemos crear el diccionario supplier_data = {}
    client_data = dict()
    item_list = list()
    
    elementos = partes[0].split("#")
    supplier_data["nombre"]=elementos[0]
    supplier_data["direccion"]=elementos[1]
    supplier_data["email"]=elementos[2]
    supplier_data["cif"]=elementos[3]

    elementos = partes[1].split("#")
    client_data["nombre"]=elementos[0]
    client_data["direccion"]=elementos[1]
    client_data["email"]=elementos[2]
    client_data["cif"]=elementos[3]

    elementos = partes[2].split("#")
    for producto in elementos:
        partes_producto = producto.split(",")
        producto_facturable = (partes_producto[0], partes_producto[1],partes_producto[2])
        item_list.append(producto_facturable)
    print(supplier_data)
    print(client_data)
    print(item_list)
