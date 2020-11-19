k = int(input("Dati suma: "))
suma = 0
tot = 0
while (suma <= k):
    num = int(input("n = "))
    if (num % 2 == 0):
        suma += num
    tot += 1
print(tot, "numere \t", suma, "in total")