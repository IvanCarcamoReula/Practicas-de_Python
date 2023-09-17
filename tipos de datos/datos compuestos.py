#creando una lista (se pueden modificar)
lista = ["Ivan", "Carcamo Reula", True, 1.85]


#creando una tupla (no se pueden modificar)
tupla = ("Ivan", "Carcamo Reula", True, 1.85)


#esto es valido
lista [3] =  "Maquinola"

#esto no
#tupla[3] = "Maquinola"


#creando un conjunto (set) (no se accede a elementos por indice, no almacena datos duplicados)
conjunto = {"Ivan", "Carcamo Reula", True, 1.85}

#print(conjunto[3]) -> no se puede acceder al elemento


#creando un diccionario (dict) (la estructura es key : valor y separamos con comas)
diccionario = {
    'nombre' : 'Ivan',
    'apellido' : 'Carcamo Reula',
    'esta emocionado' : True,
    'altura' : 1.75,
    'dato duplicado' : "Carcamo Reula"    
}

print(diccionario['nombre'])