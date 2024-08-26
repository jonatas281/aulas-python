import os
os. system ("CLS clear ")
# declarando variaveis

soma =  0

for i in range(4):
    notas = float(input("digite uma nota: "))
    soma = soma + notas

    media = soma / 4

    print (f"media: {media}")



