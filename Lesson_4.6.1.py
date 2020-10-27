"""
Реализовать скрипт: бесконечный итератор, генерирующий целые
числа, начиная с указанного.
Implement the script: an infinite iterator that generates
integers starting from the specified number.
"""


from sys import argv
from itertools import count

script_name, start, end = argv
for i in count(int(start)):
    if i > int(end):
        break
    print(i)
