








quantidade_notas=5
lista_numero=[]

print ("\n===solicitando dados===")
for i in range (quantidade_notas):
    numero=float(input(f"digite o {i+1}ª numero:"))
    lista_numero.append(numero)


#processamento.
maior_numero =max(lista_numero)
menor_numero =min(lista_numero)

#saida
print("\n===exibindo resultado===")
for contador, nota in enumerate(lista_numero):
    print(f"{contador+1}ªnota: {nota}")

    print(f"menor numero: {menor_numero}")
    print(f"maior numero: {maior_numero}")








