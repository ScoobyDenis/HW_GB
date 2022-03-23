# 1. Создать программный файл в текстовом формате, записать в него построчно
# данные, вводимые пользователем. Об окончании ввода данных будет
# свидетельствовать пустая строка.

file = open('animals.txt', 'w', encoding='utf-8')

s = " "
while s != '':
    s = input("enter animal: ")
    file.write(s + '\n')
file.close()

file = open('animals.txt', 'r', encoding='utf-8')
animals = file.read()
print(animals)
file.close()

# 2. Создать текстовый файл (не программно), сохранить
# в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

f = open('poem.txt', 'r', encoding='utf-8')
string_count = 0
print(f.read())
print()
f.close()
f = open('poem.txt', 'r', encoding='utf-8')
for line in f:
    string_count += 1
    line = line.split()
    print(f'{string_count} строка содержит {len(line)} слов(a)')

f.close()

# 3. Создать текстовый файл (не программно). Построчно записать
# фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести
# фамилии этих сотрудников. Выполнить подсчёт средней величины
# дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32

with open('salary.txt', 'r', encoding='utf-8') as salary:
    print(salary.read())
print()
with open('salary.txt', 'r', encoding='utf-8') as salary:
    l = []
    total = 0
    count = 0
    for line in salary:
        line = line.split()
        total += float(line[1])
        count += 1
        if float(line[1]) < 20000:
            l.append(line[0])

print("Средняя зарплата сотрудников: ", total/count)
print("Оклад меньше 20000 у следующих сотрудников: ", end='')
print(*l, sep=', ')

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую
# построчно данные. При этом английские числительные должны
# заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.

d = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
d_list = []
with open('digits.txt', 'r', encoding='utf-8') as digits:
    for i in digits:
        i = i.split()
        d_list.append(d[i[0]] + ' - ' + i[2])

with open('цифры.txt', 'w', encoding='utf-8') as new_digits:
    for el in d_list:
        new_digits.write(el)
        new_digits.write('\n')

rus_digits = open('цифры.txt', 'r', encoding='utf-8')
t = rus_digits.read()
print(t)
rus_digits.close()

# 5. Создать (программно) текстовый файл, записать в него
# программно набор чисел, разделённых пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить её на экран.

try:
    with open('nums.txt', 'w+', encoding='utf-8') as sum_nums:

        num = input("Enter digits separated by spaces: ")
        sum_nums.writelines(num)
        my_nums = num.split()

        print("Sum of numbers:", sum(map(int, my_nums)))
except ValueError:
    print('You need to enter only integers')
# 5. Создать (программно) текстовый файл, записать в него
# программно набор чисел, разделённых пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить её на экран.

try:
    with open('nums.txt', 'w+', encoding='utf-8') as sum_nums:

        num = input("Enter digits separated by spaces: ")
        sum_nums.writelines(num)
        my_nums = num.split()

        print("Sum of numbers:", sum(map(int, my_nums)))
except ValueError:
    print('You need to enter only integers')


# 6. Сформировать (не программно) текстовый файл. В нём каждая
# строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету. Сюда должно
# входить и количество занятий. Необязательно, чтобы для каждого
# предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

def int_clear(s):
    try:
        for i in s:
            if i in "().—-',';:" or i.isalpha():
                s = s.replace(i, '')
        if s != None:
            return int(s)
    except ValueError:
        pass


sub = []
hours = []
with open('subs.txt', 'r+', encoding='utf-8') as subjects:
    for line in subjects:
        subject, lecture, practice, laboratory = line.split()
        sub.append(subject[:-1])
        hours.append(int_clear(lecture) + int_clear(practice) + int_clear(laboratory))

d = dict(zip(sub, hours))
print(d)
# не смог избавиться от значений None и при сложении ошибку выдает

# 7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.

# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
#  а также среднюю прибыль. Если фирма получила убытки, в расчёт средней
# прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их
# прибылями, а также словарь со средней прибылью. Если фирма получила
# убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
#                 {“average_profit”: 2000}].

# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import json

with open('firm_info.txt', 'w', encoding='utf-8') as firms:
    firms.write('Coca-cola ООО 1500000 300000 \n')
    firms.write('Pepsi ООО 1450000 300000 \n')
    firms.write('Ikea ООО 1300000 350000 \n')
    firms.write('Ivanov ИП 100000 150000 \n')
with open('firm_info.txt', 'r', encoding='utf-8') as firms:
    profit = []
    no_profit = []
    average = []
    average_profit = []
    for i in firms:
        i = i.split()
        x = int(i[2]) - int(i[3])
        if x > -1:
            profit.append(i[0])
            profit.append(x)
            average.append(x)
        else:
            no_profit.append(i[0])
            no_profit.append(x)
    average_profit.append('average_profit')
    average_profit.append(int(sum(average) / len(average)))


def list_for_dict(l):
    d = {}
    a = l[::2]
    b = l[1::2]
    d = dict(zip(a, b))
    return d


profit = list_for_dict(profit)
no_profit = list_for_dict(no_profit)
average_profit = list_for_dict(average_profit)

d_json = []
d_json.append(profit)
d_json.append(no_profit)
d_json.append(average_profit)

with open('new_json.json', 'w', encoding='utf-8') as firms:
    json.dump(d_json, firms)

str_js = json.dumps(d_json)
print(str_js)