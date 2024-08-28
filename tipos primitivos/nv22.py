import os
os. system ("CLS || clear:")

#declarando variaveis


login_salvo = "jona"
senha_salva = "12345"
login = input("digite seu login: ")
senha = input("digite sua senha: ")
contador = 0
    
    

while True:
    login = input("digite seu login: ")
    senha = input("digite seua senha: ")
    contador += 1
    if login_salvo == login and senha_salva == senha:
      print("bem vindo ")
   
      
      break
    else:
      print("login ou senha invalido. ")
      print(f"\ntentativas: {contador} \n ")
      if contador == 3:
        break


print("==FIM===")












