'''
# Задача №33. Решение в группах Хакер Василий получил доступ к классному журналу 
и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные –
на минимальные. Input: 5 -> 1 3 3 3 4 Output: 1 3 3 3 1
'''
def switch(li,max,count = 0):
    if count == len(li):
        return
    if li[count] == max:
        li[count] = min(li)
    return switch(li,max, count + 1)


list_v = [1, 4, 5, 1, 4,5]
max = max(list_v)

switch(list_v,max)
print(list_v)