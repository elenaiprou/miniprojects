#Contar palabras. Deberia subir texto desde un txt pero por ahora empiezo por una frase escrita en este archivo.

text = "Hoy me he encontrado con las personas que viven en la selva."

numPalabras = 0
for caracter in text:
    if caracter == " ":
        numPalabras +=1

print("Palabras totales: ", numPalabras)

"""
def count_word(text):
    count=1
    for i in range(len)
"""