# простая реализация паттерна Информационный эксперт
# class PriceProducts:
#     def __init__(self, name: str, category: str, price: float, count: int):
#         self.name = name
#         self.category = category
#         self.price = price
#         self.count = count
#
#     def sum_position(self):
#         return self.price * self.count
#
#
# sale = PriceProducts('BMW', 'auto', 5_000_000, 2)
# # print(f'Сумма покупки: {sale.price * sale.count}')
# print(f'Сумма покупки: {sale.sum_position()}')


# более сложная реализация паттерна Информационных эксперт
class Products:
    list_of_products: dict = {}

    # def add_product(self, name_products: str, price: int, quantity: int):
    #     key = len(self.list_of_products) + 1
    #     self.list_of_products[key] = name_products, price, quantity

    # def calculate_sum(self):
    #     _sum: int = 0
    #     for key, values in self.list_of_products.items():
    #         _sum += values[1] * values[2]
    #     return _sum

    def add_product(self, name_products: str, price: int, quantity: int):
        key = len(self.list_of_products) + 1
        self.list_of_products[key] = {
            'name_products': name_products,
            'price': price,
            'quantity': quantity}

    def calculate_sum(self):
        all_sum: int = 0
        for key, values in self.list_of_products.items():
            all_sum += values['price'] * values['quantity']
        return all_sum

    def show_buys(self):
        return list(self.list_of_products.values())


buyer = Products()
buyer.add_product("Хлеб постный", 34, 1)
buyer.add_product("Вода минеральная", 166, 6)
buyer.add_product("Шашлык бараний", 2990, 3)
print(buyer.show_buys())
print(buyer.calculate_sum())
