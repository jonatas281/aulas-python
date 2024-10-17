import sqlite3
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Funcionario(Base):
    __tablename__ = 'funcionarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    cof = Column(String)
    setor = Column(String)
    funcao = Column(String)
    salario = Column(Integer)
    telefone = Column(String)

def create_db():
    engine = create_engine('sqlite:///rh_system.db')
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)()

def adicionar_funcionario(session):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cof = input("COF: ")
    setor = input("Setor: ")
    funcao = input("Função: ")
    salario = float(input("Salário: "))
    telefone = input("Telefone: ")

    novo_funcionario = Funcionario(nome=nome, idade=idade, cof=cof, setor=setor, funcao=funcao, salario=salario, telefone=telefone)
    session.add(novo_funcionario)
    session.commit()
    print("Funcionário adicionado com sucesso!")

def consultar_funcionario(session):
    id_funcionario = int(input("ID do funcionário: "))
    funcionario = session.query(Funcionario).filter(Funcionario.id == id_funcionario).first()
    if funcionario:
        print(f"Funcionário: {funcionario.nome}, Idade: {funcionario.idade}, Setor: {funcionario.setor}")
    else:
        print("Funcionário não encontrado.")

def atualizar_funcionario(session):
    id_funcionario = int(input("ID do funcionário: "))
    funcionario = session.query(Funcionario).filter(Funcionario.id == id_funcionario).first()
    if funcionario:
        funcionario.nome = input("Novo Nome: ")
        funcionario.idade = int(input("Nova Idade: "))
        funcionario.cof = input("Novo COF: ")
        funcionario.setor = input("Novo Setor: ")
        funcionario.funcao = input("Nova Função: ")
        funcionario.salario = float(input("Novo Salário: "))
        funcionario.telefone = input("Novo Telefone: ")
        session.commit()
        print("Funcionário atualizado com sucesso!")
    else:
        print("Funcionário não encontrado.")

def excluir_funcionario(session):
    id_funcionario = int(input("ID do funcionário: "))
    funcionario = session.query(Funcionario).filter(Funcionario.id == id_funcionario).first()
    if funcionario:
        session.delete(funcionario)
        session.commit()
        print("Funcionário excluído com sucesso!")
    else:
        print("Funcionário não encontrado.")

def listar_funcionarios(session):
    funcionarios = session.query(Funcionario).all()
    for funcionario in funcionarios:
        print(f"ID: {funcionario.id}, Nome: {funcionario.nome}, Setor: {funcionario.setor}")

def main():
    session = create_db()
    while True:
        print("\nRH System")
        print("1 - Adicionar funcionário")
        print("2 - Consultar funcionário")
        print("3 - Atualizar dados de funcionário")
        print("4 - Excluir funcionário")
        print("5 - Listar todos os funcionários")
        print("0 - Sair do sistema")
       
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            adicionar_funcionario(session)
        elif escolha == '2':
            consultar_funcionario(session)
        elif escolha == '3':
            atualizar_funcionario(session)
        elif escolha == '4':
            excluir_funcionario(session)
        elif escolha == '5':
            listar_funcionarios(session)
        elif escolha == '0':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

