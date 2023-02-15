a = 5 #int
b = 5.1
c = "5"
d = "Cinco"
e = "5.1"

af = float(a)
bi = int(b) #Se admite, trunca los decimales
ci = int(c)
#di = int(d) #Error. No puede convertir "Cinco" a int
ei = int(float(e)) #Pasar "5.1" a int no es posible directamente
bs = str(b)

#función isinstance --> Determina si una instancia (variable, objeto) es de una clase determinada
print(isinstance(af,float))#True
print(isinstance(af,int))#False
