'''
Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
Найдите количество и выведите его.
'''
n = int(input("Введите количество элементов : "))
list_1 = []
for i in range(n):
    list_1.append(int(input("Введите число: ")))
print(list_1)
k = 3
count = 0 # кол-во элементов k
i = 0
while i < len(list_1):
    if list_1[i] == k:
        count += 1
    i += 1        
print(count)
