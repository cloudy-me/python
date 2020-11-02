# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.

from math import factorial


def generator():
    x = int(input('Enter integer: '))
    for num in range(1, x + 1):
        yield factorial(num)


fact = generator()
for el in fact:
    print(el)
