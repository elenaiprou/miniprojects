expenses = [10.5, 8, 5, 15, 20, 5, 3]

suma = 0

for expense in expenses:
    suma = suma + expense

print("You spend ", suma, "€", sep ='') # sep ='' elimina espacios entre texto y valotes

#hay una función porpia, que es la funcion sum con la lista

total = sum(expenses)
print("You spend ", total, "€", sep ='')