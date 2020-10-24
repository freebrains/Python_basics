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