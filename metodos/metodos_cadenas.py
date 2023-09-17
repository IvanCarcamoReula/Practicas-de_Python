cadena1 = "Hola soy Ivan"
cadena2 = "Bienvenido maquinola"

#convierte a mayuscula
mayusc = cadena1.upper()

#convierte a minuscula
minusc = cadena1.lower()

#primera letra mayuscula
primer_letra_mayusc =cadena1.capitalize()

#buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1
busqueda_find = cadena1.find("I")

#buscamos una cadena en otra cadena, si no hay coincidencias lanza una excepcion
busqueda_index = cadena1.index("I")

#si es numerico, devuelve true, sino devuelve false
es_numerico = cadena1.isnumeric()

#si es alfanumerico devolvemos true, sino dedvuelve false
es_alfanumerico = cadena1.isalpha()

#contamos las coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de veces que coincida
contar_coincidencias = cadena1.count("a")

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true
empieza_con = cadena1.startswith("H")

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve true
termina_con = cadena1.endswith("n")

#si el valor 1, se encuentra en la cadena original, reemplaza el valor 1 de la misma, por el valor 2
cadena_nueva = cadena1.replace("Hola", "Holu maquina")

#separar cadenas con las cadenas que les pasemos
cadena_separada = cadena1.split(",")

print(contar_coincidencias)