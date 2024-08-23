import os
os . system ("cls || clear")
 
# solicitando dados 
numero = int(input("digite um numero para a tabuada."))

print(f"\ntabuada de multiplicaçãode numero {numero}")
for i in range(1,11):
    print(f"{numero} X {i}= {numero * i }")             