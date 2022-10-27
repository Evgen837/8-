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

#     def letters_num(self):
#         return EngAlphabet.__letters_num
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
#     # protected методы
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
#
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
#     alexander = Human('Sasha', 27)
#     alexander.info()
#     small_house = SmallHouse(8_500)
#     alexander.buy_house(small_house, 5)
#     alexander.earn_money(5_000)
#     alexander.buy_house(small_house, 5)
#     alexander.earn_money(20_000)
#     alexander.buy_house(small_house, 5)
#     alexander.info()




# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


# class Water:
#     def __add__(self, other):
#         if isinstance(other, Air):
#             return Storm()
#         elif isinstance(other, Fire):
#             return Vapor()
#         elif isinstance(other, Earth):
#             return Dirt()
#         else:
#             return None
#
#     def __str__(self):
#         return 'Вода'
#
# class Air:
#     def __add__(self, other):
#         if isinstance(other, Water):
#             return Storm()
#         elif isinstance(other, Fire):
#             return Lightning()
#         elif isinstance(other, Earth):
#             return Dust()
#         else:
#             return None
#
#     def __str__(self):
#         return 'Воздух'
#
# class Fire:
#     def __add__(self, other):
#         if isinstance(other, Water):
#             return Vapor()
#         elif isinstance(other, Air):
#             return Lightning()
#         elif isinstance(other, Earth):
#             return Lava()
#         else:
#             return None
#
#     def __str__(self):
#         return 'Огонь'
#
# class Earth:
#     def __add__(self, other):
#         if isinstance(other, Water):
#             return Dirt()
#         elif isinstance(other, Air):
#             return Dust()
#         elif isinstance(other, Fire):
#             return Lava()
#         else:
#             return None
#
#     def __str__(self):
#         return 'Земля'
#
# class Storm:
#     def __str__(self):
#         return 'Шторм'
#
# class Vapor:
#     def __str__(self):
#         return 'Пар'
#
# class Dirt:
#     def __str__(self):
#         return 'Грязь'
#
# class Lightning:
#     def __str__(self):
#         return 'Молния'
#
# class Dust:
#     def __str__(self):
#         return 'Пыль'
#
# class Lava:
#     def __str__(self):
#         return 'Лава'
#
#
# water = Water()
# air = Air()
# fire = Fire()
# earth = Earth()
# print(air + water, water + air)
# print(water + fire, fire + water)
# print(water + earth, earth + water)
# print(air + fire, fire + air)
# print(air + earth, earth + air)
# print(fire + earth, earth + fire)







# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.


