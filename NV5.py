import os 
os .system("cls || clear ")

# solicitando dados 
print("""
1 - picanha R$ 25,00
2 - lasanha R$ 20,00
3 - strogonoff R$ 18,00
4 - bife acebolado R$ 15,00
5 - pao com ovo R$ 5,00
""")

opcao=int(input("digite uma opcao: "))

match (opcao):
    case 1 :
        print("picanha R$ 25,00: ")
    case 2 :
        print("lasanha R$ 20,00: ")
    case 3 :
        print("strogonoff R$ 18,00: ")
    case 4 :
        print("bife acebolado R$ 15,00: ")
    case 5 : 
        print("pao com ovo R$ 5,00: ")
    case _ :
        print("opcao invalida: ")

print("===fim===")

