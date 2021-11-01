#par o impar project

num_pens=input("¿Que numero estas pensando? ")
num = float(num_pens)

while num > 0:  
    if num % 2 == 0:
        print("El {} es un número par".format(num))
        num_pens=input("¿Que numero estas pensando? ")
        num = float(num_pens)
    else:
        print("El {} es un número impar".format(num))
        num_pens=input("¿Que numero estas pensando? ")
        num = float(num_pens)
else:
    print("gracias por participar")
