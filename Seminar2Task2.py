# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial (num, count = 1):
    for a in range(1, num + 1):
        count *= a
    return count

n = int(input('Введите число: '))
print(f'Набор произведений чисел от 1 до {n} = ', end = '')
for a in range(1, n + 1):
    if a == n: 
        print(f'{factorial(a)}')
    else:
        print(f'{factorial(a)}', end = ', ')