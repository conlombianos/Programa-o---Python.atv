import json
import os
ARQUIVO_ESTOQUE = 'estoque.json'

def Carregar_estoque():
    if os.path.exists(ARQUIVO_ESTOQUE):
        with open(ARQUIVO_ESTOQUE, 'r') as f:
            return json.load(f)
    else:
        return {}

def Salvar_estoque(Estoque):
    with open(ARQUIVO_ESTOQUE, 'w') as f:
        json.dump(Estoque, f, indent=4)

def Adicionar_produto(Estoque):
    Nome = input("Nome do produto: ")
    if Nome in Estoque:
        print("Esse produto já existe. A quantidade no estoque foi aumentada.")
        Quantidade = int(input("Quantidade que deseja adicionar: "))
        Estoque[Nome]['quantidade'] += Quantidade
    else:
        quantidade = int(input("Quantidade: "))
        Preco = float(input("Preço de cada produto: R$ "))
        Estoque[Nome] = {'quantidade': quantidade, 'preco': Preco}
        
    Salvar_estoque(Estoque)
    print("Produto adicionado.\n")

def Exibir_estoque(estoque):
    if not estoque:
        print("Sem produtos no estoque vazio.\n")
        return
    
    Total = 0
    print("\nProdutos no estoque:")
    for nome, Dados in estoque.items():
        print(f"- {nome} | Quantidade: {Dados['quantidade']} | Preço: U$ {Dados['preco']:.2f}")
        total += Dados['quantidade'] * Dados['preco']
    print(f"Valor total do estoque: R$ {total:.2f}\n")

def Menu():
    estoque = Carregar_estoque()
    while True:
        print("--- Informação do Estoque ---")
        print("1. Adicionar produto")
        print("2. Exibir estoque")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            Adicionar_produto(estoque)
        elif opcao == '2':
            Exibir_estoque(estoque)
        elif opcao == '3':
            print("Finalizado.")
            break
        else:
            print("Tente novamente.\n")

Menu()