"""
Реализовать функцию, принимающую несколько параметров, описывающих
данные пользователя: имя, фамилия, год рождения, город проживания,
email, телефон. Функция должна принимать параметры как именованные
аргументы. Реализовать вывод данных о пользователе одной строкой.
Implement a function that uses several parameters describing the
user: first name, last name, year of birth, city of residence,
email, phone number. The function must use parameters as named
arguments. Implement the output of user data in a single line.
"""


def info_func(sec_name, first_name, birth_date, city, email, tel):
    print(f"Name - {sec_name}; First Name - {first_name}; Birth date - {birth_date}; City "
          f"of living - {city}; Email - {email}; Telephone - {tel}", end="")


info_func(sec_name=input("Enter your second name - "), first_name=input("Enter your first name - "), birth_date=input(
    "Enter your birth date - "), city=input("Enter your city of living - "), email=input("Enter you email address - "),
          tel=input("Enter your telephone number - ")
          )
