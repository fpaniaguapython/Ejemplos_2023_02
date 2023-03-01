edad = 10

def funcion1():
    print("Función 1")
    print("F1:", edad)#Muestra la variable global (10)
    pass

def funcion2():
    print("Función 2")
    edad = 20#Aquí la asignación es una declaración local + asignación
    print("F2:", edad)#Muestra la variable local (20)
    pass

def funcion3():
    print("Función 3")
    global edad #Indicamos a Python que utilice la variable edad del ámbito global
    edad = 30#Aquí la asignación se hace sobre la variable global
    print("F3:", edad)#Muestra la variable global (30)
    pass

def funcion4():
    print("Función 4")
    edad = edad + 10 #Produce un error

def funcion5():
    global x #Al no existir en el ámbito global, la crea en dicho ámbito
    x=5
    
funcion1()
print("Después de ejecutar funcion1:",edad)#Muestra la variable global (10)
funcion2()
print("Después de ejecutar funcion2:",edad)#Muestra la variable global (10)
funcion3()
print("Después de ejecutar funcion3:",edad)#Muestra la variable global (30)
#funcion4() #Produce un error
funcion5()
print("Después de ejecutar funcion5:", x)#Muestra la variable declarada global en la propia función (5)
