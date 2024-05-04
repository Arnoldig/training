class User:
    count: int = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_id(self):
        self.count += 1
        return self.count


class Basket:
    def __init__(self, id: int):
        self.id = id
        self.list_pr: dict = {}

    def add_product(self, product_name: str, amount: int, price: int):
        if self.id not in self.list_pr:
            self.list_pr[self.id] = []
            self.list_pr[self.id].append({
                'product_name': product_name,
                'amount': amount,
                'price': price})
        else:
            self.list_pr[self.id].append({
                'product_name': product_name,
                'amount': amount,
                'price': price})

    def calculate_sum(self):
        all_sum: int = 0
        for values in self.list_pr.values():
            for value in values:
                all_sum += value['amount'] * value['price']
        return all_sum

    def show_discount(self):
        all_sum: float = self.calculate_sum()
        return Discount(all_sum)


class Discount:

    def __init__(self, all_sum: float):
        self.all_sum = all_sum

    def get_discount(self) -> float:
        if self.all_sum <= 100:
            return 0.99 * self.all_sum
        else:
            return 0.85 * self.all_sum


user = User('Михаил', 23)
id = user.get_id()
basket = Basket(id)
basket.add_product('Mac1', 1, 100)
basket.add_product('Mac2', 2, 200)
basket.add_product('Mac3', 7, 900)
print(basket.list_pr)
print(basket.calculate_sum())

# user = User('Святослав', 30)
id = user.get_id()
basket_ = Basket(id)
basket_.add_product('Mac1', 1, 100)
basket_.add_product('Mac2', 2, 200)
basket_.add_product('Mac3', 7, 900)
print(basket_.list_pr)
print(basket_.calculate_sum())
