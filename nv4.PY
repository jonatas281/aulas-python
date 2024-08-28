import os
os.system("cls||clear") 
#solicitando dados

primeiro_numero=int("didite primeiro numero: ")
segundo_numero=int("digite segundo numero: ")
opcao=input("digite a opcao (+ - * /):")

match(opcao):
     case "+":
       resultado = primeiro_numero + segundo_numero
     case "-":
       resultado = primeiro_numero - segundo_numero
     case "*":
       resultado = primeiro_numero * segundo_numero
     case "/":
       resultado = primeiro_numero / segundo_numero
     case _:
       print("opcao invalida:")

print(f"resultado: {resultado}")
print("===f===")
# calculando