# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def personal_data(**kwargs):
    print(f"Thank you! Your data is: {kwargs}")


user_name = input("Enter your name: ")
user_surname: str = input("Enter your surname: ")
user_birth = int(input("Enter your year of birth: "))
user_city = input("Enter your city of residence: ")
user_email = input("Enter your email: ")
user_mob = input("Enter your phone number: ")

personal_data(name=user_name, surname=user_surname, birth_year=user_birth, city=user_city, email=user_email,
              mob=user_mob)
