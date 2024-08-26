import os 
os.system ("CLA || clear")
soma =  0
media=0
for i in range(3):
    notas = float(input("digite uma nota: "))
    soma = soma + notas

if notas >= 7 :
    print("aprovado: ")
else:
    if notas <= 4 :
        print("reprovado: ")
    else:
        print("recuperação")
#calculando
    media = soma / 3

    
    
    print (f"media: {media}")








