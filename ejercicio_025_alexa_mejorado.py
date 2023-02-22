#Proporcionar la hora
#Proporcionar los ingredientes de la tortilla de patatas (con cebolla)
#Proporcionar los ingredientes de un huevo frito
#En qué año se descubrió la penicilina
#Quién descubrió la penicilina

def mostrar_hora():
    print("Son las 18:15")

def mostrar_ingredientes_tortilla():
    print("Ingredientes de la tortilla")

def mostrar_ingredientes_huevo_frito():
    print("Ingredientes del huevo frito")

def mostrar_anyo_penicilina():
    print("1928")

def mostrar_descubridor_penicilina():
    print("Alexander Fleming")

tupla_funciones = (mostrar_hora, mostrar_ingredientes_tortilla, mostrar_ingredientes_huevo_frito, mostrar_anyo_penicilina, mostrar_descubridor_penicilina)

hora = {"qué","hora","es","dime","la","hora"}
tortilla = {"qué","ingredientes","tiene","la","tortilla","de","patatas","dime","la","tortilla","de","patatas","receta"}
huevo = {"qué","ingredientes","tiene","el","huevo","frito","cómo","se","hace","un", "huevo","frito","receta"}
anyo_penicilina = {"en","qué","año","se","descubrió","la","penicilina"}
descubridor_penicilina = {"quién","descubrió","la","penicilina"}
base_conocimiento = (hora, tortilla, huevo, anyo_penicilina, descubridor_penicilina)

pregunta = input("¿Qué deseas saber?")
#conjuntos, ¿tuplas?, método intersection de los conjuntos
palabras_clave = set(pregunta.split())

coincidencias = [len(palabras_clave.intersection(conocimiento)) for conocimiento in base_conocimiento]
maximo_coincidencias = max(coincidencias)
posicion_maximo = coincidencias.index(maximo_coincidencias)

if maximo_coincidencias==0:
    posicion_maximo=-1
    print("No entiendo la pregunta")
else:
    tupla_funciones[posicion_maximo]()






