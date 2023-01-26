#Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается
#сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
n = int(input('type value of n: '))
m = int(input('type value of m: '))
k = int(input('type value of k: '))
if (k % n == 0 or k % m == 0) and k < n*m:
    print('Yes')
else:
    print('No')
