#creando una funcion de 3 parametros
#def frase(nombre, apellido, adjetivo):
#   return f'Hola {nombre} {apellido}, sos muy {adjetivo}'

#utilizando keyword arguments
#frase_resultante = frase(adjetivo = "Capo",nombre="Ivan", apellido="Carcamo Reula")

#print(frase_resultante)

#la misma funcion con un parametro opcional y un valor por defecto
def frase(nombre, apellido, adjetivo = "tonto"):
   return f'Hola {nombre} {apellido}, sos muy {adjetivo}'

frase_resultante = frase("Ivan", "Carcamo Reula",adjetivo="inteligente")
print(frase_resultante)