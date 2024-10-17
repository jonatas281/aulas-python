import os 
os.system("cls || clear")

# Estrutura de dados.
@dataclass
class cliente:
    nome: str
    sobrenome: str
    idade: int
    peso: float
    altura: float

quantidade_cliente= 0
lista_cliente = []
#salvar em um arquivo chamado: carteira de clientes.txt
for i in range(quantidade_cliente):
    cliente(
      nome = input("digite seu nome: ")
      sobrenome = input("digite seu sobrenome: ")
      idade = int(input("digite sua idade: "))
      peso = float("digite seu peso: ")
      altura = float("dugite sua altura: ")
  ) 
#fazer leitura de dados do arquivo carteira_de_clientes.txt e mostre no terminal
lista_cliente.append(cliente)
