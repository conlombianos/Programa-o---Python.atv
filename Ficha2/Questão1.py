import json
from datetime import datetime
ARQUIVO = 'tarefas.json'

def Carregar_tarefas():
    try:
        with open(ARQUIVO, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def Salvar_tarefas(Tarefas):
    with open(ARQUIVO, 'w') as f:
        json.dump(Tarefas, f, indent=4)

def Adicionar_tarefa():
    Descricao = input("Escreva uma descrição para a tarefa: ")
    Prazo = input("Digite o prazo (DD-MM-AA): ")
    Tarefa = {
        'descricao': Descricao,
        'prazo': Prazo,
        'concluida': False
    }

    Tarefas = Carregar_tarefas()
    Tarefas.append(Tarefa)
    Salvar_tarefas(Tarefas)
    print("Tarefa adicionada!")

def Listar_tarefas():
    Tarefas = Carregar_tarefas()
    Tarefas = sorted(Tarefas, key=lambda x: x['prazo'])

    for i, Tarefa in enumerate(Tarefas):
        print(f"{i+1}. {Tarefa['descricao']} (Prazo: {Tarefa['prazo']})")

def Marcar_concluida():
    Listar_tarefas()
    Indice = int(input("Digite o número da tarefa concluída: ")) - 1
    Tarefas = Carregar_tarefas()
    
    if 0 <= Indice < len(Tarefas):
        Tarefas[Indice]['concluida'] = True
        Salvar_tarefas(Tarefas)
        print("Tarefa concluída!")
    else:
        print("Número inválido.")

def Menu():
    while True:
        print("\n--- Gerenciador de Tarefas ---")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Sair")

        Escolha = input("Escolha uma opção: ")
        if Escolha == '1':
            Adicionar_tarefa()
        elif Escolha == '2':
            Listar_tarefas()
        elif Escolha == '3':
            Marcar_concluida()
        elif Escolha == '4':
            print("Finalizado.")
            break
        else:
            print("Tente novamente.")
Menu()