#Convertir la primera letra de cada palabra de la lista a mayúsculas
#lista = ["uno","dos","tres"]

#Opción 1 (for)
#Solución Alexander
lista = ["uno","dos","tres"]
lista_resultado = []# o list()
for item in lista:
    lista_resultado.append(item.capitalize())
print(lista_resultado)
#Solución alternativa
lista = ["uno","dos","tres"]
for i in range(len(lista)):
    lista[i]=lista[i].capitalize()
print(lista)

#Opción 2 (comprensión de listas)
lista = ["uno","dos","tres"]
lista = [palabra.capitalize() for palabra in lista]
print(lista_resultado)

#Opción 3 (map)
lista = ["uno","dos","tres"]
def convertir_a_mayusculas(palabra):
    return palabra.capitalize()

#map(convertir_a_mayusculas, lista) --> Aplicar la función 'convertir_a_mayusculas' a cada elemento de la lista
lista_resultado = list(map(convertir_a_mayusculas, lista))
print(lista_resultado)


######
#CASO DE USO DE FUNCIÓN MAP
######
def enviar_email_a_moroso(moroso):
    asunto ="Debes dinero"
    email_from = "clientes@miempresa.com"
    email_to = moroso[2]
    texto_mensaje = f"Estimado {moroso[0]}, te recordamos que debes {moroso[1]}€ a mi empresa. Paga."
    print("Enviando mensaje:",asunto, email_from, email_to, texto_mensaje)
    return(texto_mensaje)

clientes = (["Javier",10000,"javier@hotmail.com"],["Alexander",5000,"alex@telefonica.net"],["Victor",3000,"victor@yahoo.es"])
list(map(enviar_email_a_moroso, clientes))#map no ejecuta la función hasta que no se itera por sus elementos