#arbriendo el archivo con with open
with open("archivos\\texto_de_dalto.txt", encoding= "UTF-8") as archivo:
    
    #leemos el archivo
    contenido = archivo.read()
    
    #mostramos el archivo
    print(archivo.read())
    
#no es necesario cerrarlo al usar with open