import json
import re

def optionLogin():
    while True:
        print("1: Registrar")
        print("2: Login")
        print("3: Sair")
        choice = input("Escolha uma opção: ")
        
        if choice == "1":
            register()
                    
        elif choice == "2":
            userLogged = login()
            if userLogged:
                break

def register():
    # Tente fazer o seguinte:
    try:
        with open("registerData.json", 'r') as f:
            user_info = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Arquivo não encontrado ou conteúdo vazio")
        user_info = {}

    userName = input('Qual é o seu nome de usuário?')
    userPassword = input('Qual é a sua senha?')
    userEmail = input('Qual é o seu email?')

    emailRegex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    if re.search(emailRegex,userEmail):

        user_info[f'{userName}'] = {
            'nome':userName,
            'senha':userPassword,
            'email':userEmail
        }

        with open("registerData.json",'w') as file:
            json.dump(user_info, file)
                        
            print('Registrado com sucesso!')           
    else:
        print('Email inválido')

def login():
    nameLogin = input('Qual é o seu nome login?')
    passwordLogin = input('qual é a sua senha?')
    
    Acess = False

    with open("registerData.json",'r') as file:
        userData = json.load(file)
        for i in userData:
            if i == nameLogin and userData[i]['senha'] == passwordLogin:
                print(f'Acesso liberado, Bem vindo {nameLogin} ')
                Acess = True
                with open('d:/UsuarioFezLogin.json','w') as f:
                        json.dump(i,f)

                return Acess
            
            elif i == nameLogin and not userData[i]['senha'] == passwordLogin:
                print(f'usuário {nameLogin} encontrado, porém senha incorreta')
                Acess = False
                return Acess
        else:
            if not Acess:
                print('usuário inexistente')
