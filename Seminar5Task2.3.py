# Реализация игры (с конфетами), человек против бота c "интеллектом":

from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, quantity):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {quantity} конфет.")


def bot_calc(quantity):
    k = randint(1,29)
    while quantity-k <= 28 and quantity > 29:
        k = randint(1,29)
    return k

gamer1 = input("Введите имя первого игрока: ")
gamer2 = "Bot"
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
        k = bot_calc(quantity)
        counter2 += k
        quantity -= k
        flag = True
        p_print(gamer2, k, counter2, quantity)

if flag:
    print(f"Поздравляю! В этот раз победил {gamer1}")
else:
    print(f"Поздравляю! В этот раз победил {gamer2}")