nombre = "valor"
print(type(nombre)) #str

numero = 3
print(type(numero)) #int

otro_numero = 3.5
print(type(otro_numero)) #float

es_correcto = True
print(type(es_correcto)) #bool

#Los str son INMUTABLES
texto = "En un lugar de La Mancha, de cuyo nombre..."
texto.upper() # No modifica el valor de la variable texto
print("SIN REASIGNAR:", texto)
texto = texto.upper()
print("DESPUÉS DE REASIGNAR:", texto)

#Concatenación de string
cadena1 = "Hola"
espacio = " "
cadena2 = "a todos"
total = cadena1 + espacio + cadena2
print(total)

#total = cadena1 + numero + cadena2 #ERROR
#total = numero + cadena1 + numero #ERROR

total = cadena1 + str(numero) + cadena2
print(total)

anyo = 2023
nombre = "Python"
version = 3
espacio = " "
# ¿Cómo escribimos por pantalla '2023 Python 3' utilizando el operador +?
cadena = str(anyo) + espacio + nombre + espacio + str(version)
print(cadena)
# ¿Cómo escribimos por pantalla '2023 Python 3' sin utilizar el operador +?
print(anyo, nombre, version)

#Operador * está sobrecargado para str copiando n veces la cadena
cadena = "Esta es una cadena"
print(cadena*3)

#SLICING
#Camel Case
nombre_fichero = "saul.jpg"

#Otros tipos numéricos
decimal = 183 # 183 Dígitos 0-9
octal = 0o127 # 87 Dígitos 0-7
hexadecimal = 0x1A # 26 Dígitos 0-9,A,B,C,D,E,F
binario = 0b1000 # 8 Dígitos 0,1
print(decimal)
print(octal)
print(hexadecimal)
print(binario)

#Números decimales
"""
10.2
10.
.2
12e2 --> 1200 Equivalente a 12*10^2
12E2 --> 1200 Equivalente a 12*10^2
12e-3 --> 0.012 Equivalente a 12/1000
"""
