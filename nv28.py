"""Crie u,a função que receba um numero e mostre uma 
mensagem informando se o numero é par ou Impar 
"""
import os
os. system ("CLS || clear")

# solicitamdo dados 

def verificador (numero):
  if numero %2==0:
    print("par")
  else:
    print("impar")
    return numero
  
numero=int(input("digite seu numero:"))

verificador(numero)