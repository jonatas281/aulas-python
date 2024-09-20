import os 
os. system ("cls || clear")

"""
. Crie um alaritimo que leia 5 numeros 
inteiros e , e. seguida, mostre na tela:
1 A quantidade de numeros pares
2 A quantidade de numeros impares
3 A quantidade de numeros positivos
4 A quantidade de numeros negativos 
"""
quantidade_numeros=5
num_impares=[]
num_pares=[]
num_positivo=[]
num_negativo=[]
for i in range (quantidade_numeros):
    numero= int(input(f"digite o {i+1}º numero: "))

    if numero %2==0:
        num_pares.append(numero)
    else:
        num_impares.append(numero)
    if numero >0:
        num_positivo.append(numero)
    else:
        num_negativo.append(numero)

print(f"quantidade de numeros pares : {len(num_pares)}")
print(f"quantidade de numeros impares: {len(num_impares)}")
print(f"quantidade de numeros positivos: {len(num_positivo)}")
print(f"quantidade de numeros negativos: {len(num_negativo)}")


