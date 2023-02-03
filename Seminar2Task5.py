#Реализуйте алгоритм перемешивания списка

import random
page = [0,1,2,3,4,5,6,7,8,9]
print ("Начальный список: " + str(page))
for i in range(len(page)-1, 0, -1):
    j = random.randint(0, i + 1) 
    page[i], page[j] = page[j], page[i] 
print ("Перемешанный список: " +  str(page))