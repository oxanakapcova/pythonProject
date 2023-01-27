# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример: - 6 -> да - 7 -> да - 1 -> нет
day_number = int(input('type day number: '))
if day_number > 7 or day_number < 1:
    print('wrong number')
elif day_number == 6 or day_number == 7:
    print("Yes")
else:
    print("No")
