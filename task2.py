# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

with open('task2.txt') as my_file:
    content = my_file.readlines()
    for num, line in enumerate(content, 1):
        print(line.strip())
        space = line.count(" ") + 1
        print(f'In line {num} there are {space} words')
print(f'Number of rows in the file - {num}')
