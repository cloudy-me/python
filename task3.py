# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

try:
    month = int(input("Please, type month number: "))
    if ( month <= 12 and month >= 1) == True:
        for el in winter:
            if el == month:
                print(f'month {month} is in winter')

        for el in spring:
            if el == month:
                print(f'month {month} is in spring')

        for el in summer:
            if el == month:
                print(f'month {month} is in summer')

        for el in autumn:
            if el == month:
                print(f'month {month} is in autumn')

        seasons = {1: "зима", 2: "зима", 3: "весна", 4: "весна", 5: "весна", 6: "лето", 7: "лето", 8: "лето",
                   9: "осень", 10: "осень", 11: "осень", 12: "зима"}
        print(f"месяц {month} попадает на время года {seasons.get(month)}")
    else:
        print("This month does not exist")
except:
    print ("Incorrect input")
