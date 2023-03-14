num_1 = int(input('Введите количество элементов первого множества через пробел: '))
num_2 = int(input('Введите количество элементов второго множества через пробел: '))

array_1 = list(map(int, input().split(' ')[:num_1]))
array_2 = list(map(int, input().split(' ')[:num_2]))
res = []


for i in array_1:
    for j in array_2:
        if i == j and (i or j) not in res:
            res.append(i)
            break
res = sorted(res)
print(res)