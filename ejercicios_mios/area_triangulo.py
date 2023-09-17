print("Ingrese los valores del triangulo: ")# Pido al usuario que ingrese los valores del triangulo

base = input("Base: ")# Ingreso del valor 1
altura = input("Altura: ")# Ingreso del valor 2

# Transformo los valores a enteros
base = int(base)
altura = int(altura)

# Calculo el area
area = (base * altura) / 2

# Imprimo el valor
print(f"El area del triángulo es de {area} metros cuadrados según los valores dados")