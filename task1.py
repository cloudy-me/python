# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division_func(var_1, var_2):
    if var_2 == 0:
        print("Division by zero!")
        return "impossible"
    else:
        return var_1 / var_2


try:
    input_1 = int(input("Enter first number: "))
    input_2 = int(input("Enter second number: "))
    print(f" Division of {input_1} by {input_2} is ", division_func(input_1, input_2))
except ValueError:
    print("Incorrect input")
