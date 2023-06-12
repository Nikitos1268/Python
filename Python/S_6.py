# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def arithmetic_progression(start, step, quantity):
    arr = [start]
    for i in range(1,quantity):
        arr.append(arr[i-1] + step)
    return arr

print(arithmetic_progression(7,2,5)) 


# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

def task(array, min, max):
    res = []
    for i in range(len(array)):
        if max >= array[i] >= min:
            res.append(i)
    return res
arr =[-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
print(task(arr,5,14))


# Promo dicosion
# Задача 30

#a1 = int(input())
#d = int(input())
#n = int(input())
#for i in range(n):
#print(a1 + i * d)

# Задача 32
#list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
#min_number = int(input())
#max_number = int(input())
#for i in range(len(list_1)):
#if min_number <= list_1[i] <= max_number:
#print(i)


import time
while True:
    print("\nПрограмма скоро закроется!")
    time.sleep(10)
    exit()