"""
escreva um programa que solicite ao usuario o ano de 
nacimento e, ultilizando uma função,retorne com a idade do 
usuario.
"""
import os
os.system("cls||clear")

def calcular_idade_ano_nascimento(ano_nascimento):
    return 2024 - ano_nascimento

ano_nascimento= int(input("digite o ano do seu nascimento: "))

idade = calcular_idade_ano_nascimento(ano_nascimento)

print ("=== RESULTADO ===")
print(F"idade: {idade}")
    