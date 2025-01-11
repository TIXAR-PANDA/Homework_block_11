from pprint import pprint
import inspect

def introspection_info(obj):
    """
  - Тип объекта.
  - Информация от разработчика.
  - Атрибуты объекта
  - Методы объекта.
  - Модуль, к которому объект принадлежит"""
    print(f'Тип объекта - {type(obj)}')
    print('Информация от разработчика: ')
    print(help(obj))
    print('Атрибуты объекта: ')
    pprint(vars(obj))
    print('Методы объекта: ')
    pprint(inspect.getmembers(obj, predicate=inspect.ismethod))
    print('Модуль, к которому объект принадлежит: ')
    print( inspect.getmodule(obj))

class Vehicle1:
    """ (см. домашнюю работу Homework - module_6_1.py)
    Класс Vehicle - это любой транспорт
    Атрибут owner(str) - владелец транспорта. (владелец может меняться)
    Атрибут __model(str) - модель (марка) транспорта. (мы не можем менять название модели)
    Атрибут __engine_power(int) - мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
    Атрибут __color(str) - название цвета. (мы не можем менять цвет автомобиля своими руками)
    Атрибут класса __COLOR_VARIANTS, в который записан список допустимых цветов для окрашивания
    """

    def __init__(self,owner,__model,__engine_power,__color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color
        self.__COLOR_VARIANTS = ['синий', 'красный', 'зеленый', 'черный', 'белый']


    def get_model(self):
        """
        Метод возвращает модель автотранспорта.
        """
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        """
        Метод возвращает мощность двигателя.
        """
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        """
        Метод возвращает цвет автотранспорта.
        """
        return f'Цвет: {self.__color}'

    def print_info(self):
        """
        Метод печатает информацию об автотранспорте.
        """
        print("Информация об автотранспорте.")
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        """  Метод set_color - принимает аргумент new_color(str)
           если он есть в списке __COLOR_VARIANTS, меняет цвет __color на new_color
           в противном случае выводит на экран надпись: 'Нельзя сменить цвет'"""
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color.lower()
        else:
            print(f'Нельзя сменить цвет на {new_color.lower()}')

class Sedan(Vehicle1):
    """  Sedan(седан) - наследник класса Vehicle
     (см. домашнюю работу Homework - module_6_1.py)"""
    __PASSENGERS_LIMIT = 5




vehicle2 = Sedan('Федот', 'Toyota Mark II', 500, 'синий')
introspection_info(vehicle2)

