# -*- coding: utf-8 -*-

# # Есть Алфавит, характеристиками которого являются:
# # 1. Язык
# # 2. Список букв
# #
# # Для Алфавита можно:
# # 1. Напечатать все буквы алфавита
# # 2. Посчитать количество букв
# #
# # Так же есть Английский алфавит, который обладает следующими свойствами:
# # 1. Язык
# # 2. Список букв
# # 3. Количество букв
# #
# # Для Английского алфавита можно:
# # 1. Посчитать количество букв
# # 2. Определить, относится ли буква к английскому алфавиту
# # 3. Получить пример текста на английском языке
#
# import string
# class Alphabet:
#
#     def __init__(self, lang, letters_str):
#         self.lang = lang
#         self.letters = list(letters_str)
#
#     def print(self):
#         print(self.letters)
#
#     def letters_num(self):
#         return len(self.letters)
#
# class EngAlphabet(Alphabet):
#     _letters_num = 26
#
#     def __init__(self):
#         super().__init__('En', string.ascii_uppercase)
#
#     def is_en_letter(self, letter):
#         if letter.upper() in self.letters:
#             return True
#         else:
#             return False
#
#     @staticmethod
#     def example():
#         print('English Example: I would like to become Python engineer')
#
# if __name__ == '__main__':
#     eng_alphabet = EngAlphabet()
#     eng_alphabet.print()
#     print(eng_alphabet.letters_num())
#     print(eng_alphabet.is_en_letter('D'))
#     print(eng_alphabet.is_en_letter('Ц'))
#     EngAlphabet.example()




# # Есть Помидор со следующими характеристиками:
# # 1. Индекс
# # 2. Стадия зрелости(стадии: Отсутствует, Цветение, Зеленый, Красный)
# #
# # Помидор может:
# # 1. Расти (переходить на следующую стадию созревания)
# # 2. Предоставлять информацию о своей зрелости
# #
# # Есть Куст с помидорами, который:
# # 1. Содержит список томатов, которые на нем растут
# #
# # И может:
# # 1. Расти вместе с томатами
# # 2. Предоставлять информацию о зрелости всех томатов
# # 3. Предоставлять урожай
# #
# # И также есть Садовник, который имеет:
# # 1. Имя
# # 2. Растение, за которым он ухаживает
# #
# # И может:
# # 1. Ухаживать за растением
# # 2. Собирать с него урожай
#
# class Tomato:
#
#     # Стадии созревания помидора
#     states = {0: 'nothing', 1: 'flower', 2: 'green_tomato', 3: 'red_tomato'}
#
#     def __init__(self, index):
#         self._index = index
#         self._state = 0
#
#     # Переход к следующей стадии созревания
#     def grow(self):
#         self._change_state()
#
#     # Проверка, созрел ли томат
#     def is_ripe(self):
#         if self._state == 3:
#             return True
#         return False
#
#     # Защищенные(protected) методы
#
#     def _change_state(self):
#         if self._state < 3:
#             self._state += 1
#         self._print_state()
#
#     def _print_state(self):
#         print(f'Tomato {self._index} is {Tomato.states[self._state]}')
#
#
# class TomatoBush:
#
#     # Создаем список из объектов класса Tomato
#     def __init__(self, num):
#         self.tomatoes = [Tomato(index) for index in range(0, num)]
#
#     # Переводим все томаты из списка на следующий этап созревания
#     def grow_all(self):
#         for tomato in self.tomatoes:
#             tomato.grow()
#
#     # Проверяем, все ли помидоры созрели
#     def all_are_ripe(self):
#         return all([tomato.is_ripe() for tomato in self.tomatoes])
#
#     # Собираем урожай
#     def give_away_all(self):
#         self.tomatoes = []
#
#
# class Gardener:
#
#     # Выдаем садовнику растение для ухода
#     def __init__(self, name, plant):
#         self.name = name
#         self._plant = plant
#
#     # Ухаживаем за растением
#     def work(self):
#         print('Gardener is working...')
#         self._plant.grow_all()
#         print('Gardener finished')
#
#     # Собираем урожай
#     def harvest(self):
#         print('Gardener is harvesting...')
#         if self._plant.all_are_ripe():
#             self._plant.give_away_all()
#             print('Harvesting is finished')
#         else:
#             print('Too early! Your plant is green and not ripe.')
#
# #тесты
# if __name__ == '__main__':
#     great_tomato_bush = TomatoBush(4)
#     gardener = Gardener('Evgenii', great_tomato_bush)
#     gardener.work()
#     gardener.work()
#     gardener.harvest()
#     gardener.work()
#     gardener.harvest()



# Есть Человек, характеристиками которого являются:
# 1. Имя
# 2. Возраст
# 3. Наличие денег
# 4. Наличие собственного жилья
#
# Человек может:
# 1. Предоставить информацию о себе
# 2. Заработать деньги
# 3. Купить дом
#
# Также же есть Дом, к свойствам которого относятся:
# 1. Площадь
# 2. Стоимость
#
# Для Дома можно:
# 1. Применить скидку на покупку
#
# Также есть Небольшой Типовой Дом, обязательной площадью 40м2.

# class Human:
#     default_name = 'No name'
#     default_age = 0
#
#     def __init__(self, name=default_name, age=default_age):
# # Динамические поля
# # Публичные
#         self.name = name
#         self.age = age
# # Приватные
#         self.__money = 0
#         self.__house = None
#
#     def info(self):
#         print(f'Name: {self.name}')
#         print(f'Age: {self.age}')
#         print(f'Money: {self.__money}')
#         print(f'House: {self.__house}')
#     @staticmethod
#     def default_info():
#         print(f'Default Name: {Human.default_name}')
#         print(f'Default Age: {Human.default_age}')
#
#     def earn_money(self, amount):
#         self.__money += amount
#         print(f'Earned {amount} money! Current value: {self.__money}')
#
#     def buy_house(self, house, discount):
#         price = house.final_price(discount)
#         if self.__money >= price:
#             self.__make_deal(house, price)
#         else:
#             print('Money not enough!')
#
#
#     def __make_deal(self, house, price):
#         self.__money -= price
#         self.__house = house
#
# class House:
#
#     def __init__(self, area, price):
#         self._area = area
#         self._price = price
#
#     def final_price(self, discount):
#         final_price = self._price * (100-discount) / 100
#         print(f'Final price: {final_price}')
#         return final_price
#
# class SmallHouse(House):
#     default_area = 40
#
#     def __init__(self, price):
#         super().__init__(SmallHouse.default_area, price)
#
# if __name__ == '__main__':
#
#     Human.default_info()
#
#     alexander = Human('Sasha', 27)
#     alexander.info()
#
#     small_house = SmallHouse(8_500)
#
#     alexander.buy_house(small_house, 5)
#
#     alexander.earn_money(5_000)
#     alexander.buy_house(small_house, 5)
#
#     alexander.earn_money(20_000)
#     alexander.buy_house(small_house, 5)
#     alexander.info()

