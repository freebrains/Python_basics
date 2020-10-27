"""
Реализовать скрипт: бесконечный итератор, повторяющий
элементы некоторого списка, определенного заранее.
Implement a script: an infinite iterator that repeats
the elements of a certain list defined in advance.
"""


from itertools import cycle

c = 0
for el in cycle([34532, 45, 236347, 'A']):
    if c > 14:
        break
    print(el)
    c += 1