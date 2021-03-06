'''
Пользователь вводит время в секундах. Переведите время в часы,
минуты и секунды и выведите в формате чч:мм:сс. Используйте
форматирование строк.
The user enters the time in seconds. Transform the time in
hours, minutes and seconds and display like hh:mm:ss. Use
string formatting.
'''

time = int(input("Enter seconds"))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"{hours:02} : {minutes:02} : {seconds:02}")