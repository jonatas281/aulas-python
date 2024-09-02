"""
2. SOMANDO NÚMEROS
Enunciado: Crie um programa que, utilizando um laço `for`,
 calcule a soma dos números de 1 a 5 e mostre o resultado.

Dica: Você pode criar uma variável para armazenar
 a soma e adicionar a ela o valor de cada número a cada iteração.
"""
import os 
os.system ("CLS || clear ")

# declarando variaveis
soma=0

for i in range (5):
    numero= int(input(f"digite: {i + 1}°numero:"))
    soma = soma + numero
    print(f"soma: {soma}")




