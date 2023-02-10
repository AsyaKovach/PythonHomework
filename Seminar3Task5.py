# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

num = int(input('Введите число: '))
nedofibonacci = [1,-1]
fibonacci = [1,1]

for i in range(2,num):
    list = fibonacci[i-1]+fibonacci[i-2]
    fibonacci.append(list)
    list2 = nedofibonacci[i-2] - nedofibonacci[i-1]
    nedofibonacci.append(list2)

nedofibonacci.reverse()
fibonacci.insert(0, 0)

print(f' Для {num} => {nedofibonacci+fibonacci}')