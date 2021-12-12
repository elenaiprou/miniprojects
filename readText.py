# leemos un texto

f = open('demo.txt', "r")

text = f.read()

textup = text.swapcase() #convierte el texto en mayúsculas. 
print(textup)

letrant = ""

for caracter in textup:
    if caracter == "E":
        letrant += "E"
    if caracter == "C" and letrant == "E":
        letrant += "C"
    if caracter == "O" and letrant == "EC":
        letrant += "O"
    if caracter == "G" and letrant == "ECO":
        letrant += "G"
    if letrant == "ECOG":
        print(letrant)
        letrant = ""


print("no se que pasa aqui", letrant)

f.close()

print("repito variable", text)