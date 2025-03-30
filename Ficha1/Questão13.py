Salario_inicial = float(input("Digite o salário: "))
Anos = int(input("Digite a quantidade de anos: "))
Aumento_percentual = float(input("Digite o aumento percentual: "))

Aumento_percentual /= 100
Salario_atual = Salario_inicial

for Ano in range(1, Anos + 1):
    Salario_atual += Salario_atual * Aumento_percentual
    Aumento_percentual *= 2 

print(f"Após {Anos} anos, o salário atual é: R$ {Salario_atual:.2f}")