# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count, cycle

for el in count(3):
    if el > 9:
        break
    else:
        print(f'List count {el}')

c = 0
for el in cycle([10, 20, 30]):
    if c > 5:
        break
    print(f'List cycle {el}')
    c += 1
