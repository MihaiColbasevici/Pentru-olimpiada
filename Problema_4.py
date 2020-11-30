s = str(input("Dati un cuvant: "))
vocala = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
for i in vocala:
    s = s.replace(i, 'p' + i)
print(s)

s1 = str(input("Dati un cuvant codificat: "))