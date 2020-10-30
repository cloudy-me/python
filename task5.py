# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def sum_function(my_list):
    my_result = 0
    for el in my_list:
        try:
            el = int(el)
            my_result = el + my_result
        except ValueError:
            break
    return my_result


my_sum = 0
decision = "Y"

while True:
    if decision.upper() == "Y":
        my_input = input("Enter a string of numbers divided by space: ")
        my_sum = my_sum + sum_function(my_input.split())
        print(f"Your result is {my_sum}")
        decision = input("Do you want to continue? If yes, type Y: ")
    else:
        break
