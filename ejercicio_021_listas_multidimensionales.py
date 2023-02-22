lista = [["Menaje","Sartén"],["Textil","Camiseta"],["Alimentación","Azúcar"],["Textil","Pantalón"]]
print(lista[1][1])

for categoria in lista:
    for item in categoria:
        print("Item:",item)