Assentos = ["X", "X", "X", "X", "X"]

def Mostrar_assentos():
    print("Assentos:", Assentos)

def Reservar_assento():
    Num = int(input("Escolha um número de 1 a 5: ")) - 1
    if Assentos[Num] == "X":
        Assentos[Num] = "Y"
        print("Assento reservado!")
    else:
        print("Assento ocupado!")

def Cancelar_reserva():
    num = int(input("Escolha um assento de 1 a 5 para cancelar: ")) - 1
    if Assentos[num] == "Y":
        Assentos[num] = "X"
        print("Reserva cancelada!")
    else:
        print("Esse assento está livre.")

while True:
    print("\n1 - Ver assentos")
    print("2 - Reservar assento")
    print("3 - Cancelar reserva")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        Mostrar_assentos()
    elif opcao == "2":
        Reservar_assento()
    elif opcao == "3":
        Cancelar_reserva()
    elif opcao == "4":
        print("Finalizado.")
        break
    else:
        print("Tente novamente!")