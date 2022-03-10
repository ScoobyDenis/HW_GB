# ''' 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать
# функцию type() для проверки типа. Элементы списка можно не запрашивать
# у пользователя, а указать явно, в программе.
# '''

my_list = [23.45, False, 2, [1,2,3], 'shshshs', {1,2,3}]
m = 1
for i in my_list:
    print(f'{m}. {i} это - {type(i)}')
    m+=1

#'''2. Для списка реализовать обмен значений соседних элементов. Значениями
# обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном
# количестве элементов последний сохранить на своём месте. Для заполнения
# списка элементов нужно использовать функцию input().
# '''

new_list = input("Введите список элементов через пробел: ").split()
k = 0
if len(new_list) % 2 == 0:
    while k < len(new_list):
        new_list[k], new_list[k+1] = new_list[k+1], new_list[k]
        k += 2
    print(*new_list)
else:
     a = new_list[-1]
     new_list = new_list[:-1]
     while k < len(new_list):
         new_list[k], new_list[k+1] = new_list[k+1], new_list[k]
         k += 2
     new_list.append(a)
     print(*new_list)

#'''3. Пользователь вводит месяц в виде целого числа
#от 1 до 12. Сообщить, к какому времени года
# относится месяц (зима, весна, лето, осень).
#  Напишите решения через list и dict.'''

month = int(input("Введите номер месяца: "))
my_months = ['winter', 'spring', 'summer', 'autumn']
if month == 1 or month == 2 or month == 12:
    print(my_months[0])
elif 3 <= month <= 5:
    print(my_months[1])
elif 6 <= month <= 8:
    print(my_months[2])
elif 9 <= month <= 11:
    print(my_months[3])
else:
    print("такого месяца не существует")
month_2 = int(input("Введите еще раз номер месяца: "))
dict_months = {"winter": [12,1,2], "spring": [3,4,5], "summer": [6,7,8], "autumn": [9,10,11]}
for el in dict_months:
    if month_2 in dict_months[el]:
        print(el)

#''' 4. Пользователь вводит строку из нескольких слов, разделённых
# пробелами. Вывести каждое слово с новой строки. Строки нужно
#  пронумеровать. Если слово длинное, выводить только первые
#   10 букв в слове.
#'''

string = input("введите строку, разделенную пробелами: ").split()
for i in range(len(string)):

    print(f'{i+1}. {string[i][:10].capitalize()}')

# ''' 5. Реализовать структуру «Рейтинг», представляющую собой набор
# натуральных чисел, который не возрастает. У пользователя нужно
#  запрашивать новый элемент рейтинга. Если в рейтинге существуют
#   элементы с одинаковыми значениями, то новый элемент с тем же
#   значением должен разместиться после них.


digit_list = [111, 11, 1, -1, -11, -111]
n = int(input("Введите натурально число(для выхода введите 0): "))
while n != 0:
    digit_list.append(n)
    print(sorted(digit_list, reverse=True))
    n = int(input("Введите натурально число(для выхода введите 0): "))

