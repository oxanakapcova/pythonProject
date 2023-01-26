# Задача 2: Найдите сумму цифр трехзначного числа. 123 -> 6 (1 + 2 + 3)   100 -> 1 (1 + 0 + 0)
value = int(input('type your 3-digits number: '))
if value < 100 or value > 999:
    print('Wrong number')
else:
    result = value % 10 + (value // 10) % 10 + value//100
    print(result)
