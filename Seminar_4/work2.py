beds = int(input('Введите количество кустов на грядке: '))
berries = list(map(int, input('Введите количество ягод на каждом из кустов через пробел: ').split(' ')[:(beds)]))
res = []

for i in range(len(berries) - 1):
    res.append(berries[i - 1] + berries[i] + berries[i + 1])
res.append(berries[-2] + berries[-1] + berries[0])
print(max(res))