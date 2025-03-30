valor_total = float(input("Digite o valor total das mercadorias compradas: R$ "))


if valor_total <= 500:
    print("Não há imposto a ser aplicado.")
else:
    excesso = valor_total - 500
    imposto = excesso * 0.
    print(f"O imposto a ser aplicado é de: R$ {imposto}")
