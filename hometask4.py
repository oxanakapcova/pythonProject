#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый
#ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза
#больше журавликов,чем Петя и Сережа вместе?
#6 -> 1 4 1
#24 -> 4 16 4
#60 -> 10 40 10
value = int(input('type your value: '))
p = None #Petya
k = None #Katya
s = None #Serezha
# p + k + 2(p+k) = p + p + 2(2p) = 2p + 4p = 6p
p = value // 6
k = p
s = 2*(p+k) #or 4*p
print(f'Petya: {p}, Katya: {k}, Serezha: {s}')
