try:
    dividendo = int(input("Dividendo:"))
    divisor = int(input("Divisor:"))
    resultado = dividendo / divisor
except ArithmeticError:
    print("Error aritmético (probablemente división entre 0)")
else:
    print(resultado)
