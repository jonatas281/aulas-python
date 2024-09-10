import os 
os. system ("cls || clear")
"""
crie um algoritima qie preencha um vetor com 10
numeros reais, calcule e mostre a quantidade de
 numeros negativos e a soma dos numeros positivo
 desse vetor.
"""
# Inicializa o vetor
vetor = []

# Preenche o vetor com 10 números reais fornecidos pelo usuário
for i in range(10):
    numero = float(input(f"Digite o {i+1}º número real: "))
    vetor.append(numero)

# Inicializa variáveis para contar números negativos e somar números positivos
quantidade_negativos = 0
soma_positivos = 0.0

# Processa o vetor
for numero in vetor:
    if numero < 0:
        quantidade_negativos += 1
    elif numero > 0:
        soma_positivos += numero

# Exibe os resultados
print(f"Quantidade de números negativos: {quantidade_negativos}")
print(f"Soma dos números positivos: {soma_positivos:.2f}")





    
