# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint
 
ha, na = 3, 8
data = [randint(1, 10) for _ in range(20)]
print("Изначальный список:", data, sep='\n')
indexes = [i for i, v in enumerate(data) if ha <= v <= na]
print("Индекс:", indexes, sep='\n')
result = []
i = len(indexes)
while i :
    i -= 1
    result.append(data.pop(indexes[i]))
print("Оставшиеся элементы:", data, sep='\n')
print("Необходимые элементы:", result, sep='\n')