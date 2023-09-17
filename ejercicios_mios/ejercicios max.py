#Definir una función max() que tome como 
#argumento dos números y devuelva el mayor de ellos.
#Es cierto que python tiene una función max() incorporada,
#pero hacerla nosotros mismos es un muy buen ejercicio.

def funcion_max(n1,n2):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    elif n2 == n1:
        print("los numeros son iguales")
    else:
        print("error")
        
print(funcion_max(88,30))

# Definir una función max_de_tres(),
# que tome tres números como argumentos
# y devuelva el mayor de ellos.

def funcion_max2(n1,n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    elif n3 > n1 and n3 > n2:
        return n3
    elif n2 == n1 == n3:
        print("los numeros son iguales")
    else:
        print("error")
        
print(funcion_max2(882,3000,120))