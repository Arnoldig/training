# реализация посредника

# класс розетки Россия
class SocketRus:
    def plug(self):
        return '2 разъёма круглых'


# класс розетки Китай
class SocketChaina:
    def plug(self):
        return '3 разъёма плоских'


# класс розетки Европа
class SocketEuro:
    def plug(self):
        return '2 разъёма круглых и 1 плоский'


# класс розетки которой просто нет (не существует)
class MyError:
    def plug(self):
        return 'Нет такого разъёма!'


class Plug:
    def connecting_power(self, name_socket: str):
        return Broker().plug(name_socket)


# класс посредника, который берёт на себя работу по определению типа разъёма
class Broker:
    my_socket: dict = {
        'rus': SocketRus,
        'chaina': SocketChaina,
        'euro': SocketEuro,
    }

    def plug(self, name_socket: str) -> str:
        temp = self.my_socket.get(name_socket, MyError)
        return temp().plug()


temp = Plug()
print(temp.connecting_power('rus'))
print(temp.connecting_power('chaina'))
print(temp.connecting_power('euro'))
print(temp.connecting_power('euro2'))
