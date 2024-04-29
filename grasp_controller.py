# # Простая реализация контроллера
#
# def user_select(select: bool = False):
#     if not select:
#         show_personal_page()
#     else:
#         show_table()
#
#
# def show_personal_page():
#     print('Отображаем персональную страницу.')
#
#
# def show_table():
#     print('Отображаем рассписание.')
#
#
# user_select() # вызов персональной страницы
# user_select(True) # вызов расписания

# # реализация контроллера через классы
# class UserSelect:
#
#     def selected(self, select: bool = False):
#         if not select:
#             PagesSelect()
#         else:
#             ShowTable()
#
#
# class PagesSelect:
#     def __init__(self):
#         print('Отображаем персональную страницу.')
#
#
# class ShowTable:
#     def __init__(self):
#         print('Отображаем рассписание.')
#
#
# temp = UserSelect()
# temp.selected()
# temp.selected(True)


# реализация через декоратор
def my_decorator(func):
    def wrapper(*select):
        if not select:
            func(select)
            print('- персональную страницу.')
        else:
            func(select)
            print('- рассписание.')
    return wrapper

@my_decorator # сахар для варианта 2 - закоментируй при вар. 1
def page_user(select: bool):
    print('Пользователю необходимо показать: ')

# реализация декоратора без синтаксического сахара, вариант 1
# temp = my_decorator(page_user)
# temp()
# temp(True)

# реализация с сахаром, вариант 2
page_user()
page_user(True)