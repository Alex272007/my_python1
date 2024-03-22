'''
задача 2 необязательная.
Пользователь вводит натуральное k. Надо сформировать многочлен такой степени, где все коэффициенты 
случайные от -10 до 10.

например, k=2 -> -x^2 + 3*x - 8 = 0
тут коэффициенты -1,3,-8
например, k=3 -> 3*x^3 - 2*x = 0
тут коэффициенты 3,0,-2,0
'''
import random

def create_coefficients(k):
    coeffs = [random.randint(-10, 10) for _ in range (k + 1)]
    return coeffs
def generate_single_coeff(coeff):
    