x = int(input('Введите сумму двух чисел: '))
y = int(input('Введите произведение двух чисел: '))
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(f"Ваши числа: {i}, {j}")