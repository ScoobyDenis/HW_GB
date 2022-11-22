# 1. Реализовать класс «Дата», функция-конструктор которого должна
# принимать дату в виде строки формата «день-месяц-год». В рамках класса
# реализовать два метода. Первый, с декоратором @classmethod. Он должен
# извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной
# структуры на реальных данных.

class Date:

    def __init__(self, d):
        self.d = d

    @classmethod
    def int_date(cls, d):
        l = []
        for i in d.split():
            if i != '-':
                l.append(i)
        return int(l[0]), int(l[1]), int(l[2])

    def __str__(self):
         return f'Это было {Date.int_date(self.d)}'

    @staticmethod
    def check_date(d, m, y):
        if 0 < d < 32 and 0 < m < 13:
            return d, m, y
        else:
            return 'Неверная дата'

putin_begin = '07 - 05 - 2000'
dd = Date(putin_begin)
print(dd)
print(Date.check_date(28, 2, 2030))
print(Date.check_date(28, 13, 2030))
print(Date.check_date(1, 1, -57000000))

# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию
# деления на ноль. Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class DivisionOfNumbers:
    '''
    Класс для проверки деления на ноль
    '''
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def division_by_zero(p1, p2):
        try:
            return p1 / p2
        except ZeroDivisionError:
            return f'попытка деления на ноль'

print(DivisionOfNumbers.__doc__)
print(DivisionOfNumbers.division_by_zero(11, 2))
print(DivisionOfNumbers.division_by_zero(1, 0))

# 3. Создайте собственный класс-исключение, который должен проверять содержимое
# списка на наличие только чисел. Проверить работу исключения на реальном примере.
# Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка.

class OnlyNums:
    '''
    Класс проверки списка на наличие только чисел
    '''
    def __init__(self, *el):
        self.l = []

    def create_list(self):
        while True:
            el = input('Введите число(для выхода введите "stop"): ').lower()
            if el.isdigit():
                self.l.append(int(el))
                print(f'список на данный момент {self.l}')
            elif el == 'stop':
                print(f'список сформирован {self.l}')
                break
            else:
                print('В список можно добавить только целые положительные числа')

print(OnlyNums.__doc__)
my_list = OnlyNums()
my_list.create_list()

# 7. Реализовать проект «Операции с комплексными числами». Создайте класс
# «Комплексное число». Реализуйте перегрузку методов сложения и умножения
# комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры
# класса (комплексные числа), выполните сложение и умножение созданных
# экземпляров. Проверьте корректность полученного результата.

class ComplexNum:
    def __init__(self, c_num):
        self.num = c_num

    def __add__(self, other):
        return self.num + other.num

    def __mul__(self, other):
        return self.num * other.num

c_one = ComplexNum(2 + 3j)
c_two = ComplexNum(8 + 7j)
print(c_one + c_two)
print(c_one * c_two)

# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают
# за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других
# данных, можно использовать любую подходящую структуру (например, словарь).

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных
# на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

class OfficeEquipment:
    def __init__(self, brand):
        self.brand = brand

class Printer(OfficeEquipment):
    def __init__(self, brand, total, coast):
        self.brand = brand
        self.total = total
        self.coast = coast
        self.type_eq = 'Принтеры'
        self.mydict = {'Тип оргтехники': self.type_eq, 'Марка': brand, 'Количество': total, 'Стоимость': coast}

    def __str__(self):
        return f'Итого: {self.mydict}'

class Scanner(OfficeEquipment):
    def __init__(self, *equipments):
        self.my_list = []
        self.type_eq = 'Сканеры'

    def create_list(self):
        s = 'y'
        while s == 'y':
            try:
                brand = input('Введите название марки сканера: ')
                total = int(input('Введите количество: '))
                coast = int(input('Стоимость единицы товара: '))
                my_dict = {'Тип оргтехники': self.type_eq, 'Марка': brand, 'Количество': total, 'Стоимость': coast}
                self.my_list.append(my_dict)
                print(self.my_list)
                s = input('Хотите ввести еще товар?(y/n) ')
            except:
                print('Ошибка ввода')

class Xerox(OfficeEquipment):
    def __init__(self, brand, total, coast):
        self.brand = brand
        self.total = total
        self.coast = coast
        self.type_eq = 'Ксероксы'
        print(f'Тип оргтехники: {self.type_eq}, Марка: {self.brand}, Количество: {self.total}, Стоимость: {self.coast}')

    @classmethod
    def equip(cls, data):
        brand, total, coast = data
        return cls(brand, total, coast)


a = Printer('Sony', 10, 7500)
print(a.__str__())
b = Scanner()
b.create_list()
print()
l = ['Hp', 7, 12500]
c = Xerox.equip(l)
