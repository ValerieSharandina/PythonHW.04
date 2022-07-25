'''
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
Пример: при N = 12 -> [2, 3]
'''
n = int(input('задай число: '))
def Factor_number(n):
    result = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            result.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        result.append(n)
    return result
print(Factor_number(n))
# если задано число 12, то в ответ должно вывести 2, 2, 3. по тому что 2, 3 - это множители числа 6