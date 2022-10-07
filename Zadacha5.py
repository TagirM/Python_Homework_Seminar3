# Задача 5.
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


countFibo = input("Введите количество чисел Фибоначчи после нуля: ")
while isint(countFibo) == False:
    countFibo = input('Введите количество чисел Фибоначчи после нуля: ')
countFibo = int(countFibo)
fiboListRight = [0 for elem in range(countFibo+1)]
fiboListRight[0] = 0
fiboListRight[1] = 1
for elem in range(2, countFibo+1):
    fiboListRight[elem] = fiboListRight[elem-1]+fiboListRight[elem-2]
# print(fiboListRight)
fiboListLeft = [0 for elem in range(countFibo)]
fiboListLeft[0] = 1
fiboListLeft[1] = -1
for elem in range(2, countFibo):
    fiboListLeft[elem] = fiboListLeft[elem-2]-fiboListLeft[elem-1]
fiboListLeft=fiboListLeft[::-1]
# print(fiboListLeft)
print(f'Список чисел Фибоначчи: {fiboListLeft+fiboListRight}')