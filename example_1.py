n = int(input('Введите целое число: '))
print(hex(n)[2:])

def f_hex(s):
    number_f = ''
    while s > 0:
        number_f += str(s % 16)
        s //= 16
    return number_f[::-1]

print(f_hex(n))
if hex(n)[2:] == f_hex(n):
    print('Функция верна')
else:
    print('Функция ошибочна')