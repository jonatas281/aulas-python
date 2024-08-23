import os
os . system ("CLS || clear ")

# solicitendo dados
print("""
forma de pagamento
1 - pagamento a vista 
2 - pagamento a prazo
""")

pagamento=int(input("digite a forma de pagamento:"))



match (pagamento):
    case 1 :
        print("""forma de pagamento a vista:
                 valor do produto: R$ 100,00 
                 valor do desconto: R$ 10,00
                 total a pagar: R$ 90,00 """)
    case 2 :
     parcela =   int (input("digite a quantidade de parcela:"))
     print(f""" forma de pagamento a prazo:
                  valor do produto: R$100,00
                  quantidade de parcela {parcela}      
                  valor da parcela: R$ 16,66
                  total a prazo: R$ 100,00 """)
    case _:
        print("invalido")
    
print("===FIM===")
              

