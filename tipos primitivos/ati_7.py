"""
7. GERANDO UMA LISTA DE QUADRADOS
Enunciado: Crie um programa que use um laço `for` para gerar
 e exibir os quadrados dos números de 1 a 5 
 (ou seja, 1², 2², 3², etc.).

Dica: O quadrado de um número é o número 
multiplicado por ele mesmo.
"""

import os 
os.system("CLS || clear")

for i in range(1,6):
    print(f"{i} * {2}= {i * 2}")