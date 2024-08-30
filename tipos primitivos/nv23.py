import os
os. system ("CLS || clear:")
#declarando variaveis

media=0
soma=0

while True:
    nota_1=float(input("digite sua nota 1: "))
    nota_2=float(input("digite sua nota 2: "))
    nota_3=float(input("digite sua nota 3: "))
#calculando
    soma= nota_1 + nota_2 + nota_3
    media= soma/3

    if media >7:
        print("\naprovado: ")
    if media < 5 or 6.9:
        print("\nrecuperação: ")
    if media <5 :
        print("\nreprovado: ")

    print(f"media: {media}")