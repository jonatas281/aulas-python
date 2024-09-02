"""
4. CONTROLE DE GASTOS MENSAIS
Enunciado: Crie um programa que ajude um usuário a controlar
 seus gastos mensais. O programa deve permitir que o usuário 
 insira gastos diários até que o total gasto no mês exceda um
 orçamento inicial fornecido. O programa deve exibir o total 
 gasto e o valor  excedente.

Dica: Defina um orçamento e use um laço while para somar os
 gastos diários. Pare quando o total gasto exceder o orçamento.
"""
import os 
os. system("CLS || clear")

orcamento = float(input("digite o orçamento do mes: "))
total_gasto=0.0
numero_gasto=0

while total_gasto <= orcamento:
    gasto_diario= float(input("digite um gasto diario: "))
    total_gasto += gasto_diario

    numero_gasto+=1
    exedente = total_gasto-orcamento

    print(f"total gasto no mes: R$ {total_gasto:.2f}")
    print(f"valor exedente: R$ {exedente:.2f}")
    

