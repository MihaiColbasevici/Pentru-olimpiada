n = int(input("Dati numarul de trepte: "))
pastila = 0
trepte = []
dif = 0
dif1 = []
for i in range(1, (n + 1)):
    tr = int(input())
    trepte.append(tr)
for i in range(0, (len(trepte) - 1)):
    if (abs(trepte[i] - trepte[i + 1]) > 1):
        pastila += 1
        dif = abs(trepte[i] - trepte[i + 1])
        dif1.append(dif)
if (pastila == 1):
    print("Piticul va avea nevoie de o pastila")
else:
    print("Piticul va avea nevoie de", pastila, "pastile")
print("Cea mai mare diferenta dintre inaltimi este", max(dif1))