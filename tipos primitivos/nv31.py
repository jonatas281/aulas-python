"""
escreva um programa que permita ler 3 notas devum 
aluno, usando laço de repetição e informe por meio
de uma função a média;
"""
import os 
os.system("cls || clear")
soma=0
quantidade_notas=3
for i in range(3):
    nota_1=int(input(f"digite a sua {i + 1}ª nota: "))
    soma += nota_1   
 
def calcular_media():
    media = soma / quantidade_notas
    print (f"media: {media}")
    return media
media = calcular_media()

    
    
      