# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

num = int(input('Введите десятичное число:'))
num_two = ' '

while num != 0:
    num_two = str(num % 2) + num_two
    num //= 2
print(f'Двоичное число - {num_two}')