import os
os. system("cls || clear")

quantidade_nota=3
soma=0

for i in range(quantidade_nota):
    while True:
        nota = float(input(f"digite {i+1} nota: "))

        if nota < 0 or nota > 10:
            print("nota invalida! \n digite novamente...")
        else:
            # soma = + nota
            soma += nota
            break

media = soma / quantidade_nota

if media >= 7:
    print("aprovado: ")
elif media >= 5:
    print("recuperação.")
else:
    print("reprovado: ")