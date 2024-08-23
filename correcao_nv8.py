import os
os . system("CLS || clear")

# declarando variaveis
desconto = 0
preco_final = 0
preco_parcelado = 0
preco_produto = 0

print("solicitando dados para o usuario.")
preco_parcelado = int(input("digite o valor do produto."))

print(f"\nescolha uma das formas de pagamento a baixo.")
print("1 - pagamento a vista")
print("2 - pagamento a prazo")
opcao = int(input("informe a opcao desejada."))

match (opcao):
    case 1 :
        desconto = preco_produto * 0.10
        preco_final = preco_produto - desconto

        print(f"\npreço do produto : R$ {preco_produto}")
        print(f"forma de pagamento a vista")
        print(f"valor do desconto: R$ {desconto}")
        print(f"total a pagar: R$ {preco_final}")
    case 2 :
        parcelas = int(input("\ndigite a quantidade de parcelas"))

        preco_parcelado = preco_produto / parcelas
        preco_final = preco_produto

        print(f"preço do produto: R$ {preco_produto}")
        print(f"forma de pagamento a prazo")
        print(f"quntidade de parcelas: {parcelas}")
        print(f"valor por parcela: R$ {preco_parcelado:.2f}")
        print(f"total a prazo : {preco_final:.2f}")
    case _ :
        print("opcao invalida: \n ")
                       