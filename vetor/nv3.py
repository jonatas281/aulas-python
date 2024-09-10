import os 
os.system("cls||clear")

"""
crie um programa que leia 3 notas, armazenando
em um vetor e calcule a media aritimetica

verifique a  situação do aluno considerando:
-media maior ou igual a 7:aprovado
media maior ou igual a 5; recuperação
media menor que 5; reprovado

mostre as 4 notas informada pelo 
usuario e informe a media
"""
# declarando variaveis
soma = 0
media=0
#entrada 
lista_nota=[]
quantidade_notas=4
print("\n===solicitando dados ===")
for i in range (quantidade_notas):
    nota = float(input("digite uma nota: "))
    lista_nota.append(nota)

# processamanto.
soma= sum(lista_nota)
media = soma/ quantidade_notas

if media >= 7:
    situacao="aprovado"
if media >= 5:
    situacao="recuperação"
if media <= 5:
    situacao="reprovado"
print(f"Resultado:{situacao}") 
