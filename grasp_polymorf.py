# # Полиморфизм и его реализация в коде
# class Car:
#     def __init__(self, name_car: str, age: int):
#         self.name_car = name_car
#         self.age = age
#
#     def move(self, speed: int):
#         print(f'Авто двигается со скоростью {speed}')
#
#
# class Animal:
#     def __init__(self, name_animal: str, age: int):
#         self.name_animal = name_animal
#         self.age = age
#
#     def move(self, speed: int):
#         if speed >= 20:
#             print('Животное не может так быстро бежать!')
#         else:
#             print(f'Животное двигается со скоростью {speed}')
#
#
# bmw = Car('BMW 520', 2024)
# bmw.move(150)
#
# cat = Animal('Сибирская 3х шёрстная', 2024)
# cat.move(10)

# уходим от if-ов через полиморфизм

class Discount:
    __discount_all: dict = {
        'age': 0.05,
        '0308': 0.10,
        '0223': 0.08,
        '0308_age': 0.18,
        'day_veteran': 0.17,
    }

    def get_discount(self, type_discount: str) -> float:
        return self.__discount_all.get(type_discount, False)


class Age:
    __start_age = 65
    __list_age: dict = {v: True for v in range(__start_age, 301)}

    def has_age_discount(self, age: int) -> float:
        return self.__list_age.get(age, False)


class Day:
    __list_day: dict = {
        '0308': True,
        '0223': True,
    }

    def has_day_discount(self, month: str, day: str, md: str) -> float:
        key = month + day
        is_used = key == md
        return self.__list_day.get(key, False) * is_used


class Day_age:
    def has_summary_discount(self, age: int,
                             month: str,
                             day: str,
                             md: str) -> float:
        return (Age().has_age_discount(age)
                * Day().has_day_discount(month, day, md))


class Day_veteran:
    def has_summary_discount(self,
                             veteran: int,
                             month: str,
                             day: str,
                             md: str) -> float:
        return (Day().has_day_discount(month, day, md)
                * veteran
                * Discount().get_discount('day_veteran')
                + Day().has_day_discount(month, day, md)
                * Discount().get_discount('0223'))


def shop():
    age = int(input('Введите ваш возраст: '))
    date = input('Введите текущую дату в формате DD/MM/YY: ').split('/')
    price = int(input('Введите стоимость покупки: '))

    day = date[0]
    month = date[1]

    if age > 65:
        print(f'Стоимость покупки с пенсионной скидкой: {price * 0.95}')

    print(price
          - price
          * Age().has_age_discount(age)
          * Discount().get_discount("age"))

    if day == "08" and month == "03":
        print(f'Стоимость покупки со скидкой в честь 8 мата: {price * 0.9}')

    print(price
          - price
          * Day().has_day_discount(month, day, "0308")
          * Discount().get_discount("0308"))

    if day == "08" and month == "03" and age > 65:
        print(f'Стоимость покупки со скидкой в честь 8 марта и '
              f'пенсионной скидкой: {price * 0.82}')

    print(price
          - price
          * Day_age().has_summary_discount(age, month, day, "0308")
          * Discount().get_discount("0308_age"))

    if day == "23" and month == "02":
        veteran = int(input('Вы ветеран? Введите 0 - если нет, 1 - если да: '))
        if veteran == 1:
            print('Стоимость покупки со скидкой в честь 23 февраля и '
                  f'статусом ветерана: {price * 0.75}')
        else:
            print('Стоимость покупки со скидкой '
                  f'в честь 23 февраля: {price * 0.92}')
    print(price
          - price
          * Day_veteran().has_summary_discount(veteran, month, day, "0223"))


if __name__ == '__main__':
    shop()

# копия функции которую необходимо было заменить на классы
# def shop():
#     age = int(input('Введите ваш возраст: '))
#     date = input('Введите текущую дату в формате DD/MM/YY: ').split('/')
#     price = int(input('Введите стоимость покупки: '))
#     day = date[0]
#     month = date[1]
#
#     if age > 65:
#         print(f'Стоимость покупки с пенсионной скидкой: {price * 0.95}')
#
#     if day == '08' and month == '03':
#         print(f'Стоимость покупки со скидкой в честь 8 мата: {price * 0.9}')
#
#     if day == '08' and month == '03' and age > 65:
#         print(
#             f'Стоимость покупки со скидкой в честь 8 марта и пенсионной скидкой: {price * 0.82}')
#
#     if day == '23' and month == '02':
#         veteran = int(input('Вы ветеран? Введите 0 - если нет, 1 - если да'))
#         if veteran == 1:
#             print(
#                 f'Стоимость покупки со скидкой в честь 23 февраля и статусом ветерана: {price * 0.75}')
#         else:
#             print(
#                 f'Стоимость покупки со скидкой в честь 23 февраля: {price * 0.92}')
