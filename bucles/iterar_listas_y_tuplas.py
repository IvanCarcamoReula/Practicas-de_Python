animales = ["gato", "perro", "loro", "cocodrilo"]
numeros = []

#recorriendo la lista animales
for animal in animales:
    print(f"Ahora la variable animal es igual a: {animal}")
  
#recorriendo la lista numeors y multiplicando con valor por 10  
for numero in numeros:
    resultado = numero * 10
    print(resultado)
    

#iterando 2 listas del mismo tamaño al mismo tiempo
for numero,animal in zip(animales,numeros):
    print(f"recorriendo lista1: {numero}")
    print(f"recorriendo lista 2: {animal}")
    


#forma no optima de recorrer una lista(no funciona en conjuntos)
for num in range(len(numeros)):
    print(numeros[num])
    
    
    
#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice es: {indice} y el valor ess: {valor}")
    
    
#usando el for/else
for nnumero in numeros:
    print(f"ejecutando el untimo bucle, valor actual: {numero}")
else:
    print("el bucle termino")
    
#todo lo anterior funciona exactamente igual para tuplas y conjuntos