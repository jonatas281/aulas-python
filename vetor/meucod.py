import os 
os. system ("cls || clear ")

# declarando variaveis e listasv 
quantidade_numeros=5
num_pares=[]
num_impares=[]
num_positivos=[]
num_negativo=[]
lista_numeros=[]

# solicitando dados
for i in range(quantidade_numeros):
    numero=int(input(f"digite seu {i+1}ª numero: "))

    if numero %2==0:
        num_pares.append(numero)
    else:
        num_impares.append(numero)
    if numero >0:
        num_positivos.append(numero)
    else:
        num_negativo.append(numero)
# calculando media de pares e impares
    if len(num_pares)==0:
        media_pares="vazio"
    else:
        media_pares= sum(num_pares)/(num_pares)
    if len(num_impares)==0:
        media_impares="vazio"
    else:
        media_impares= sum (num_impares)/(num_impares)
    media_geral=sum(lista_numeros)/len(lista_numeros)


print(f"quantidade de numeros pares:{len(num_pares)}")
print(f"quantidade de numeros impares: {len(num_impares)}")
print(f"quantidade de numero positivo: {len(num_positivos)}")
print(f"quantidade de numeros negativo: {len(num_negativo)}")
print(f"media pares: {media_pares:.2}")
print(f"media impares: {media_impares:.2}")
print(f"media geral: {media_geral:.2}")



