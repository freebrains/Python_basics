"""
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к
какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
The user enters the month as an integer from 1 to 12. Output what
time of the year the month belongs to (winter, spring, summer, autumn).
Write solution using dict and list.
"""

my_dict = {1: "Winter", 2: "Still winter", 3: "Spring", 4: "Spring", 5: "Oh, finally spring", 6: "Hooray!! It's Summer",
           7: "Summer", 8: "Summer", 9: "Autumn", 10: "Autumn", 11: "Autumn. Winter is coming!", 12: "God no!! Winter"}
month = int(input("Enter month using digit - "))
print(my_dict.get(month))
