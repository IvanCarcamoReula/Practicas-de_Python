#forma no optima de sumar valores
#def suma (lista):
#    numeros_sumados = 0
#    for numero in lista:
#        numeros_sumados = numeros_sumados + numero    
#    return numeros_sumados

#resultado = suma ([55,3,9,5,98,45,32])

#forma optima de sumar valores
def suma_total (numeros): 
    return sum ([*numeros])

resultado2 = suma_total([55,3,9,5,98,45,32])


#lo mismo que arriba pero utilizando el operador * como argumento (*args)
def suma(nombre,*numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"

resultado = suma ("Ivan",4,5,6,7)


