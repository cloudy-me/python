# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open('task3.txt') as my_file:
    content = my_file.readlines()
    total_salary = 0
    n = 0

    for el in content:
        space = el.find(" ")
        salary = float(el[space + 1:len(el) - 2])
        if salary < 20000:
            print(f'Salary {salary} of {el[:space]} is below 20,000')
        total_salary += salary
        n += 1
    print(f'Average salary is {total_salary / n:.2f}')
