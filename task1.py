# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

with open('text.txt', 'w+') as my_file:
    str_list = []
    my_line = "empty"
    while True:
        if my_line == "":
            break
        my_line = input('Enter your data: ')
        str_list.append(my_line)
        str_list.append('\n')
    my_file.writelines(str_list)
