import os 
os. system ("cls || clear ")

#declarando variaveis

login = input("digite seu login: ")
senha = input("digite sua senha: ")

login_salvo = login == "jona"
senha_salva = senha =="12345"


while True: 
    login = input("digite seu login: ")
    senha = input("digite seua senha: ")
    if login_salvo == login and senha_salva == senha:
      print("bem vindo ")
      break
    else:
      print("login ou senha invalido. ")

print("==FIM===")




