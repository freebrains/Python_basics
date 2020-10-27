"""
*Реализовать структуру данных «Товары». Она должна представлять
собой список кортежей. Каждый кортеж хранит информацию об
отдельном товаре. В кортеже должно быть два элемента — номер
товара и словарь с параметрами (характеристиками товара: название,
цена, количество, единица измерения). Структуру нужно сформировать
программно, т.е. запрашивать все данные у пользователя.
Implement the "Products" data structure. It should be a list of
tuples. Each tuple stores information about a separate product.
The tuple must have two elements — the product number and a
dictionary with parameters (product characteristics: name, price,
quantity, unit of measurement). The structure needs to be formed
programmatically, i.e. request all data from the user.
"""


goods = []
n = 0
while True:
    pre_tuple = []
    name = input("Enter name of product or 'N' to escape - ")
    if name != "N":
        n += 1
        dictionary = {"название": name, "цена": int(input("Enter price - ")),
                      "количество": int(input("Enter quantity - ")), "единицы": input("Enter units - ")}
        pre_tuple.append(n)
        pre_tuple.append(dictionary)
        final_tuple = tuple(pre_tuple)
        goods.append(final_tuple)
    else:
        break
print(goods)
