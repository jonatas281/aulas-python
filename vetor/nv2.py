import os 
os. system("cls || clear")

"""
crie um programa que leia 3 notas armazenando em um 
vetor e calcule a media aritimetica.

mostre as 3 notas informada pelo o usuario 
e informe a media
"""
# declarando variaveis
soma = 0
media=0
#entrada 
lista_nota=[]
quantidade_notas=3
print("\n===solicitando dados ===")
for i in range (quantidade_notas):
    nota = float(input("digite uma nota: "))
    lista_nota.append(nota)

# processamanto.
soma= sum(lista_nota)
media = soma/ quantidade_notas

#saida
print("\n===exibindo dados===")
for contador,nota in enumerate(lista_nota):
    print(f"{contador+1}ªnota: {nota}")
print(f"media: {media}")

