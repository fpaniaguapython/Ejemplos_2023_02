def get_invoice_data():
    #Creamos la lista de datos de facturación
    invoices_data = list()

    #Leer todas las líneas del fichero
    with open("datos_factura.txt","r",encoding="utf-8") as fichero:
        items = fichero.readlines()

    #Eliminar los saltos de línea
    items = [item[0:-1] for item in items]

    #Recorrer cada línea que está formada por el proveedor, el cliente y los productos (usando $ como separador)
    for item in items:
        #Hacemos el split de las partes 
        partes = item.split("$")

        #Construimos las estructuras de datos
        supplier_data = dict() #o podemos crear el diccionario supplier_data = {}
        client_data = dict()
        item_list = list()
        
        #Proveedor
        elementos = partes[0].split("#")
        supplier_data["nombre"]=elementos[0]
        supplier_data["direccion"]=elementos[1]
        supplier_data["email"]=elementos[2]
        supplier_data["cif"]=elementos[3]

        #Cliente
        elementos = partes[1].split("#")
        client_data["nombre"]=elementos[0]
        client_data["direccion"]=elementos[1]
        client_data["email"]=elementos[2]
        client_data["cif"]=elementos[3]

        #Productos de facturación
        productos = partes[2].split("#")
        for producto in productos:
            partes_producto = producto.split(",")
            producto_facturable = (partes_producto[0], float(partes_producto[1]),float(partes_producto[2]))
            item_list.append(producto_facturable)
        
        invoices_data.append((supplier_data,client_data,item_list))
    
    #Devolvemos los datos de las facturas leídas del fichero
    return invoices_data