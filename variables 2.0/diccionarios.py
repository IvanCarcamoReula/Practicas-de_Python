#creando diccionarios con dict()
diccionario = dict(nombre="Ivan",apellido="Carcamo")

#las listas no pueden ser claves
diccionario = {frozenset(["Ivan", "rancio"]): "jajajaj"}

#creando diccionario con fromkeys() valor por defecto: none
diccionario = dict.fromkeys(["nombre","apellido"])

#creando diccionario con fromkeys() cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre","apellido"], "no se")

print(diccionario)