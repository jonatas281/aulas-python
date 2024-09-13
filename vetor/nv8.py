import os 
os.system ("cla || clear")

"""
crie um algoritmo que aceite aoenas 6 valores inteiros
positivos e pares em seguida, mostre na  tela os valores
lidos na ordem inversa.

caso seja informado  um numero diferente dos criterios
apresentado acima reoita a pergunta para o usuario.
"""

quantidade_numero=6
lista_numero=0
lista_pares_positivos=[]
#entrada.
for i in range(quantidade_numero):
    while True:
       numero= int(input(f"digite o {i+1}ª:  numero: "))
  
    # verificando se o numero é par e positivo
       if numero % 2 == 0 and numero > 0: 
         lista_pares_positivos.append(numero)
         break
       else:
          print ("numero invalido. \n tente novamente. \n \n")
#saida.
print("\n=== exibindo resultado ===")
for numero in reversed(lista_pares_positivos):
    print(numero) 
