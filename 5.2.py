import os 
os. system ("cls || clear")

# Inicializa o vetor
vetor = []

# Define a quantidade de números a serem lidos
n = int(input("Quantos números você deseja informar? "))

# Preenche o vetor com os números fornecidos pelo usuário
for i in range(n):
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)

# Inicializa a contagem de números ímpares
quantidade_impares = 0

# Processa o vetor
for numero in vetor:
    if numero % 2 != 0:
        quantidade_impares += 1

# Exibe os números informados e a quantidade de números ímpares
print("Números informados:")
for numero in vetor:
    print(numero)

print(f"Quantidade de números ímpares: {quantidade_impares}")




