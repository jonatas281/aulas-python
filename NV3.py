import os
os .system ("cls || clear ")

#solicitando dados
nome=input("digite seu nome:")
idade=int(input("digite sua idade: "))

# verifivando
if idade<18 or idade >65 :
    print("nao sao obrigados a votar:")
else:
    print("voto obrigatorio:")



