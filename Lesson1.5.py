'''
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки
больше выручки). Выведите соответствующее сообщение. Если
фирма отработала с прибылью, вычислите рентабельность выручки
(соотношение прибыли к выручке). Далее запросите численность
сотрудников фирмы и определите прибыль фирмы в расчете на
одного сотрудника.
Request from the user amount of revenue and costs. Determine
the financial result of the company (profit - revenue is
greater than costs, or loss - costs are greater than revenue).
Display appropriate message. If the company has worked with
a profit, calculate the return on revenue (the ratio of
profit to revenue). Next, ask for the number of employees
and determine the company's profit per employee.
'''


a = int(input("Enter income - "))
b = int(input("Enter expenses - "))
if a < b:
    print("Sorry(( You have loss")
else:
    income = a - b
    rent = a / income
    print(f"Wow!!! You have profit. Your profitability is - {rent:.2f}")
    income = a - b
    workers = int(input("Enter number of workers - "))
    income_per_worker = income / workers
    print(f"Your income per worker is - {income_per_worker:.2f}")