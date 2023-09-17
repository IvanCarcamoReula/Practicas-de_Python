#si el moudulo estuviera dentro de una carpeta en la misma ruta
#import funciones_buenas.saludar as m_saludar

import sys

sys.path.append('e:\\Documentos\\Desktop\\Ejercicios Python\\funciones_buenas')

import saludar as modulo_saludo
print(modulo_saludo.saludar("Ivan"))