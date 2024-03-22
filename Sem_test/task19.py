'''
Задача №19.
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 2
Output: [4, 5, 1, 2, 3]

'''
# # Создание списка чисел
# numbers = [1, 2, 3, 4, 5]

# # Определение K
# K = -3 # Можно изменить знак K для тестирования

# # Проверка знака K и определение направления сдвига
# if K > 0:
#     # Сдвиг вправо
#     last_k_elements = numbers[-K:]
#     first_n_k_elements = numbers[:-K]
#     shifted_numbers = last_k_elements + first_n_k_elements
# elif K < 0:
#     # Сдвиг влево
#     K = abs(K) # Преобразование K в положительное число для сдвига влево
#     last_k_elements = numbers[K:]
#     first_n_k_elements = numbers[:K]
#     shifted_numbers = first_n_k_elements + last_k_elements
# else:
#     # Если K равно 0, список остается без изменений
#     shifted_numbers = numbers

# # Вывод результата
# print(shifted_numbers)

list_1 = [1, 2, 3, 4, 5]
k = int(input("Введите сдвиг ")) % len(list_1)
# list_2 = list_1[-k: ] + list_1[:-k]
# print(list_2)

for i in range(k):
    a = list_1.pop()
    list_1.insert(0,a)
print(list_1)