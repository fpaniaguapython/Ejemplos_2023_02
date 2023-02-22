tupla = ("Uno","Dos","Zaragoza","Tres")
print(tupla[1]) #Acceso por índice
print(tupla[0:1]) #Admite slicing
#tupla[1]="Two" #Error
lista = list(tupla)#Convierte tupla a lista
tupla = tuple(lista)#Convierte lista a tupla