# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('task5.txt', 'w+') as my_file:
    numbers = input('Enter your series of numbers: ')
    my_file.writelines(numbers)
    my_file.seek(0)
    content = my_file.read()
    cum_sum = 0
    for el in content.split():
        cum_sum += int(el)
    print(f'Sum of your numbers is {cum_sum}')

