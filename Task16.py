from random import randint

n = int(input("Введите размерность списка: "))
lst = [randint(0,9) for i in range(n)]
print(lst)

x = int(input("Введите искомое число: "))
count = 0
for i in range(n):
    if lst[i] == x:
        count+=1
print(f"Число {x} встречается в списке {count} раз")