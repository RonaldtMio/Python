N = int(input('Введите количество монеток: '))
eagle = 0
tail = 0

for i in range(N):
    coin = int(input('1 - орел, 0 = решка: '))
    if coin == 0:
        tail += 1
    elif coin == 1:
        eagle += 1
    else:
        print('Введите 0 или 1!!!')
if eagle > tail:
    print(tail)
elif tail >= eagle:
    print(eagle)