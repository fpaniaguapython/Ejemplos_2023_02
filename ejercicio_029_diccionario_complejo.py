"""
Cliente:
- Id
- Nombre
- Edad
- Facturacion
"""
#1,Cristian,38,10000
#2,Fernando,51,12000
#3,Alexander,28,25000
clientes = {
    1:["Cristian",38,1000],
    2:["Fernando",51,12000],
    3:["Alexander",28,25000]
    }

#1. Pedir al usuario un identificador de cliente y mostrar su nombre y saldo. Mostrar el diccionario con un for.
id_cliente = int(input("Introduce identificador de cliente para consultar su nombre y saldo:"))
print(clientes[id_cliente][0]+":",(clientes[id_cliente][2]))
for k,v in clientes.items():
    print(k,v)

#2. Pedir al usuario un identificador de cliente e incrementar su saldo en 1000. Mostrar el diccionario con un for.
id_cliente = int(input("Introduce el identificador de cliente a incrementar saldo:"))
clientes[id_cliente][2]+=10000
for k,v in clientes.items():
    print(k,v)

#3. Pedir al usuario un identificador de cliente. 
# Comprobar que existe. Si no existe, pedir un nuevo cliente. 
# Si existe, preguntar si lo quiere borrar y borrar si confirma.
while True:
    id_cliente = int(input("Introduce el identificador de cliente a borrar:"))
    if id_cliente in clientes:
        confirmacion = input("¿Desea borrar cliente S/N?")
        if (confirmacion=="S"):
            del clientes[id_cliente]
            print("El cliente ha sido borrado")
            break
        else:
            print("Operación cancelada")
    else:
        print("El cliente no existe")

for k,v in clientes.items():
    print(k,v)

#4. Utilizando la función max, obtener el nombre del cliente que más has facturado.
clientes = {
    1:["Cristian",38,1000],
    2:["Fernando",51,12000],
    3:["Vanesa",30,45000],
    4:["Alexander",28,25000]
    }

def obtener_facturacion(cliente):
    return cliente[2]

lista = [clientes[k][2] for k in clientes.keys()]

cliente_vip = max(clientes.values(), key=obtener_facturacion)
print("El nombre del cliente con más facturación es", cliente_vip)

#5. Dado el nombre del cliente con más facturación, obtener el id
clave_cliente_vip = [k for k,v in clientes.items() if v[0]==cliente_vip[0]]
print(clave_cliente_vip[0])#El primer elemento