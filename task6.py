# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

with open('task6.txt') as my_file:
    my_dict = {}
    content = my_file.readlines()
    for line in content:
        subject = line[:line.find(':')]
        length = len(subject) + 2

        if line[length:length + 1] == '—':
            lection = 0
            length += 2
        else:
            lection = line[length:line.find('(')]
            length = line.find('л') + 3

        if line[length:length + 1] == '—':
            practice = 0
            length += 2
        else:
            practice = line[length:line.find('пр') - 1]
            length = line.find('пр') + 4

        if line[length:length + 1] == '—':
            lab = 0
        else:
            lab = line[length:line.find('лаб') - 1]

        total = int(lection) + int(practice) + int(lab)
        my_dict.update({subject: total})
    print(my_dict)
