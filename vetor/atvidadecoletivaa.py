import os 
os. system ("cls || clear")

"""
crie u, algoritimo que leia 5 numeros
 inteiros e em seguida usando funcoes 
 calcule e mostre na tela:

 1 A quantidade de numeros pares e impares ;
 2 A  quantidade  de numeros positivos e negativos;
 3 A quantidade de numeros inseridos 
 4 O maior e o menor numero;
 5 A media de numeros pares;
 6 A media de numeros impares;
 7 A media de todos os numeros inseridos;
 8 Mostrar os numeros lidos na ordem inverça.

alunos: jonatas fernandes, fabricio silvany,Fabio de CArvalho, victor Andrade.
"""
QUANTIDADE = 5
lista_numeros = []
pares = []
impares = []
positivos = [] 
negativos = []

def verificador_pares_impares (numeros):
    qtd_pares = 0
    qtd_impares = 0
    for numero in numeros:
        if numero %2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

def verificador_positivos_negativos(numeros):
    positivos = 0
    negativos = 0

    for numero in numeros:    
        if numero > 0:
            positivos.append(numero)
        else:
            numero < 0
            negativos.append(numero)
    return positivos, negativos

for i in range(QUANTIDADE):
    numero = int(input(f"Digite o {i+1}º numero: "))
    lista_numeros.append(numero)
    os.system("cls || clear")

pares,impares = verificador_pares_impares(lista_numeros)
positivos, negativos = verificador_positivos_negativos(lista_numeros)

#Evitando divisão por zero
if len(pares) == 0:
    media_pares = "vazio"
else:
    media_pares = sum(pares)/len(pares)

if len(impares) == 0:
    media_impares = "vazio"
else:
    media_impares = sum(impares)/len(impares)

media_geral = sum(lista_numeros)/len(lista_numeros)

print(f"Quantidade de números inseridos: {len(lista_numeros)}")
print(f"Quantidade de pares: {len(pares)}")
print(f"Quantidade de impares: {len(impares)}")
print(f"Quantidade positivos: {len(positivos)}")
print(f"Quantidade negativos: {len(negativos)}")
print(f"Maior número:{max(lista_numeros)}")
print(f"Menor número:{min(lista_numeros)}")
print(f"Média Pares:{media_pares:.2}")
print(f"Média Impares: {media_impares:.2}")
print(f"Média de todos os números: {media_geral:.2}")
print(f"Números inseridos: {lista_numeros}")
lista_numeros.reverse()
print(f"Ordem inversa dos números inseridos: {lista_numeros}")