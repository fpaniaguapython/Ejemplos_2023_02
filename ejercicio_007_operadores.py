"""
ARITMÉTICOS
+
-
*
/
// -> División entera
% -> Módulo o resto
** Exponencial
"""

"""
Solicitar al usuario utilizando la función input
dos números y le vamos a proporcionar el cociente
y el resto por separado.
"""
# dividendo = int(input("Introduce el dividendo:"))
# divisor = int(input("Introduce el divisor:"))
# cociente = dividendo // divisor
# resto = dividendo % divisor
# print("El cociente es",cociente,"y el resto es",resto)

"""
ARITMÉTICOS ABREVIADOS
+= -> Suma y asignación
-= -> Resta y asignación
*= -> Multiplicar y asignar
/= -> Dividir y asignar
//= -> Dividir (división entera) y asignar el cociente
%= -> Calcular el módulo y asignar
**= -> Elevar a potencia y asignar
"""
a=5
a=a+2 #Incrementar en 2 al valor de la variable a
a+=2 #Incrementar en 2 al valor de la variable a
a=a-1 #Decrementar en 2 el valor de la variable
a-=2 #Decrementar en 2 el valor de la variable
"""
OPERADORES LÓGICOS
== Igual
!= Distinto
> Mayor
>= Mayor o igual
< Menor 
<= Igual

and
or
not
"""

salario=5000
edad=21
numero_hijos=2
altura=170
peso=65
ciudad="Soria"

#Salario es mayor o igual que 5000
print(salario >= 5000)
#Salario es menor que 5000 o tiene hijos
print(salario < 5000 or numero_hijos > 0)
#Salario es menor que 5000, tiene hijos, pesa más de 80 kilos y mide menos de 160.
print(salario < 5000 and numero_hijos > 0 and peso > 80 and altura < 160)
#Vive en Zaragoza, pesa menos de 70 kilos, no tiene hijos, es mayor de edad y cobra más de 10000
print(ciudad=="Zaragoza" and peso<70 and numero_hijos==0 and edad>=18 and salario>1000)
#(No vive en Zaragoza ni en Madrid, pesa entre 60 y 70 kilos, no menos de 3 hijos, es mayor de edad) o cobra entre 10000 y 150000
print((ciudad!="Zaragoza" and ciudad!="Madrid" and peso>=60 and peso<=70 and numero_hijos>=3 and edad>=18) or (salario>=10000 and salario<=150000))
#Mejora de la condición anterior
vive_fuera = ciudad!="Zaragoza" and ciudad!="Madrid"
tiene_peso_medio = peso>=60 and peso<=70
es_mayor_edad=edad>=18
salario_en_rango=salario>=10000 and salario<=150000
print((vive_fuera and tiene_peso_medio and numero_hijos>=3 and es_mayor_edad) or (salario_en_rango))
print(vive_fuera and tiene_peso_medio and numero_hijos>=3 and es_mayor_edad or salario_en_rango)




