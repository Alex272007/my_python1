# Найти сумму всех цифр от 1 до введенного пользователем.

def calc_summa(n):
    res = 0
    while True:
        if n == 0:
            break
        res += n
        n -= 1
    return res

def calc_rec_summa(n):
    if n == 0:
        return 0
    return n + calc_rec_summa(n - 1)   # аналог 8,9,10 строчки кода

'''
calc_rec_summa(4)
1 этап - погружение
4 + (3 + (2 + (1 + 0)))

2 этап - всплытие
4 + (3 + 3 ) = 10 

'''

n = int(input("Введите натуральное число "))
print(calc_summa(n))
print(calc_rec_summa(n))