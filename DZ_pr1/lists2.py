'''
Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k 
и вывести его.
Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - 
выведите его.
'''
n = int(input("Введите количество элементов: "))
list = []
for i in range(n):
    list.append(int(input("Введите число: ")))
print(list)
k = int(input("Введите искомое число: "))

result = list[0]

min_diff = abs(k - list[0])
for number in list:
    if abs(k - number) < min_diff:
        min_diff = abs(k - number)
        result = number
print(result)

    