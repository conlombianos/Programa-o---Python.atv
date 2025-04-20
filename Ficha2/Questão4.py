# Dicionário para armazenar os usuários
usuarios = {}

# Função para cadastrar novo usuário
def cadastrar_usuario():
    print("=== Cadastro de Novo Usuário ===")
    nome = input("Escolha um nome de usuário: ")
    if nome in usuarios:
        print("Usuário já existe.\n")
        return
    senha = input("Crie uma senha: ")
    usuarios[nome] = {"senha": senha, "saldo": 0, "transacoes": []}
    print("Usuário cadastrado com sucesso!\n")

# Função para login
def login():
    print("=== Login ===")
    nome = input("Usuário: ")
    senha = input("Senha: ")
    if nome in usuarios and usuarios[nome]["senha"] == senha:
        print("Login bem-sucedido!\n")
        return nome
    else:
        print("Usuário ou senha incorretos.\n")
        return None

# Função para exibir menu bancário
def menu(usuario):
    while True:
        print("=== Menu ===")
        print("1 - Ver saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Ver histórico")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print(f"Saldo atual: R${usuarios[usuario]['saldo']:.2f}\n")

        elif opcao == "2":
            valor = float(input("Valor para depósito: R$"))
            if valor > 0:
                usuarios[usuario]["saldo"] += valor
                usuarios[usuario]["transacoes"].append(f"Depósito de R${valor:.2f}")
                print("Depósito realizado com sucesso!\n")
            else:
                print("Valor inválido.\n")

        elif opcao == "3":
            valor = float(input("Valor para saque: R$"))
            if 0 < valor <= usuarios[usuario]["saldo"]:
                usuarios[usuario]["saldo"] -= valor
                usuarios[usuario]["transacoes"].append(f"Saque de R${valor:.2f}")
                print("Saque realizado com sucesso!\n")
            else:
                print("Saldo insuficiente ou valor inválido.\n")

        elif opcao == "4":
            print("=== Histórico de Transações ===")
            for t in usuarios[usuario]["transacoes"]:
                print("-", t)
            if not usuarios[usuario]["transacoes"]:
                print("Nenhuma transação realizada.")
            print()

        elif opcao == "5":
            print("Saindo...\n")
            break

        else:
            print("Opção inválida.\n")

# Execução principal
def sistema_bancario():
    while True:
        print("=== Bem-vindo ao Sistema Bancário ===")
        print("1 - Login")
        print("2 - Cadastrar novo usuário")
        print("3 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            usuario = login()
            if usuario:
                menu(usuario)
        elif escolha == "2":
            cadastrar_usuario()
        elif escolha == "3":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida.\n")

# Iniciar o sistema
sistema_bancario()