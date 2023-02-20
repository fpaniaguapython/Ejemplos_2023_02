dividendo = 5
divisor = 0
try:
    resultado = dividendo / divisor
    print("xx")
except ZeroDivisionError:
    print("División entre 0")
else:#Solo si no hay error en el bloque try
    print("Resultado:",resultado)
finally:#Se ejecuta siempre después del try-except
    print("Fin del proceso")
print("EL FINAL DE TODO")#Se ejecuta después del try-except PERO NO OBLIGATORIAMENTE
