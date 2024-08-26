import os 
os.system ("CLA || clear")

soma=0

for i in range(3):
    notas = float(input("digite uma nota: "))
    soma = soma + notas

media = soma / 3

if notas >= 7 :
    print("aprovado: ")
elif notas >= 4:
    print("recuperaçao:")
else:
    print("reprovado: ")

    print (f"media: {media}")













