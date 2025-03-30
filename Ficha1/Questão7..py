apar = int(input("Digite um número ímpar: "))

if apar % 2 == 0:
    print("Coloque um número ímpar.")

else:
    antImpar = 0
    proxImpar = 0
    for i in range(apar - 1, apar + 2):
        if i < apar and i % 2 != 0:
            antImpar = i
        elif i > apar and i % 2 != 0:
            proxImpar = i

 
    diferenca = proxImpar**2 - antImpar**2
    print(f"A diferença entre o quadrado de {proxImpar} e {antImpar} é {diferenca}.")
