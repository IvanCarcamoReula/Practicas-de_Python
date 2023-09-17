diccionario = {
    "nombre" : 'Ivan',
    "apellido" : 'Carcamo Reula',
    "subs" : 1000
}


#nos devuelve un elemento dict_item
claves = diccionario.keys()
#obteniendo un elementocon get() (si no encuentra nada el programa continua)
valor_de_ksdk = diccionario.get("ksdk")
print("hola papa, el programa continua")

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("nombre")

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()


print(diccionario_iterable)