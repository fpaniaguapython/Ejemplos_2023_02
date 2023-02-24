#FUNCIÓN sorted
#MÉTODO sort

numeros = [15,3,28]
numeros_ordenados = sorted(numeros)
print(type(numeros_ordenados))
print(numeros_ordenados)

clientes = [["Cristian",38,1000], ["Fernando",51,12000],["Alexander",28,25000]]
clientes_ordenados = sorted(clientes)
print(clientes_ordenados)

def ordenar(cliente):
    return cliente[2]

clientes_ordenados = sorted(clientes, key=ordenar)#la función sorted no modifica el original
print("CO:",clientes_ordenados)
clientes.sort(key=ordenar)#el método sort ordena la lista
print("CO2:", clientes)


#Utilizando la función sorted, ordenar los lenguajes por año y, en caso de sean iguales, por número de usuarios
#Python, PHP Ruby, Java
lenguajes_programacion = (("Python",1991,15000),("Java",1995,15000),("Ruby",1995,16000),("PHP",1994,8000))

#Solución Ángel
def ordenar_por_anio_y_usuarios(lenguaje):
    return (lenguaje[1], lenguaje[2])
lenguajes_ordenados = sorted(lenguajes_programacion, key=ordenar_por_anio_y_usuarios)
print(lenguajes_ordenados)

#Solución Miguel Ángel
def ordenar(item):
    anio = item[1]
    usuarios = item[2]
    return(anio*100000000 + usuarios)
lenguajes_ordenados = sorted(lenguajes_programacion, key=ordenar)
print(lenguajes_ordenados)