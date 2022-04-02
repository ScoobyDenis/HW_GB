# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго
# (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном
# порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его
# нарушении выводить соответствующее сообщение и завершать скрипт.

import time

class TrafficLight:
    __colors = ['***red***', '***yellow***', '***green***']

    def running(self, cycles):
        for i in range(cycles):
            print(TrafficLight.__colors[0])
            print("Ready")
            time.sleep(7)
            print(TrafficLight.__colors[1])
            print('Steady')
            time.sleep(2)
            print(TrafficLight.__colors[2])
            print('Go')
            time.sleep(5)
step_1 = TrafficLight()
step_1.running(int(input("Введите количество циклов светофора: ")))

# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия
# всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв.
# метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.
print("_____________")
class Road:

    def __init__(self, _length, _width):
        weight = 25
        thickness = 5
        total_weight = _length * _width * weight * thickness
        print(f'{int(total_weight/1000)} т.')

a = Road(500,15)

print("_____________")
# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
# элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса
# Position, передать данные, проверить значения атрибутов, вызвать методы
# экземпляров.


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(self.name, self.surname)
    def get_total_income(self):
        print(self._income.get("wage") + self._income.get("bonus"))

a = Position("Jhon", "Parker", "manager", 4000, 1500)
a.get_full_name()
a.get_total_income()

print("_____________")
# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
# о превышении скорости.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.name} is start"
    def stop(self):
        return f"{self.name} is stop"
    def turn(self, direction):
        return f"{self.name} is direction to " + direction
    def show_speed(self):
        return self.speed

class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)
    def show_speed(self):
        if self.speed > 60:
            return f"{self.speed}... Over speed!!!"
        else:
            return self.speed

class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)
    def show_speed(self):
        if self.speed > 40:
            return f"{self.speed}... Over speed!!!"
        else:
            return self.speed

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police=True)



merc = PoliceCar(150, "black", 'Mercedec', True)
print(merc.go())
print(merc.show_speed())
print(merc.turn("Bank"))
print(merc.stop())

prius = TownCar(80, "blue", 'Toyota-prius', False)
print(prius.show_speed())

gazel = WorkCar(39, "white", "Gazel", False)
print(gazel.go(), gazel.show_speed(), gazel.turn("river"), gazel.stop(), sep='\n')

print("_____________")
# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса
# метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод
# для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Start rendering with", self.title)
        print("""
        ---{{--{@
        """)

class Pen(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Start rendering with", self.title)
        print("""
        ../\_/\ . . (ღ
          =^.^= . . ))
        . ./ \ . . _(__
         ..(__)__, ██╝
         """)

class Pencil(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Start rendering with", self.title)
        print("""
           ░░░░░░░░░░░░░░░░░░░░░░
        ░░░░▄▄█▄▄░░░░░░░░░░░░░
        ░▄▀██████▌▄▄█▀░░▄▄▄░░░
        ░█░▐███████▀░░░░███▀▌░
        ▒▒▀▀█████▀▒▒▒▒▒▒███▀▒▒
        """)

class Marker(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Start rendering with", self.title)
        print("""
        (\__/)
        (='.'=)
        (")_(")
        """)

parker = Pen("Parker")
parker.draw()
hatber = Pencil("hatber")
hatber.draw()
erich_krause = Marker("ErichKrause")
erich_krause.draw()