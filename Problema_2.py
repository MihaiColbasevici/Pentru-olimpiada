num = int(input("Dati un numar: "))
roman = ''
i = 0
conv = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'], [ 100, 'C'], [ 90, 'XC'], [ 50, 'L'], [ 40, 'XL'], [  10, 'X'], [  9, 'IX'], [  5, 'V'], [  4, 'IV'], [1, 'I']]
while num > 0:
    while conv[i][0] > num:
        i += 1
    roman += conv[i][1]
    num -= conv[i][0]
print(roman)