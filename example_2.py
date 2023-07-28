#Решение поддерживает введение правильных дробей

import fractions


d1 = input('Введите перввую дробь: ')
d2 = input('Введите вторую дробь: ')
print('Функция (сложение):', fractions.Fraction(d1) + fractions.Fraction(d2))

ch_1 = int(d1[0])
zn_1 = int(d1[2])

ch_2 = int(d2[0])
zn_2 = int(d2[2])

if zn_1 == zn_2:
    ch = ch_1 + ch_2
    zn = zn_1
    if ch != zn:
        while ch % 2 == 0 and zn % 2 == 0:
            ch //= 2
            zn //= 2
        else:
            print(f"Мой код (сложение): {ch}/{zn}")
    else:
        print(f"Мой код (сложение): {ch//zn}")
else:
    ch = (ch_1 * zn_2) + (zn_1*ch_2)
    zn = zn_1 * zn_2
    print(f"Мой код (сложение): {ch}/{zn}")


print('Функция (умножение):', fractions.Fraction(d1) * fractions.Fraction(d2))

ch = ch_1 * ch_2
zn = zn_1 * zn_2
if ch != zn:
        while ch % 2 == 0 and zn % 2 == 0:
            ch //= 2
            zn //= 2
        else:
            print(f"Мой код (умножение): {ch}/{zn}")
else:
    print(f"Мой код (умножение): {ch//zn}")