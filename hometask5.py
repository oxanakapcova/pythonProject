# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

value = int(input('type number: '))
if value < 1 or value > 4:
    print('wrong number')
elif value == 1:
    print('X > 0; Y > 0')
elif value == 2:
    print('X < 0; Y > 0')
elif value == 3:
    print('X < 0; Y < 0')
else:
    print('X > 0; Y < 0')