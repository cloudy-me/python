# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операц.
number = int(input("Введите целое положительное число: "))
a = 0

while True:
    if number <=0:
        break
    else:
        digit = number % 10
        number = (number - digit) / 10
        if a < digit:
            a = digit

print("Самая большая цифра:",int(a))
