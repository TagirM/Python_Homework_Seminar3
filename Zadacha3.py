# Задача 3.
# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform


def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


countElem = input('Введите количество элементов списка: ')
while isint(countElem) == False:
    countElem = input('Введите количество элементов списка: ')
countElem = int(countElem)
myList = []
for elem in range(countElem):
    myList.append(round(uniform(1, 9), 2))
print(f'Список из вещественных чисел: {myList}')
floatList = []
for elem in range(countElem):
    floatList.append(round(myList[elem] % 1, 2))
print(f'Список из дробей чисел: {floatList}')
print(
    f'Разница между максимальным и минимальным значением дробной части элементов: {round(max(floatList)-min(floatList),2)}')
