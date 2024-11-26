from basic_func import *


def base_func():
    """
    Основная исполняемая функция
    :return: None
    """
    while True: #запускаем бесконечный цикл
        print("Список доступных команд:\n"
              "new_book - добавление книги\n"
              "delete_book - удаление книги из списка\n"
              "update_status - обновление статуса книги\n"
              "find_book - поиск книги\n"
              "all_books - все книги\n")
        command = input("Введите команду: ")

        if command == "new_book":
            new_book()
        elif command == "delete_book":
            delete_book()
        elif command == "update_status":
            update_status_book()
        elif command == "find_book":
            find_book()
        elif command == "all_books":
            all_books()
        else:
            print("\nТакой команды не существует!\n")


if __name__ == '__main__':
    base_func()


