'''
Задача 28: Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел. Из
всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.
Пример:
2 2
4
'''
def sum(a, b):
    # Базовый случай: если одно из чисел равно 0, возвращаем другое число
    if a == 0:
        return b
    elif b == 0:
        return a
    # Рекурсивный случай: уменьшаем одно из чисел на 1 и рекурсивно вызываем функцию sum()
    else:
        return sum(a + 1, b - 1)
    
a = int(input("Введите число: "))
b = int(input("Введите число: "))

print(sum(a, b))