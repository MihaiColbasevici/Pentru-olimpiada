n1 = int(input("Dati un numar: "))
n2 = int(input("Dati un alt numar: "))
c = 0
if (n1 > 1) and (n1 < 9999) and (n2 > 1) and (n2 < 9999):
    n1 = str(n1)
    n2 = str(n2)
    if (len(n1) == 4) and (len(n2) == 4):
        if (n1[0] != n2[0]):
            c += 1
        if (n1[1] != n2[1]):
            c += 1
        if (n1[2] != n2[2]):
            c += 1
        if (n1[3] != n2[3]):
            c += 1
    if (len(n1) == 3) and (len(n2) == 3):
        if (n1[0] != n2[0]):
            c += 1
        if (n1[1] != n2[1]):
            c += 1
        if (n1[2] != n2[2]):
            c += 1
    if (len(n1) == 2) and (len(n2) == 2):
        if (n1[0] != n2[0]):
            c += 1
        if (n1[1] != n2[1]):
            c += 1
    if (len(n1) == 1) and (len(n2) == 1):
        if (n1[0] != n2[0]):
            c += 1
print(c, "numere trebuiesc schimbate.")