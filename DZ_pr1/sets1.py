'''
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без 
повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
На вход подается 2 числа через пробел: n m
n - кол-во элементов первого множества.
m - кол-во элементов второго множества.
Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо
''' 
n = int(input("Введите сколько элементов: "))
m = int(input("Введите сколько элементов: "))

# var2 = []
# for i in range(n):
#     var2.append(int(input("Введите число: ")))
# print(var2)
var2 = [int(input("Введите число: ")) for i in range(n)]
print(var2)

# var3 = []
# for i in range(m):
#     var3.append(int(input("Введите число: ")))
# print(var3)
var3 = [int(input("Введите число: ")) for i in range(m)]
print(var3)

set1 = set(var2)
set2 = set(var3)
intersection = list(set1.intersection(set2))
intersection.sort()
intersec = " ".join(str(i) for i in intersection)
print(intersec)