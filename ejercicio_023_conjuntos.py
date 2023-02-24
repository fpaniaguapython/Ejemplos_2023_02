conjunto1 = {"Cosa1","Cosa2"}
conjunto2 = set()
print("Cosa1" in conjunto1)#True
print("Cosa3" not in conjunto1)#True
print("Cosa2" in conjunto2)#False

###########
#isdisjoint
###########
frutas_verano = {"Higo","Sandía","Melón"}
frutas_invierno = {"Uva","Manzana","Pera"}
frutas_entretiempo = {"Fresa","Plátano","Pera"}
print("¿No tienen en común (verano-invierno)?:",frutas_verano.isdisjoint(frutas_invierno))
print("¿No tienen en común (entretiempo-invierno)?:",frutas_entretiempo.isdisjoint(frutas_invierno))

palabras_prohibidas={"guerra","dolor","pobreza"}
#post = "mi deseo es que haya paz en el mundo y que no haya pobreza"#post prohibido
post = "mi deseo es que haya paz en el mundo y que no haya abundancia para todas las personas"#post permitido
palabras_introducidas=set(post.split())
if palabras_introducidas.isdisjoint(palabras_prohibidas):
    print("El post es correcto")
else:
    print("El post tiene palabras prohibidas")

###########
#intersection
###########
frutas_invierno = {"Uva","Manzana","Pera","Naranja","Mandarina"}
frutas_entretiempo = {"Naranja","Fresa","Plátano","Pera"}
conjunto_de_frutas_comunes = frutas_invierno.intersection(frutas_entretiempo)
print(f"Hemos encontrado {len(conjunto_de_frutas_comunes)} frutas comunes")#f-string
for fruta in conjunto_de_frutas_comunes:
    print("Común:",fruta)

###########
#difference
###########
frutas_invierno = {"Uva","Manzana","Pera","Naranja","Mandarina"}
frutas_entretiempo = {"Naranja","Fresa","Plátano","Pera"}

solo_invierno = frutas_invierno.difference(frutas_entretiempo)
solo_entretiempo = frutas_entretiempo.difference(frutas_invierno)

print("Solo invierno:", solo_invierno)#Uva, Manzana, Mandarina
print("Solo entretiempo:", solo_entretiempo)#Fresa, Plátano
