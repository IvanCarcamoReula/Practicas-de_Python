texto = input("Escriba una frase: ")

lista = texto.split()

contar_elementos = len(lista)


print(texto)
print(f"La frase escrita tiene {contar_elementos} palabras en total")