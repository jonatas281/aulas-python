import os 
os. system ("cls || clear ")

#solicitando dados

print ("""
1 - domingo 
2 - segunda
3 - terça 
4 - quarta 
5 - quinta 
6 - sexta
7 - sabado """)

opcao=int(input("digite a opção:"))

match (opcao):
    case 1 : 
        print("domingo: final de semana. ")
    case 2 :
        print("segunda: dia ultil. ")
    case 3 :
        print("terça: dia ultil. ")
    case 4 :
        print("quarta: dia ultil. ")
    case 5 : 
        print("quinta: dia ultil. ")
    case 6 : 
        print("sexta: dia ultil. ")
    case 7 :
        print("sabado: fim de semana. ")
    case _:
        print("opcao invalido")

print("=== fim===")

    