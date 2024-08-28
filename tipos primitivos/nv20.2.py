import os 
os. system ("cls || clear ")

soma=0 
media=0

while True: 
   primeira_nota = float(input("digite a primeira_nota: "))
   segunda_nota = float(input("digite sua segunda_nota: "))
   

   if primeira_nota < 0 or primeira_nota > 10:
      print("\n nota deve ser maior ou igual a o e menor ou igual a 10: ")
   elif segunda_nota < 0 or segunda_nota > 10:
      print("\n nota deve ser maior ou igual a o e menor ou igual a 10: ")

   else:
     break # para o laço de repetição

    
soma = primeira_nota + segunda_nota
media = soma / 2

print(f"media: {media}")
print(f"=== fim===")   




