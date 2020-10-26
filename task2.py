# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

my_list=[]

while True:
    a = input ("Type + to add an element to the list: ")
    if a == "+":
        new_my_list = input ("Add new element to the list: ")
        my_list.append(new_my_list)
    else:
        break

print(f"Your input: {my_list}")

my_list_new=[]
len_my_list= len(my_list)

while len_my_list // 2 > 0:
    order_change= my_list[1::-1]
    my_list_new.extend(order_change)
    my_list.pop(0)
    my_list.pop(0)
    len_my_list = len(my_list)

if len_my_list % 2 == 1:
    my_list_new.extend(my_list)

print(f"Your output {my_list_new}")
