from sys import argv

work_hour, pay_rate, bonus = argv[1:]
salary = int(work_hour)*int(pay_rate)+int(bonus)
print(f'Salary {salary}')


