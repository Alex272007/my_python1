A = int(input("Введите натуральное число A > 1 для определения по какому счету числом Фибоначчи оно является: "))

firstFib0, secondFib0 = 0,1
position = 1

while firstFib0 < A:
    firstFib0,secondFib0 = secondFib0,firstFib0 + secondFib0
    position += 1

if firstFib0 == A:
    print(f"Число {A} является числом Фибоначчи,Позиция - {position}")
else:
    print(f"Число не в ряду Фибоначчи, ближайшее число - {firstFib0}, занимающее позицию {position}")