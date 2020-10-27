# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

my_list = [5, 7, 3, 2, 3]
print('Input: ', my_list)

my_list.sort (reverse=True)
print('Sorted list: ', my_list)

try:
    number = int(input('Type positive number: '))
    if number > 0:
        my_list.append(number)
        my_list.sort (reverse=True)
        print('New sorted list: ', my_list)
    else:
        print('Incorrect input. Try one more time')
except ValueError:
    print("Type a positive number!")

