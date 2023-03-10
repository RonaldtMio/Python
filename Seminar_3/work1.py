# # Вариант 1. Пример решения с заданным массивом.


# n = int(input('Введите длину массива: '))
# array = [i for i in range(1, n + 1)]
# x = int(input('Введите число: '))
# list = []

# for i in range(0, len(array)):
#     if i == x:
#         list.append(array[i])
# print(len(list))

# Вариант 2. Пример решения с введенным масивом.

n = int(input('Введите длину массива: '))
array = [int(input('Введите элементы массива: ')) for i in range(0, n)]
x = int(input('Введите число: '))
count = 0

print(array)
for i in range(0, len(array)):
    if array[i] == x:
        count += 1
print(f"Число {x} встречается в массиве {count} раз(а)")
