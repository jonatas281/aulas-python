""""
3. IMPRIMINDO NÚMEROS PARES 
Enunciado: Desenvolva um programa que use um laço `for`
 para imprimir todos os números pares de 2 a 10.

Dica: Um número é par se ele é divisível por 2. 
Use o operador `%` para verificar se o número é par.
"""
import os
os. system ("CLS || clear")


print ("\nultilizando o laço (for):")

for numero in range (1, 11):
    if numero % 2 == 0:
        print(numero)