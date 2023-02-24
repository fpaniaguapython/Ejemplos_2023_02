#Asignación múltiple
x,y=1,2
#Asignación a tupla
x*=1,2,3,4,5
print(x)
#Asignación a lista y a otro tipo
*x,nombre=1,2,3,4,"Lucía"
print(x)
print(nombre)
#Asignación a lista y a otros DOS tipos
*x,nombre,apellido=1,2,3,4,"Lucía","González"
print(x)
print(nombre,apellido)
#Asignación de otro tipo y lista
nombre,*x = "Carmen",1,2,3,4
print(nombre)
print(x)

