n = int(input("Введите значение n: "))
m = int(input("Введите значение m: "))
k = int(input("Введите значение k: "))

if k % n == 0 or k % m == 0:
    print("Yes")
else:
    print("No")