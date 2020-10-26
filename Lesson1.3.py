'''
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
Ask the user number n. Calculate sum of n + nn + nnn.
For example, the user entered number 3. Calculating
3 + 33 + 333 = 369.
'''


n = input("Enter n ")
n1 = n + n
n2 = n + n + n
a = int(n)
b = int(n1)
c = int(n2)
sum = a + b + c
print(sum)