Dias = int(input("Digite o número de dias de aluguel: "))
Quilometros = float(input("Digite a quantidade de quilômetros rodados: "))

Custo_diario = Dias * 90

if Quilometros > 100:
    Km_excedente = Quilometros - 100
    Taxa_extra = Km_excedente * 12
    Custo_total = Custo_diario + Taxa_extra
else:
    Custo_total = Custo_diario

print(f"O valor total a ser pago é: R$ {Custo_total}")