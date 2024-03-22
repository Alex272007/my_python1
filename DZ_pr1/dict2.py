'''
Задача №25. Общее обсуждение
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

'''
# def track_duplicates(input_string):
#     # Создаем словарь для отслеживания количества повторений символов
#     char_count = {}
    
#     # Разбиваем входную строку на символы
#     characters = input_string.split()
    
#     # Создаем список для хранения результата
#     result = []
    
#     for char in characters:
#         # Если символ встречается впервые, добавляем его в результат
#         if char not in char_count:
#             result.append(char)
#             char_count[char] = 1
#         else:
#             # Если символ уже встречался, добавляем его с постфиксом "_n"
#             count = char_count[char]
#             result.append(f"{char}_{count}")
#             char_count[char] += 1
    
#     # Преобразуем список в строку и возвращаем результат
#     return " ".join(result)

# # Пример использования
# input_string = "a a a b c a a d c d d"
# output_string = track_duplicates(input_string)
# print(output_string)

str1 = 'a a a b c a a d c d d '.split()
dict1 ={}
for letter in str1:
    if letter not in dict1:
        dict1[letter] = 0 
        print(letter, end = " " )
    else: 
        dict1[letter] += 1 
        print(f'{letter}_{dict1[letter]}', end = " ")