# from random import randint
# from termcolor import cprint
# class Cat:
#     def __init__(self, name):
#         self.name = name
#         self.fullness = 10
#         self.house = None
#
#     def __str__(self):
#         return 'Я - {}, сытость {}'.format(self.name, self.fullness)
#
#     def wandering_the_street(self):
#         cprint('{} бродит по улице в поисках пищи и любящих хозяев'.format(self.name), color='cyan')
#         self.fullness -= 10
#
#     def eat_trash(self):
#         cprint('{} нашел в помойке что-то съедобное'.format(self.name), color='cyan')
#         self.fullness += 20
#
#     def eat(self):
#         if self.house.bowl >= 10:
#             cprint('{} поел'.format(self.name), color='yellow')
#             self.fullness += 10
#             self.house.bowl -= 10
#             self.house.dirt += 20
#         else:
#             cprint('{} нет еды'.format(self.name), color='red')
#
#     def sleep(self):
#         if self.house.bowl >= 10:
#             cprint('{} сытый и довольный заснул на кресле'.format(self.name), color='yellow')
#             self.fullness -= 10
#             self.house.dirt += 20
#         else:
#             cprint('{} задрых возле пустой миски в ожидании корма'.format(self.name), color='red')
#
#     def scrape_wallpaper(self):
#         if self.house.bowl >= 20:
#             cprint('{} был в хорошем настроении и точил свои когти об стену '.format(self.name), color='yellow')
#             self.fullness -= 10
#             self.house.dirt += 50
#         else:
#             cprint('{} Целый день драл обои в надежде что его заметят и накормят'.format(self.name), color='red')
#
#     def act(self):
#         if self.fullness <= 0:
#             cprint('{} умер...'.format(self.name), color='red')
#             return
#         dice = randint(1, 6)
#         if self.fullness < 20:
#             self.eat()
#         elif dice % 2 == 0:
#             self.sleep()
#         else:
#             self.scrape_wallpaper()
#
#
# class Man:
#
#     # Есть переменные объекта, а есть переменные класса. Изменение первых коснется только конкретного объкета,
#     # а второго - всех объкетов этого класса. Поэтому если мы здесь сделаем именно переменную класса,
#     # то все люди будут знать, что в доме появился кот
#     has_a_cat = False
#
#     def __init__(self, name):
#         self.name = name
#         self.fullness = 50
#         self.house = None
#
#     def __str__(self):
#         return 'Я - {}, сытость {}'.format(self.name, self.fullness)
#
#     def eat(self):
#         if self.house.food >= 10:
#             cprint('{} поел'.format(self.name), color='yellow')
#             self.fullness += 10
#             self.house.food -= 10
#         else:
#             cprint('{} нет еды'.format(self.name), color='red')
#
#     def work(self):
#         cprint('{} сходил на работу'.format(self.name), color='blue')
#         self.house.money += 100
#         self.fullness -= 10
#
#     def pick_cat(self, cat):
#         cat.house = self.house
#         cprint('{} Подобрал кота по имени {}'.format(self.name, cat.name), color='blue')
#         cprint('{} купил миску для кота'.format(self.name), color='blue')
#         self.fullness -= 10
#         Man.has_a_cat = True
#
#     def cleaning(self):
#         cprint('{} убрался в доме'.format(self.name), color='blue')
#         self.house.dirt -= 100
#         self.fullness -= 20
#
#     def watch_MTV(self):
#         cprint('{} смотрел MTV целый день'.format(self.name), color='green')
#         self.fullness -= 10
#
#     def shopping(self):
#         if self.house.money >= 50:
#             cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
#             self.house.food += 50
#             self.house.money -= 50
#         else:
#             cprint('{} деньги кончились!'.format(self.name), color='red')
#
#     def go_to_the_house(self, house):
#         self.house = house
#         self.fullness -= 10
#         cprint('{} Вьехал в дом'.format(self.name), color='cyan')
#
#     def buy_cat_food(self):
#         if self.house.money >= 50:
#             cprint('{} сходил в зоомагазин за кошачим кормом'.format(self.name), color='cyan')
#             self.fullness -= 10
#             self.house.bowl += 50
#             self.house.money -= 50
#         else:
#             cprint('{} деньги кончились!'.format(self.name), color='red')
#
#     def act(self):
#         if self.fullness <= 0:
#             cprint('{} умер...'.format(self.name), color='red')
#             return
#         dice = randint(1, 6)
#         if self.fullness <= 20:
#             self.eat()
#         elif self.house.money <= 80:
#             self.work()
#         elif self.house.food < 30:
#             self.shopping()
#         elif self.house.dirt >= 100:
#             self.cleaning()
#         elif self.house.bowl < 20 and Man.has_a_cat:
#             self.buy_cat_food()
#         elif dice == 1:
#             self.work()
#         elif dice == 2:
#             self.eat()
#         else:
#             self.watch_MTV()
#
#
# class House:
#
#     def __init__(self):
#         self.food = 50
#         self.money = 0
#         self.bowl = 0
#         self.dirt = 0
#
#     def __str__(self):
#         return 'Остатки в доме: Еда: {}, деньги: {}, корм: {}, уровень грязи: {}'.format(self.food, self.money, self.bowl, self.dirt)
#
# citizens = [
#     Man(name='Бивис'),
#     Man(name='Батхед'),
#     Man(name='Кенни'),
# ]
# murzik = Cat(name='Мурзик')
# my_sweet_home = House()
# for citisen in citizens:
#     citisen.go_to_the_house(house=my_sweet_home)
#
# for day in range(1, 365):
#     print('================ день {} =================='.format(day))
#     if murzik.house is None:
#         if murzik.fullness <= 10:
#             murzik.eat_trash()
#         murzik.wandering_the_street()
#         print(murzik)
#     if day == 5:
#         citizens[0].pick_cat(murzik)
#         citizens.append(murzik)
#     for citisen in citizens:
#         citisen.act()
#     print('--- в конце дня ---')
#     for citisen in citizens:
#         print(citisen)
#     print(my_sweet_home)









