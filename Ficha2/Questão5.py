Usuarios = {}

def Cadastrar_usuario():
    print("---Cadastro de Usuário---")
    Nome = input("Digite seu nome completo: ")
    if Nome in Usuarios:
        print("Esse usuário já existe.\n")
        return
    Senha = input("Crie uma senha: ")
    Usuarios[Nome] = {"senha": Senha, "saldo": 0, "transacoes": []}
    print("Usuário cadastrado com sucesso!\n")

def Login():
    print("---Login---")
    Nome = input("Usuário: ")
    Senha = input("Senha: ")
    if Nome in Usuarios and Usuarios[Nome]["senha"] == Senha:
        print("Login feito!\n")
        return Nome
    else:
        print("Usuário ou senha incorretos.\n")
        return None

def Menu(usuario):
    while True:
        print("--- Menu ---")
        print("1 - Ver saldo")
        print("2 - Depositar")
        print("3 - Receber")
        print("4 - Histórico de transferência")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print(f"Saldo atual: R${usuario[usuario]['saldo']:.2f}\n")
        elif opcao == "2":
            valor = float(input("Valor para depósito: R$"))
            if valor > 0:
                usuario[usuario]["saldo"] += valor
                usuario[usuario]["transacoes"].append(f"Depósito de R${valor:.2f}")
                print("Depósito realizado!\n")
            else:
                print("Tente novamente.\n")
        elif opcao == "3":
            valor = float(input("Valor para saque: R$"))
            if 0 < valor <= usuario[usuario]["saldo"]:
                usuario[usuario]["saldo"] -= valor
                usuario[usuario]["transacoes"].append(f"Saque de R${valor:.2f}")
                print("Saque realizado!\n")
            else:
                print("Saldo insuficiente ou valor inválido.\n")
        elif opcao == "4":
            print("---Histórico de Trasferência---")
            for t in usuario[usuario]["transacoes"]:
                print("-", t)
            if not usuario[usuario]["transacoes"]:
                print("Nenhuma transação foi realizada.")
            print()
        elif opcao == "5":
            print("Finalizado.\n")
            break
        else:
            print("Tente Novamente mais tarde.\n")

def Sistema_bancario():
    while True:
        Usuario = Login()
        if Usuario:
            Menu(Usuario)

Sistema_bancario()