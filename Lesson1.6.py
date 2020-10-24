a = int(input("Enter initial km - "))
b = int(input("Enter limit km - "))
n = 0
while a < b:
    a = a + a * 0.1
    n += 1
print("On", n, "th day the sportsman reached result - not more", b, "km")