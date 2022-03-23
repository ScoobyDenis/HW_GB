# 1. Реализовать скрипт, в котором должна быть предусмотрена функция
# расчёта заработной платы сотрудника. Используйте в нём формулу:
# (выработка в часах*ставка в час) + премия. Во время выполнения
# расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

def salary(hours, rate, premium):
    return hours * rate + premium

path, hours, rate, premium = argv
hours, rate, premium = map(int, argv[1:])
print("Salary:", salary(hours, rate, premium))