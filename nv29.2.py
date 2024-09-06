import os
os. system ("CLS || clear")


def verificar_pares_impares():
    pares = 0 
    impares = 0

    for i in range (6):
        numero = int(input("digite um numero: "))

        if numero % 2 == 0 :
            pares+=1
        else:
            impares+=1
    
    print(f"\nquantdade pares: {pares}")
    print(f"quantidade impares: {impares}")

    #chamando a funçao.
    verificar_pares_impares()