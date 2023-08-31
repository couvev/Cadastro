import json

users = {}

def save_data(users):
    with open('data.json', 'w') as file:
        json.dump(users, file)

def load_data():
    try:
        with open('data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

users = load_data()

def add_user():
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    tel = input("Digite seu telefone: ")
    cpf = input("Digite seu CPF: ")
    
    users[nome] = {'senha': senha, 'telefone': tel, 'cpf': cpf}
    
    print("Usuário adicionado!")
    
    save_data(users)
    
    if input("Adicionar mais um? ") == "Sim":
        add_user()
    elif input("Fazer login? ") == "Login":
        login_user()
    

def login_user():
    username_input = input("Usuário: ")
    password_input = input("Senha: ")

    if username_input in users:
        user_info = users[username_input]
        if user_info['senha'] == password_input:
            print("Acesso concedido!")
            print("Telefone:", user_info['telefone'])
            print("CPF:", user_info['cpf'])
        else:
            print("Senha incorreta!")
    else:
        print("Usuário não encontrado, faça cadastro!")
        add_user()

while True:
    teste_add = input("Login ou Cadastro? ")

    if teste_add == "Login":
        login_user()
        break
    elif teste_add == "Cadastro":
        add_user()
    else:
        print("Opção inválida. Escolha entre 'Login' ou 'Cadastro'.")

print("OK")
