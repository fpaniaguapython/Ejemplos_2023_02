from comunes import dias_semana
ingresos = [10000, 12000, 13000, 8000, 3000, 2000, 15000]
#Solución cutre
lista_ingresos = []
for indice in range(0,7):
    lista_ingresos.append((dias_semana[indice],ingresos[indice]))
print(lista_ingresos)
#Solución guay
lista_ingresos = list(zip(dias_semana, ingresos))
print(lista_ingresos)

#zip con tres elementos
numero_clientes = (3,8,9)
nombres_clientes = ("Javier","Saúl","Vanesa")
anyo_contratacion = [1999,2015,2018]
lista_clientes = list(zip(nombres_clientes, numero_clientes, anyo_contratacion))
print(lista_clientes)

#zip con tres elementos y ERROR detectado 
numero_clientes = (3,8,9)
nombres_clientes = ("Javier","Saúl","Vanesa","Ángel")
anyo_contratacion = [1999,2015,2018]
lista_clientes = list(zip(nombres_clientes, numero_clientes, anyo_contratacion, strict=True))
print(lista_clientes)