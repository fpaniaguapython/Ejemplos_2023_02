#Agregar dinamicamente una ruta al path para que encuentre un módulo
import sys
sys.path.append("F:/modulos_python") #Agregar dinamicamente una ruta al path de Python
from generador import generar_uno
print(generar_uno())