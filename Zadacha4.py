# Задача 4.
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


decimalNumber = input("Введите любое десятичное целое число: ")
while isint(decimalNumber) == False:
    decimalNumber = input('Введите любое десятичное целое число: ')
decimalNumber = int(decimalNumber)
lenghtList = decimalNumber
countElem = 0
while (lenghtList > 0):
    lenghtList = lenghtList // 2
    countElem += 1
binaryNumber = []
for elem in range(countElem):
    binaryNumber.append(decimalNumber % 2)
    decimalNumber = decimalNumber // 2
print('Преобразованное двоичное число: ')
print(*binaryNumber[::-1])
