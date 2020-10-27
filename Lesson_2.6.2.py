"""
Необходимо собрать аналитику о товарах. Реализовать словарь, в
котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список
названий товаров.
Collect analytics about products. Implement a dictionary where
each key is a product characteristic, such as a name, and the
value is a list of characteristic values, such as a list of
product names.
"""


product_name = []
price = []
qty = []
units = []
while True:
    name = input("Enter name of product or 'N' to escape - ")
    if name != "N":
        lib_1 = [name, int(input("Enter price - ")), int(input("Enter quantity - ")), input("Enter units - ")]
        product_name.append(lib_1[0])
        price.append(lib_1[1])
        qty.append(lib_1[2])
        units.append(lib_1[3])
    else:
        break
library = {"название": product_name, "цена": price, "количество": qty, "ед.": units}
print(library)
