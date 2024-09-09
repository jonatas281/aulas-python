"""
escreva um programa que solicite que o usuario o fornecimento do seu peso
em kg e de sua altura em M e a partir deles calcule o indice de massa corporea
do ultilizador:
"""
import os
os.system("cls || clear")

#funções 
def calcular_imc(peso,altura):
    resultado=peso / (altura * altura)
    return resultado

def verificar_clasificacao(imc):
    if imc < 18.5:
       return "abaixo do peso"
    elif imc < 24.9:
        return "peso normal."
    elif imc < 29.9:
        return "sobrepeso."
    elif imc < 34.9:
        return "obesidade grau I."
    elif imc < 39.9:
        return "obesidade grau II."
    else:
        return "obesidade grau III."

#entrada.
peso= flolat=(input("digite seu peso:"))
eltura= float(input("digite sua altura: "))

#processamento.
imc = calcular_imc(peso,altura)
classificacao = verificar_clasificacao (imc)

# saida
print(f"imc: {imc:.2f}")
print(f"classificação: {classificacao}")