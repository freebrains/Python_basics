number = int(input("Enter the number - "))
a = number % 10
high = a
while True:
    number = number // 10
    if number % 10 != 0:
       a = number % 10
       if a >= high:
           high = a
       else:
            high = high
       continue
    else:
        break
print(high)