entrada = input("Escriba un mensaje: ")
entrada.upper()
fichero = open("archivo.txt","w")
fichero.write(entrada)
fichero.close()