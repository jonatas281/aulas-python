"""
faça um programa que imprime a tabuada de um numero informado pelo o usuario
de 1 a 10 ultilizando uma função para exibir o resultado.
"""
import os
os.system("CLS || clear")
# declarando variaveis

tabuada = 0 

def tabuada_numero (n1,n2):
    calculo = n1 * n2
    return tabuada

numero = int(input("digite um numero: "))

for i in range (1,11):
      tabuada = print(f"{numero} X {i} = {i* numero} " )

tabuada = tabuada_numero (numero,1)