# from termcolor import cprint
# from random import randint
#
# ######################################################## Часть первая
# #
# # Создать модель жизни небольшой семьи.
# #
# # Каждый день участники жизни могут делать только одно действие.
# # Все вместе они должны прожить год и не умереть.
# #
# # Муж может:
# #   есть,
# #   играть в WoT,
# #   ходить на работу,
# # Жена может:
# #   есть,
# #   покупать продукты,
# #   покупать шубу,
# #   убираться в доме,
#
# # Все они живут в одном доме, дом характеризуется:
# #   кол-во денег в тумбочке (в начале - 100)
# #   кол-во еды в холодильнике (в начале - 50)
# #   кол-во грязи (в начале - 0)
# #
# # У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
# #
# # Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# # Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# # Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
# #
# # Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# # Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
# #
# # Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# # Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# # Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# # Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
# #
# # Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.
# #
#
# class House:
#
#     def __init__(self):
#         self.dirt = 0
#         self.money = 100
#         self.food = 50
#         self.cat_food = 30
#         self.total_money = 0
#         self.total_fur_coat = 0
#         self.total_food_eaten = 0
#         self.total_cat_food_eaten = 0
#
#     def __str__(self):
#         return 'Степень загрязнения дома {}, еды в холодильнике {}, еды для кота {}, денег в тумбочке {}'.format(
#             self.dirt, self.food, self.cat_food, self.money)
#
#     def make_dusty(self):
#         self.dirt += 5
#         return
#
#
# class Creature:
#     INITIAL_FULLNESS = 30
#     DEPRESSION_BORDER = 10
#
#     def __init__(self, name):
#         self.happiness = 100
#         self.fullness = self.INITIAL_FULLNESS
#         self.name = name
#
#     def __str__(self):
#         return '{} - степень сытости {}, уровень счастья {}'.format(
#             self.name, self.fullness, self.happiness)
#
#     def is_alive(self):
#         return self.fullness > 0 and self.happiness > self.DEPRESSION_BORDER
#
#     def act(self):
#         if self.fullness <= 0:
#             cprint('{} помер с голоду!'.format(self.name), 'red')
#             return True  # действие уже совершено
#         if self.happiness <= self.DEPRESSION_BORDER:
#             cprint('{} скончался от депрессии!'.format(self.name), 'red')
#             return True  # действие уже совершено
#         return False
#
#
# class Man(Creature):
#
#     def __init__(self, name):
#         super().__init__(name)
#         self.pet = None
#         self.house = None
#         self.dice = 0
#         self.child = None
#
#     def eat(self):
#         if self.house.food >= 10:
#             cprint('{} поел'.format(self.name), 'yellow')
#             feed = randint(10, 30)
#             if feed > self.house.food:
#                 feed = self.house.food
#             self.house.food -= feed
#             self.fullness += feed
#             self.house.total_food_eaten += feed
#         else:
#             cprint('В доме нет еды!', 'red')
#             self.fullness -= 10
#
#     def go_into_the_house(self, house):
#         self.house = house
#         cprint('{} заехал в дом'.format(self.name), 'yellow')
#
#     def pet_the_cat(self):
#         if self.pet:
#             cprint('{} погладил {}а'.format(self.name, self.pet.name), 'yellow')
#             self.fullness -= 10
#             self.happiness += 5
#
#     def pick_up_cat(self, cat):
#         cat.house = self.house
#         cprint('{} подобрал {}а на помойке'.format(self.name, cat.name), 'yellow')
#
#     def act(self):
#         if super().act():
#             return True  # действие уже совершено
#         if self.fullness <= 30:
#             self.eat()
#             return True  # действие уже совершено
#         if self.house.dirt >= 90:
#             self.happiness -= 10
#         return False
#
#
# class Husband(Man):
#
#     def work(self):
#         cprint('{} сходил на работу'.format(self.name), 'yellow')
#         self.house.money += 150
#         self.fullness -= 10
#         self.house.total_money += 150
#
#     def gaming(self):
#         cprint('{} играет в WoT'.format(self.name), 'yellow')
#         self.fullness -= 10
#         self.happiness += 20
#
#     def act(self):
#         if super().act():
#             return
#         dice = randint(1, 6)
#         if self.house.money <= 300:
#             self.work()
#         elif dice == 1:
#             self.eat()
#         elif dice == 2:
#             self.pet_the_cat()
#         else:
#             self.gaming()
#
# class Wife(Man):
#
#     def shopping(self):
#         if self.house.money >= 100:
#             food = randint(80, 100)
#             self.house.food += food
#             self.house.money -= food
#             cprint('{} купила {} еды'.format(self.name, food), 'yellow')
#         else:
#             cprint('{}: в доме нет денег'.format(self.name), 'yellow')
#         self.fullness -= 10
#
#     def buy_cat_food(self):
#         if self.house.money >= 100:
#             cat_food = randint(10, 100)
#             self.house.cat_food += cat_food
#             self.house.money -= cat_food
#             cprint('{} купила {} еды для кота'.format(self.name, cat_food), 'yellow')
#         else:
#             cprint('{}: в доме нет денег, чтобы купить еду коту'.format(self.name), 'yellow')
#         self.fullness -= 10
#
#     def buy_fur_coat(self):
#         if self.house.money >= 350:
#             cprint('{} купила шубу'.format(self.name), 'yellow')
#             self.happiness += 60
#             self.house.money -= 350
#             self.house.total_fur_coat += 1
#         else:
#             cprint('{}: На шубу нет денег!'.format(self.name), 'yellow')
#             self.happiness -= 20
#         self.fullness -= 10
#
#     def clean_house(self):
#         cprint('{} убралась в доме'.format(self.name), 'yellow')
#         self.fullness -= 10
#         self.house.dirt -= 60
#
#     def act(self):
#         if super().act():
#             return
#         dice = randint(1, 3)
#         if self.house.dirt > 80:
#             self.clean_house()
#         elif self.house.food <= 60:
#             self.shopping()
#         elif self.house.cat_food <= 20:
#             self.buy_cat_food()
#         elif dice == 1:
#             self.eat()
#         elif dice == 2:
#             self.pet_the_cat()
#         else:
#             self.buy_fur_coat()
#
# class Cat(Creature):
#     DEPRESSION_BORDER = 30
#
#     def __init__(self, name):
#         super().__init__(name)
#         self.house = None
#
#     def eat(self):
#         if self.house is None:
#             cprint('Бездомный {} не может поесть!'.format(self.name), 'yellow')
#             return
#         if self.house.cat_food >= 10:
#             feed = randint(5, 10)
#             self.house.cat_food -= feed
#             self.house.total_cat_food_eaten += feed
#             self.fullness += feed * 2
#             cprint('{} поел из миски'.format(self.name), 'yellow')
#         else:
#             cprint('У {}а нет еды! '.format(self.name), 'yellow')
#
#     def sleep(self):
#         self.fullness -= 10
#         self.happiness -= 10
#         cprint('{} поспал'.format(self.name), 'yellow')
#
#     def soil(self):
#         self.fullness -= 10
#         self.house.dirt += 30
#         self.happiness += 50
#         cprint('{} разодрал обои'.format(self.name), 'yellow')
#
#     def act(self):
#         if super().act():
#             return
#         dice = randint(1, 6)
#         if self.fullness <= 10:
#             self.eat()
#         elif dice in (1, 2):
#             self.soil()
#         else:
#             self.sleep()
#
# class Child(Man):
#
#     def eat(self):
#         if self.house.food >= 10:
#             cprint('{} поел'.format(self.name), 'yellow')
#             feed = randint(5, 10)
#             self.house.food -= feed
#             self.fullness += feed
#             self.house.total_food_eaten += feed
#         else:
#             cprint('В доме нет еды! {} голодает!'.format(self.name), 'red')
#
#     def sleep(self):
#         cprint('{} спит. Не шумите!'.format(self.name), 'yellow')
#         self.fullness -= 10
#
#     def act(self):
#         if super().act():
#             return
#         if self.fullness < 10:
#             self.eat()
#         else:
#             self.sleep()
#
#
# if __name__ == '__main__':
#     home = House()
#     serge = Husband(name='Сережа')
#     masha = Wife(name='Маша')
#     serge.go_into_the_house(house=home)
#     masha.go_into_the_house(house=home)
#     kolya = Child(name='Коля')
#     kolya.go_into_the_house(house=home)
#     family_members = [serge, masha, kolya]
#     for day in range(1, 366):
#         cprint('================== День {} =================='.format(day), color='red')
#         if day == 7:
#             barsik = Cat(name='Барсик')
#             masha.pick_up_cat(cat=barsik)
#             family_members.append(barsik)
#         all_alive = True
#         for member in family_members:
#             member.act()
#             if not member.is_alive():
#                 cprint('{} умер(ла)...'.format(member.name), color='red')
#                 all_alive = False
#         for member in family_members:
#             cprint(member, color='cyan')
#         home.make_dusty()
#         cprint(home, color='cyan')
#         if not all_alive:
#             cprint('Нельзя жить в одном доме с трупом...', color='red')
#             break
#     cprint('Всего денег заработано {}'.format(home.total_money), color='green')
#     cprint('Всего шуб куплено {}'.format(home.total_fur_coat), color='green')
#     cprint('Всего еды съедено {}'.format(home.total_food_eaten), color='green')
#     cprint('Всего котом съедено еды {}'.format(home.total_cat_food_eaten), color='green')

