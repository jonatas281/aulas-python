"""10. SOMA DOS NÚMEROS ÍMPARES
Enunciado: Escreva um programa que calcule a soma dos 
números ímpares de 1 a 9 utilizando um laço `for`.

Dica: Verifique
se um número é ímpar usando o operador `%` e adicione esses
 números a uma
variável de soma.
"""
import os
os.system("CLS || clear ")

soma=0

for numero in range (1, 10):
    if numero % 1 == 0:
        print(numero)

soma = soma + numero
print(f"soma: {soma}")









