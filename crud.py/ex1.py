class aluno:
    nome: str
    idade: int

quantidade_aluno = 0
lista_de_alunos=0
lista_alunos = []
#solicitando dados
for i in range (quantidade_aluno):
    aluno(
        nome = input ("digite seu nome: "),
        idade = int(input("insira sua idade: "))             
    )
    lista_de_alunos.append(aluno)

print("\n=== Exibindo dados dos alunos ===")
for aluno in lista_de_alunos:
    print(f"nome: {aluno.nome}")
    print(f"idade: {aluno.idade}")

# definindo arquivo para salvar os dados.
nome_do_arquivo = "lista_de_alunos_senai.txt"

# abrindo arquivo e definindo que sera feita a escrita de dados.
with open(nome_do_arquivo, "a") as arquivo_alunos:
    #percorrendo no arquivo uma linha de cada vez.
    arquivo_alunos.write(f"{aluno.nome}, {aluno.idade}\n")
#fechar conexao com o arquivo 


print("\n=== dados dos alunos salvo com sucesso===")
