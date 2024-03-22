# import random


# NUM_CLASSES = 10


# def show_avg_value(sp):
#     avg = sum(sp) / len(sp)
#     print(avg)

# def calc_avg_value(sp):
#     avg = sum(sp) / len(sp)
#     return avg



# sp = [1,3,5,7,9]

# show_avg_value(sp)
# print(calc_avg_value(sp))

import random


NUM_CLASSES = 10


def show_avg_value(sp):
    avg = sum(sp) / len(sp)
    print(avg)

def calc_avg_value(sp: list) -> float:
    '''
    Эта функция вычисляет среднее арифметическое списка
    '''
    # надо проверить список или нет, и если нет то будем ругаться - выдавать ошибку
    if not isinstance(sp, list):
        raise TypeError("На входе должен быть список")
        # print("На входе должен быть список")
        # return 
    avg = sum(sp) / len(sp)
    return avg



sp = [1,3,5,7,10]
# show_avg_value(sp)
# print(calc_avg_value(sp))
t = tuple(sp)
try:
    print(calc_avg_value(t))
except TypeError as te:
    print(te)
# print(calc_avg_value.__doc__)