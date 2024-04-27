class Animal:
    def __init__(self, age, weight, size):
        self.age = age
        self.__weight = weight
        self.__size = size

    @property  # геттер - возвращает пользователю переменную класса
    def weight_all_next(self):
        return self.__weight

    # сеттер - устанавливает значение переменной класса
    @weight_all_next.setter
    def weight_all_next(self, value):
        if value > 0:
            self.__weight = value
        else:
            print('Ошибка установки значения переменной!')

    def run(self):
        print(f'Животное массой {self.__weight} кг, бежит!')


cat = Animal(3, 4, 30)
print(cat.weight_all_next)
cat.weight_all_next = -1
cat.weight_all_next = 100
print(cat.weight_all_next)
