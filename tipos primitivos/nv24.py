# escreva um algoritimo que pergunte ao usuario se deseja
# inserir mais uma nota, se a resposta do usuario for "N",
# o programa fara a media aritmetica das notas informadas
# e mostrara a media aritmetica para o  usuario.

import os
os. system("CLS || clear ")

soma = 0 
media = 0
nota=0
# solicitando dados

Nota_1 = float(input("digite sua primeira nota: "))
Nota_2= float(input("digite sua segunda nota: "))

#exibindo dados 
print("""
deseja inserir mais uma nota?
1=sim ou 2=não!
""")
opcao=int(input("digite a opção:"))
match(opcao):
    case 1 : 
        print("digite sua nota:")
    case 2 :
        print(f"digite ")
        soma = Nota_1 + Nota_2 
        media = soma / 2
    case _:
        print("opção invalida:")

print("===FIM===")
        








