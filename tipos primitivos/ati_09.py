"""

9. CRIANDO UM RETÂNGULO COM ASTERISCOS
Enunciado: Desenvolva um programa que utilize dois laços `for`
 (um dentro do outro) para imprimir um retângulo de 4 linhas
   por 6  colunas de asteriscos (`*`).

Dica: Use um laço para cada linha e outro 
para cada coluna dentro da linha.
"""
import os 
os. system("cls || clear")

num_linha= 4 
num_colunas= 6

#laço para cada linha
for i in range (num_linha):
    # laço para cada coluna dentro da linha
    for j in range (num_colunas):
        #imprime um asteristico sem pular a linha
        print ('*', end='')
    print()