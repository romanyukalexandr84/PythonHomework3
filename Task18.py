from random import randint

n = int(input("Введите размерность списка: "))
lst = [randint(0,20) for i in range(n)]
print(lst)

x = int(input("Задайте число x: "))
nearValue = lst[0]
for i in range(n):
    if abs(x - lst[i]) < abs(x - nearValue):
        nearValue = lst[i]
print(f"Самый близкий по величине элемент к числу {x} это элемент {nearValue}")