Num1 = int(input("Digite o primeiro número: "))
Num2 = int(input("Digite o segundo número: "))
Num3 = int(input("Digite o terceiro número: "))

if Num1 >= Num2 and Num1 >= Num3:
    maior = Num1
elif Num2 >= Num1 and Num2 >= Num3:
    Maior = Num2
else:
    Maior = Num3

# Determinar o menor número
if Num1 <= Num2 and Num1 <= Num3:
    Menor = Num1
elif Num2 <= Num1 and Num2 <= Num3:
    Menor = Num2
else:
    Menor = Num3

print(f"O maior número é {Maior}.")
print(f"O menor número é {Menor}.")