# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func():
    var_1 = int(input("Enter first number: "))
    var_2 = int(input("Enter second number: "))
    var_3 = int(input("Enter third number: "))
    sum_result = max(var_1, var_2) + max(var_2, var_3)
    return sum_result


try:
    print("Sum of the two largest numbers is ", my_func())
except ValueError:
    print("Incorrect input")
