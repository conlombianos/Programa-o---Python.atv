prime = 0

for num in range(2, 10**6):
    Nprimo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            Nprimo = False
            break
    if Nprimo:
        print(num)
        prime += 1
    if prime == 100:
        break