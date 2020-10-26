'''
Спортсмен занимается ежедневными пробежками. В первый день
его результат составил a километров. Каждый день спортсмен
увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат
спортсмена составить не менее b километров. Программа должна
принимать значения параметров a и b и выводить одно натуральное
число — номер дня.
The athlete is engaged in daily jogging. On the first day the
result was a kilometers. Every day the athlete increased the
result by 10% relative to the previous one. Determine the number
of the day for which the total result is at least b kilometers.
The program must accept the values of parameters a nad b and
output a single natural number - the day number.
'''

a = int(input("Enter initial km - "))
b = int(input("Enter limit km - "))
n = 1
while a < b:
    a = a + a * 0.1
    n += 1
print("On", n, "th day the sportsman reached result - not more", b, "km")