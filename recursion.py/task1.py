'''
Задача №31. Решение в группах Последовательностью Фибоначчи называется последовательность 
чисел a0 , a1 , ..., an , ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). 
Требуется найти N-е число Фибоначчи Input: 7 Output: 21
'''
def find_fib_num(n):
    if n in (0, 1):
        return n
    return find_fib_num(n-2) + find_fib_num(n-1)
print(find_fib_num(7))

'''
n = int(input("Введите число: "))

def fib(n,a = 0,b = 1):
    if n == 0:
      return b
    return fib(n-1,b,a + b)

print(fib(n))
'''