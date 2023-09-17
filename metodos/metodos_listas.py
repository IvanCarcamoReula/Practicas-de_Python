#creando una lista con list
lista = list ([5415,True,34])

#devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#agregando un elemento a la lista con append
lista.append("jajajajaja")

#agregando un elemento a la lista en un indice especifico
lista.insert(2,"toma mama")

#agregando varios elementos a la lista
lista.extend([False,887])

#eliminando un elemento de la lista (por su indice)
lista.pop(2) #-1 para eliminar el ultimo, -2 para eliminar el anteultimo, y asi sucesivamente

#removiendo un elemento de la lista por su valor
lista.remove("jajajajaja")

#eliminando todos los elementos de la lista
#lista.clear()

#ordenando la lista de forma ascendente (si usamos reverseTrue la ordena en reversa)
lista.sort()

#invirtiendo los elementos de una lista
lista.reverse()

#verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(34)

print(lista)