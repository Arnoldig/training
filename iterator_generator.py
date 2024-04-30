class IterClass:
    count: int = 0
    # my_list: list = range(10)

    def __iter__(self):
        return self

    def __next__(self): # это генератор получился
        self.count += 1
        if self.count > 10:
            raise StopIteration
        return self.count

    # def __next__(self):  # это ИТЕРАТОР
    #     self.count += 1
    #     if self.count > len(self.my_list):
    #         raise StopIteration
    #     return self.my_list[self.count - 1]


first_iter = IterClass()
for i in first_iter:
    print(i)
