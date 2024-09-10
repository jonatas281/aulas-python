import os
os.system("cls || clear")

#entrada 
lista_notas=[]

#por indice
for i in range (2):
    nota=float(input("digite uma nota: "))
    lista_notas.append(nota)

#saida.
for nota in lista_notas:
    print(f"nota: {nota}")
