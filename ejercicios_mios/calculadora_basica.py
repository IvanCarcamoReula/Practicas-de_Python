#Ejercicio: Crear una calculadora básica en Python

#Crea un programa en Python que permita al
# usuario realizar operaciones matemáticas básicas como suma,
# resta, multiplicación y división.
# Tu programa debe solicitar al usuario que ingrese dos números
# y la operación que desea realizar. Luego, debe imprimir el resultado de la operación.


"""numero1 = input("dame el primer numero: ") #Pide al usuario el primer numero

numero2 = input("dame el segundo numero: ") #Pide al usuario el segundo numero

numero1 = int(numero1)#Transforma el numero 1 a entero
numero2 = int(numero2)#Transforma el segundo numero a entero

operacion = input("elije una operacion: ") #Pide al usuario que elija el numero de la operacion

operacion = int(operacion)#Transforma el numero de la operacion a entero

#Si el numero es igual a 1 suma, igual a 2 resta igual a 3 multiplica, igual a 4 divide
#Si no se elijio un numero de operacion indicado da un aviso
if operacion == 1:
    resultado = numero1 + numero2
    print(resultado)
elif operacion == 2:
    resultado = numero1 - numero2
    print(resultado)
elif operacion == 3:
    resultado = numero1 * numero2
    print(resultado)
elif operacion == 4:
    resultado = numero1 / numero2
    print(resultado)
else: 
    print("No ha seleccionado una operacion compatible")
    """
    
    
    
    
    
numero1 = input("dame el primer numero: ") #Pide al usuario el primer numero

operacion = input("elije una operacion: ") #Pide al usuario que elija la operacion

numero2 = input("dame el segundo numero: ") #Pide al usuario el segundo numero

numero1 = int(numero1)#Transforma el numero 1 a entero
numero2 = int(numero2)#Transforma el segundo numero a entero


#Si se elijio el simbolo es "+" suma, "-" resta, "*" multiplica, "/" divide
#Si no se elijio un numero de operacion indicado da un aviso



if operacion == "+":
    resultado = numero1 + numero2
    print(resultado)
elif operacion == "-":
    resultado = numero1 - numero2
    print(resultado)
elif operacion == "*":
    resultado = numero1 * numero2
    print(resultado)
elif operacion == "/":
    resultado = numero1 / numero2
    print(resultado)
else: 
    print("No ha seleccionado una operacion compatible")
