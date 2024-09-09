"""
escreva um programa que permita ler 2 nota de um aluno e :
- informe por meio de uma funçao a media;

- informe por meio de uma função se a média for maior ou
igual a 7, o aluno estara aprovado, caso contrario, estara
 reprovado.
"""
import os 
os.system("cls || claar")
#declarando variaveis
soma=0
divisao=0
media=0
def calcular_media(nota_1,nota_2):
    soma = nota_1 + nota_2
    media = soma/2
    return media
def verificar_resultado(media):
    if media >=7:
        return"aprovado"
    else:
        return "reprovado"
    
# solicitando dados
nota_1=float(input("digite sua primeira nota: "))
nota_2=float(input("digite sua segunda nota: "))
   
media = calcular_media(nota_1,nota_2)
resultado= verificar_resultado(media)


#exibindo dadoa
print("===resultado===")
print(f"media:{media}")
print(f"resultado: {resultado}")
