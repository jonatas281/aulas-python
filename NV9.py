import os 
os . system (" CLS || clear")

#declarando variavel
peso_ideal= 0
# solicitando dados
altura= float(input("digite sua altura:"))

sexo = int(input("digite seu sexo (M ou F):")). upper()

# verificando
match sexo:
    case "M":
      peso_ideal = (72.7 * altura)- 58
    case "F":
      peso_ideal = (62.1 * altura)- 44.7
    case _:
      print("opcao invalida.")

      print(f"sexo: {sexo}")
      print(f"peso ideal: {peso_ideal:.2f}")
      

