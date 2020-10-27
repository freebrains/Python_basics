"""
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к
какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
The user enters the month as an integer from 1 to 12. Output time
of year the month belongs to (winter, spring, summer, autumn).
Write solutions using list and dict.
"""


m_list = ["winter", "winter", "spring", "spring", "spring", "summer", "summer", "summer", "autumn", "autumn", "autumn",
          "winter"]
month = int(input("Enter any month in digit - "))
print(m_list[month - 1])
