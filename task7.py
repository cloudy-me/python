# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.

import json

with open('task7.txt') as my_file:
    dict_profit = {}
    my_list = []
    total_prof = 0
    n = 0

    content = my_file.readlines()
    for line in content:
        print(line.split())
        firm_name, organisation, revenue, loss = line.split()
        profit = float(revenue) - float(loss)
        dict_profit.update({firm_name: profit})
    print(f'Profit result {dict_profit}')
    my_list.append(dict_profit)

    profit_value = dict_profit.values()
    for el in profit_value:
        if el > 0:
            total_prof += el
            n += 1
    av_profit = int(total_prof / n)
    dict_av_profit = {'average profit': av_profit}
    my_list.append(dict_av_profit)
    print(my_list)

with open('my_new_file.json', 'w') as write_f:
    json.dump(my_list, write_f)
