'''
В фермерском хозяйстве в Карелии выращивают чернику. Черника растет на круглой грядке, 
и кусты черники высажены по окружности грядки. Каждый куст черники имеет урожайность, 
которая соответствует количеству ягод на этом кусте.
Урожайность черничных кустов представлена в виде списка arr, где arr[i] - это урожайность 
(количество ягод) i-го куста.
В фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит 
из управляющего модуля и нескольких собирающих модулей. Каждый собирающий модуль может 
собрать ягоды с одного куста и с двух соседних кустов. Собирающий модуль находится перед 
определенным кустом, и он может выбирать, с какого куста начать сбор ягод.
Ваша задача - написать программу, которая определит максимальное число ягод, которое может 
собрать один собирающий модуль за один заход, находясь перед некоторым кустом грядки.

Входные данные:
На вход программе подается список arr, где arr[i] (1 ≤ arr[i] ≤ 1000) - урожайность i-го 
куста черники. Размер списка не превышает 1000 элементов.

Выходные данные:
Программа должна вывести одно целое число - максимальное количество ягод, которое может 
собрать собирающий модуль, находясь перед некоторым кустом грядки.
'''
n = int(input("Введите урожайность 1-го куста черники: "))

arr = [int(input("Введите число: ")) for i in range(n)]
print(arr)

