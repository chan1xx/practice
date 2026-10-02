n = int(input())
if n % 2 == 0:
    print("четное")
else:
    print("нечетное")
if n > 0:
    print("положительное")
elif n == 0:
    print("ноль")
else:
    print("отрицательное")
if n in range(10, 51):
    print("принадлежит диапазону [10, 50]")
else:
    print("не принадлежит диапазону [10, 50]")
