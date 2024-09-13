import os 
os. system ("CLS || CLEAR")

""""
CRIE UM ALGORITIMO QUE RECEBA do usuario
valores e armazene em um vetor 5 numeros caso seja negativo,
atribua o valor 0.
- Liste os valores do vetor.
"""
quantidade_numeros = 5
lista_numero=[]

for i in range(quantidade_numeros):
    numero = int(input(f"digite seu  {i+1}ª numero: "))

# verificando se o numero informado é negativo.
    if numero < 0:

    #caso o numero seja negativo,
    #sera substituido por 0
        numero = 0



#inserindo o numero no vetor.
    lista_numero.append(numero)

    print("\n===exibindo dados ===")
    for cada_numero in lista_numero :
        print(cada_numero)








