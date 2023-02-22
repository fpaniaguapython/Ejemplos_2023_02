# Proporcionar la hora
# Proporcionar los ingredientes de la tortilla de patatas (con cebolla)
# Proporcionar los ingredientes de un huevo frito
# En qué año se descubrió la penicilina
# Quién descubrió la penicilina
def mostrar_hora():
    print("Son las 18:15")
def mostrar_ingredientes_tortilla():
    print("Ingredientes de la tortilla")
def mostrar_ingredientes_huevos():
    print("Los huevos llevan huevos jajajaja")

hora = {"qué", "hora", "es", "dime", "la", "hora"}

tortilla = {"qué", "ingredientes", "tiene", "la", "tortilla",
            "de", "patatas", "dime", "la", "tortilla", "de", "patatas"}

huevos = {"como", "hacer", "huevos", "fritos",
          "dime ", "como", "hago", "huevos", "fritos"}

pregunta = input("¿Qué deseas saber? ")
pregunta = set(pregunta.split())

# Hora
coincidencia_hora = hora.intersection(pregunta)
cantidad_hora = len(coincidencia_hora)

# Tortilla
coincidencia_tortilla = tortilla.intersection(pregunta)
cantidad_tortilla = len(coincidencia_tortilla)

# Huevos frito
coincidencia_huevos = huevos.intersection(pregunta)
cantidad_huevos = len(coincidencia_huevos)

mayor_que = 0
funcion = ''

respuestas = [['hora', cantidad_hora], ['tortilla',cantidad_tortilla], ['huevos', cantidad_huevos]]
for respuesta in respuestas:
    if (int(respuesta[1]) > mayor_que):
        mayor_que = respuesta[1]
        funcion = respuesta[0]
match funcion:
    case 'hora':
        mostrar_hora()
    case 'tortilla':
        mostrar_ingredientes_tortilla()
    case 'huevos':
        mostrar_ingredientes_huevos()
    case _:  # deafult otra cosa
        print("No te entiendo")