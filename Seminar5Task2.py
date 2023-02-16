# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint # человек с человеком

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, quantity):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {quantity} конфет.")

gamer1 = input("Введите имя первого игрока: ")
gamer2 = input("Введите имя второго игрока: ")
quantity = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первый ходит {gamer1}")
else:
    print(f"Первый ходит {gamer2}")

counter1 = 0 
counter2 = 0

while quantity > 28:
    if flag:
        k = input_dat(gamer1)
        counter1 += k
        quantity -= k
        flag = False
        p_print(gamer1, k, counter1, quantity)
    else:
        k = input_dat(gamer2)
        counter2 += k
        quantity -= k
        flag = True
        p_print(gamer2, k, counter2, quantity)

if flag:
    print(f"Поздравляю! В этот раз победил {gamer1}")
else:
    print(f"Поздравляю! В этот раз победил {gamer2}")