from datetime import date

salario = 12000
if salario > 10000:
    print("Qué suerte tienes")
    print("Enhorabuena")
else:
    print("Busca otro empleo")
    print("Te mereces algo mejor")
print("Fin del programa")

#Ejercicio 
#Pedir al usuario su año de nacimiento
#Calcular su edad ()
#Indicarle al usuario si es o no mayor de edad
MAYORIA_EDAD=18
anyo_actual = date.today().year
anyo_nacimiento = int(input("Introduce tu año de nacimiento:"))
edad=anyo_actual-anyo_nacimiento
if edad>=MAYORIA_EDAD:
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")