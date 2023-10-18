""" 
from io import open
archivo_texto= open("..\import_persistente\Archivo.txt", "w")
frase = "Estupendo fía para estudiar Python \n el miércoles"
archivo_texto.write(frase)
archivo_texto.close()
 """
from io import open
archivo_texto= open("..\import_persistente\Archivo.txt", "r")
text=archivo_texto.read()
archivo_texto.close()
print(text)