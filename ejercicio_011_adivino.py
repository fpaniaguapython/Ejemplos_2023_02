from random import randint
#Generar un número aleatorio enter 1-9
numero_secreto = randint(1,9)
"""
- Solicitar al usuario un número entre 1 y 9.
- Verificar si es o no es el número secreto.
- Si no es el número secreto, pedir un nuevo número hasta que acierte.
- Contar el número de intentos.
- Si acierta en 3 o menos intentos, es un adivino. Si no, es un impostor.
"""
#input, int, while
numero_intentos=1
numero_candidato = int(input("Introduce tu número candidato [1-9]:"))
while numero_candidato!=numero_secreto:
    print("Te has equivocado de número")
    numero_candidato = int(input("Introduce tu número candidato [1-9]:"))
    numero_intentos+=1
print("Has acertado")
if numero_intentos<=3:
    print("Eres un adivino de postín")
else:
    print("Eres un fraude de adivino")