"""
Crie funções que receba 2 numeros e retorne a soma,subtração
divisao e multiplicação destes dois numeros informados. 
OBS: Crie uma função para cada operação.
"""
import os 
os. system ("CLS || clear")
# declarando dados

soma=0
subtracao=0
divisao=0
multiplicacao=0

def soma (n1,n2):
    print( soma )
    print(f"{n1 + n2} = {n1 + n2}")
    return soma
def subtracao (n1,n2):
    print( subtracao )
    print(f"{n1 - n2} = {n1 - n2}")
    return( subtracao )
def divisao (n1,n2):
    print( divisao )
    print(f"{n1 / n2} = {n1 / n2}")
    return
def multiplicacao (n1,n2):
    print(f"{n1 * n2} = {n1 * n2 }")
    return    
#solicitando dados 
primeiro_numero = int(input("digite seu primeiro numero: "))
segundo_numero = int(input("digite seu segundo numero: "))

soma = soma (primeiro_numero, segundo_numero)
subtracao = subtracao (primeiro_numero,segundo_numero)
divisao = divisao(primeiro_numero, segundo_numero)
multiplicacao = multiplicacao(primeiro_numero, segundo_numero)

print ("=== exibindo resultado===")
print (f"soma: {soma}")
print (f"subtracao: {subtracao}")
print(f"divisao: {divisao}")
print(f"multiplicacao: {multiplicacao}")

