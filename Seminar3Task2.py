# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
def couples(list):
    list1 = []
    count = -1
    i = 0
    lenf = len(list) / 2
    while i < lenf:
        list1.append(list[i]*list[count])
        count -= 1
        i += 1
    return list1


list = [2, 3, 4, 5, 6]
list1 = couples(list)
print(list)
print(list1)