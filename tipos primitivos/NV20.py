import os 
os. system ("cls || clear ")

nota= float(input("digite sua nota: "))

while nota < 0 or nota > 10:

    print("\nA nota deve ser maior ou igual a 0 e menor ou igual a 10")
nota = float(float("digite uma nota: "))

print(f"nota: {nota}")