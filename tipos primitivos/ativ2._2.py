"""
2. ENCONTRANDO O PRIMEIRO NÚMERO DIVISÍVEL POR 7
Enunciado: Escreva um programa que use um laço while para
 encontrar o primeiro número maior que 50 que seja divisível
 por 7. Exiba esse número.

Dica: Inicie com uma variável em 51 e use o operador % 
para verificar divisibilidade por 7. Continue até encontrar
 um número que satisfaça a condição.
"""
import os 
os. system

numero = 51

while True:
    if numero % 7 == 0 :
        print(f"o primeiro numero maior que 50 que é divisivel por 7 é {numero}")
        break

    numero+= 1 