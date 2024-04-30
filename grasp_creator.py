class Product:
    count: int = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description


class Sales:
    my_list = []

    def create_product(self, name, description, amount):
        product = Product(name, description)
        self.my_list.append([product, amount])

    def amount(self):
        amount: float = 0
        for product, amnt in self.my_list:
            amount += amnt
        print(f'Товаров в корзине: {amount}')

    def names(self):
        for product, count in self.my_list:
            print(product.name)

    def descriptions(self):
        for product, count in self.my_list:
            print(product.description)


temp = Sales()
temp.create_product('Хлеб', 'Описание хлеба', 16.8)
temp.create_product('Пасха', 'Описание пасхи', 14.2)
temp.amount()
temp.names()
temp.descriptions()
