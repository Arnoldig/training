class SentStatus:

    def __enter__(self):
        print("Открыт доступ к файлу ...")


    def __exit__(self, exc_type, exc_value, trace):
        print("Доступ к файлу прекращён.")


with SentStatus():
    print("Записываю данные в файл Ридер.docs")
