# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

my_list = []
k = 1
a = '+'

while a == '+':
    name = input('Type product type: ')
    price = float(input('Type product price: '))
    quantity = int(input('Type product quantity: '))
    unit = input('Type units of measurement: ')
    my_dict = {'product type': name, 'price': price, 'quantity': quantity, 'units': unit}
    my_tuple = (k, my_dict)
    my_list.append(my_tuple)
    k += 1
    a = input ('Type + to add new product: ')

print('Available products: ', my_list)

# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.

name_list = []
price_list = []
quantity_list = []
unit_list = []
product_details = []

while len(my_list) > 0:
    for el in my_list[0]:
        product_details.append(el)
    product_dict = product_details[1]
    name_list.append(product_dict.get('product type'))
    price_list.append(product_dict.get('price'))
    quantity_list.append(product_dict.get('quantity'))
    unit_list.append(product_dict.get('units'))
    my_list.pop(0)
    print(product_details)
    product_details.clear()

product_dict = {'name':name_list,'price':price_list,'quantity':quantity_list,'unit':unit_list}
print('Products data: ', product_dict)

