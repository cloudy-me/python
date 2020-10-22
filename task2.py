# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
time = int(input("Введите время в секундах:"))
hours = time // 3600
less_hour = time % 3600
minutes = less_hour // 60
seconds = less_hour % 60

if hours > 24:
    days = hours // 24
    hours = hours % 24
else:
    days = 0

if hours <10:
    hours = "0" + str(hours)

if minutes < 10:
    minutes = "0" + str(minutes)

if seconds < 10:
    seconds = "0" + str(seconds)

print(f"{days} days, time {hours}:{minutes}:{seconds}")