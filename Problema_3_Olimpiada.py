n = int(input("Dati numarul de pe usa: "))
cheia = 0
suma = 0
prim = 0
# divizorii si suma lor
for x in range(1, ((n // 2) + 1)):
    if (n % x == 0):
        suma += x
# daca suma este un numar prim
if (suma > 1):
    for k in range(2, ((suma // 2) + 1)):
        if (suma % k == 0):
            break
        else:
            prim = 1
# suma cifrelor numarului
if (prim == 1):
    for x in str(suma):
        cheia += int(x)
else:
    for x in str(n):
        if (int(x) % 2 != 0):
            cheia += int(x)
print(cheia)