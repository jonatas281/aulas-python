"""
3. MULTIPLICAÇÃO ATÉ O VALOR MÁXIMO
Enunciado: Escreva um programa que multiplique um número inicial
 por um fator dado pelo usuário até que o produto exceda 100. 
 Exiba o produto final e o número de multiplicações realizadas.

Dica: Use uma variável para o produto e outra para contar 
as multiplicações. Continue multiplicando o número pelo
 fator até que o produto seja maior que 100.
"""
import os 
os.system("CLS || clear ")


numero_inicial = float(input("Digite o número inicial: "))
fator = float(input("Digite o fator de multiplicação: "))


produto = numero_inicial
contagem_multiplicacoes = 0

while produto <= 100:
    produto *= fator
    contagem_multiplicacoes += 1

    print(f"O produto final é: {produto}")
print(f"Número de multiplicações realizadas: {contagem_multiplicacoes}")