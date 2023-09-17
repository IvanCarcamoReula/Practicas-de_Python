#creando una funcion simple
#def saludar():
#    print("Hola Ivan, mi maestro ¿Como andas?")

#  ejecutando una funcion simple
#saludar()



#crear una funcion que tenga parametros
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == 'mujer'):
        adjetivo = 'reina'
    elif(sexo == 'hombre'):
        adjetivo = 'titan'
    print(f"Hola {nombre}, mi {adjetivo} ¿como andas?")
    
saludar("ivan","hombre")

#crear una funcion que nos retorne valores
def crear_contraseña_random(num):
    chars = "adufqelkñfo"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}"
    return contraseña,num

#desempaquetando la funcion
password,primer_numero = crear_contraseña_random(981)

#mostrando los resultados obtenidos y los datos utilizados para obtenerlo
print(f"Tu contraseña nueva es: {password}")
print(f"El numero utilizado para crearla fue: {primer_numero}")
