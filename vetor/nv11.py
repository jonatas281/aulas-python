import os
os . system ("cls || clear")



quantidade_numeros=5
num_impares=[]
num_pares=[]
num_positivo=[]
num_negativo=[]
contador=1

while True:
    numero = int(input(f"digite o {contador}º numero: "))
    contador +=1
    if numero %2==0:
        num_pares.append(numero)
    else:
        num_impares.append(numero)
    if numero >0:
        num_positivo.append(numero)
    else:
        num_negativo.append(numero)

    if numero ==0:
        break     

print(f"quantidade de numeros pares : {len(num_pares)}")
print(f"quantidade de numeros impares: {len(num_impares)}")
print(f"quantidade de numeros positivos: {len(num_positivo)}")
print(f"quantidade de numeros negativos: {len(num_negativo)}")






