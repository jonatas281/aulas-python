import os
os. system ("cls || clear")

soma = 0

for i in range(4):
  numero = int(input(f"digite {i+1}° numero: "))
  soma = soma + numero
  print (f"soma: {soma}")