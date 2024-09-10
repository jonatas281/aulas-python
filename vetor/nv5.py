import os
os.system("cls||clear")
"""
crie um programa que leia numeros 
armazenados em um vetor e informe quantos
sao impares. 

mostre os numeros informados peloo usuario:
"""
quantidade_notas=6
pares=0
impares=0
lista_numeros=0
verificar_pares_impares=6
def ferificar_pares_impares(numeros):
    qtd_pares = 0
    qtd_impares = 0
    for numero in numero:
        if numero % 2 == 0:
            qtd_pares +=1
        else:
            qtd_impares +=1
    return qtd_pares,qtd_impares

print("\n===solicitando dados===")
for i in range(quantidade_notas):
    numero= float(input(f"digite o {i+1}ªnumero: "))
    lista_numeros.append(numero)

#processamento
pares,impares= verificar_pares_impares(lista_numeros)

#saida
print("\n=== exibindo resultado===")
for contador,nota in enumerate (lista_numeros):
    print(f"{contador}ªnota:{nota}")





