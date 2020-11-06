# 4. Создать (не программно) текстовый файл со следующим содержимым:
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

with open('task4.txt') as my_file:
    content = my_file.readlines()
    content_new = []
    for num, el in enumerate(content, 1):
        if num == 1:
            el = el.replace('One', 'один')
        elif num == 2:
            el = el.replace('Two', 'два')
        elif num == 3:
            el = el.replace('Three', 'три')
        else:
            el = el.replace('Four', 'четыре')
        content_new.append(el)

with open('task4_new.txt','w') as my_file_new:
    my_file_new.writelines(content_new)
