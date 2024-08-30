import os 
os. system("cls || clear")

soma = 0
contador = 0

while True:
    nota = float(input("digite uma nota: "))
    contador += 1 
    soma += nota

    resposta = input ("deseja inserir mais uma nota ? ").upper()

    if resposta == "N":
        break
media = soma / contador
print(f"media: {media}")
