# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

num = int(input("Введите количество чисел в списке: "))
sum = 0
n = {i : 3*i + 1 for i in range(1,num+1)}
print(f"Для n = {num}: {n}")

def sequence(num):
    return[round((1 + 1 / i)**i, 2) for i in range (1, num + 1)]          
print(f'Список для {num} чисел =',sequence(num))

for i in range(1, num + 1):
    sum += (1 + 1 / i) ** i
print(f'Сумма последовательности из {num} чисел равна: {str(sum)[:5]}')