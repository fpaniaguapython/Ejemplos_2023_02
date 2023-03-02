def dividir_enteros(dividendo, divisor):
    if not isinstance(dividendo, int) or not isinstance(divisor, int):
        raise TypeError("Los parámetros deben ser números enteros")
    if divisor==0:
        raise ValueError("El divisor no puede ser cero")
    return dividendo/divisor

try:
    resultado = dividir_enteros(0xF1,0b1010101)
    print(resultado)
except TypeError as te:
    print("Mensaje de la exception:", te)#Muestra el mensaje con el que se ha construido la exception
    print("Mensaje para el usuario:", "El tipo de los operandos debe ser entero")#Muestra MI mensaje
except ValueError as ve:
    print("Mensaje de la exception:", ve)#Muestra el mensaje con el que se ha construido la exception
    print("Mensaje para el usuario:", "El dividendo no puede ser cero")#Muestra MI mensaje