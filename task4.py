# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def my_func(base, power):
    my_result = base ** power
    return my_result


def my_exponentiation(base, power):
    result = base
    i = 1
    while i < abs(power):
        result = result * base
        i += 1
    return 1 / result


try:
    x = int(input("Enter a positive number: "))
    y = int(input("Enter a negative number: "))
    if x <= 0 or y >= 0:
        print("Wrong input!")
    else:
        print(f"{x} in the power of {y} is {my_func(base=x, power=y)}")
        print(f"{x} in the power of {y} is {my_exponentiation(x, y)}")
except ValueError:
    print("Incorrect input!")
