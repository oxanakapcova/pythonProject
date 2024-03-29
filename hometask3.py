# Напишите программу, которая принимает на вход координаты
# точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в
# которой находится эта точка (или на какой оси она находится).
# Пример: - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('type X: '))
y = int(input('type Y: '))
# solution 1
if x > 0 and y > 0:
    print('1')
elif x > 0 > y:
    print('4')
elif x < 0 and y < 0:
    print('3')
else:
    print('2')

# solution 2
if x > 0:
    if y > 0:
        print('1')
    else:
        print('4')
else:
    if y > 0:
        print('2')
    else:
        print('3')
