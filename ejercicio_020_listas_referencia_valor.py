from comunes import dias_semana

#Cambiar el Viernes de dias_semana por Biernes (asignación por referencia)
los_dias = dias_semana

print("LOS DIAS:", los_dias)
print("LOS DIAS DE LA SEMANA:", dias_semana)
#Al haberse asignado por referencia, el cambio afecta a las dos listas
dias_semana[4]="Biernes"
print("LOS DIAS:", los_dias)
print("LOS DIAS DE LA SEMANA:", dias_semana)

#Cambiar el Jueves de dias_semana por Juebes (asignación por copia)
los_dias = dias_semana[:]
dias_semana[3]="Juebes"
print("LOS DIAS:", los_dias)
print("LOS DIAS DE LA SEMANA:", dias_semana)