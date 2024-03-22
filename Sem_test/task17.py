'''
Задача №17. 
Дан список чисел. Определите, сколько в нем
встречается различных чисел.

'''
# print([i for i in range(5)])
# print([(i, i ** 2) for i in range(5)])
# print([i for i in range(11) if i %2 == 0])

# list1 = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(list1)))

n = int(input("Введите количество элементов: "))
data = []
for i in range(n):
    data.append(int(input("Введите число: ")))
print(data)
print(len(set(data)))