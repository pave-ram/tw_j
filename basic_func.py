import json
import random


#
def new_book():
    """
    Функция для добавления новой книги в библ.
    :return: None
    """
    print("Введите данные книги как в примере\n"
          "(Название книги; автор; год издания)\n\n"
          "Пример: Дубровский; А.С.Пушкин; 1841")

    result = input("Вводите: ")
    result = result.split(";")

    if len(result) == 3: #проверяем количество полученных данных
        try:
            year = int(result[2]) #проверяем соотвествие записи года
        except Exception:
            print("При указании года, вписывайте просто число\n"
                  "(Пример: 2000)\n\n"
                  "Для повторной попытки добавления книги воспользуйтесь командой new_book")
            return None

    else:
        print("Данные введены некорректно\n\n"
              "Для повторной попытки добавления книги воспользуйтесь командой new_book")
        return None

    new_data_book = {"title": result[0],
                     "author": result[1],
                     "year": year,
                     "status": True} #формируем словарь для записи

    with open('data.txt', encoding="UTF8") as outfile: #открываем файл для чтения
        json_file = json.load(outfile)

        id_book = str(random.randint(1000000, 10000000)) #создаем уникальный id
        if id_book not in json_file: #проверка на уникальность значения id
            json_file[id_book] = new_data_book

    with open('data.txt', 'w', encoding="UTF8") as outfile: #перезаписываем новые данные в "Хранилище"
        json.dump(json_file, outfile)

    print("\n------------Книга успешно записана------------\n"
          f"Название: {result[0]}\n"
          f"Автор: {result[1]}\n"
          f"Год: {year}\n"
          f"ID записи: {id_book}\n\n")


def delete_book():
    """
    Функция удаления книги из библ.
    :return: None
    """
    print("\nВведите ID записи книги, которую хотите удалить\n"
          "(Пример: 1054788)\n")
    id_book = input("Вводите:")

    try:
        id_book = int(id_book) #проверка соответствия введнных данных
    except Exception:
        print("\nЗначение ID книги должен состоять из цифр от 0-9\n"
              "Для повторной попытки удаления книги воспользуйтесь командой delete_book\n\n")
        return None

    id_book = str(id_book)

    with open('data.txt', encoding="UTF8") as outfile: #открываем файл для чтения
        json_file = json.load(outfile)

        if id_book in json_file:
            print("---------Данные книги удалены--------\n" # проверка существования искомого для удаления ID
                  f"Удалены следующие данные по введенному ID\n"
                  f"ID книги: {id_book}\n"
                  f"Название: {json_file[id_book]['title']}\n"
                  f"Автор: {json_file[id_book]['author']}\n"
                  f"Год: {json_file[id_book]['year']}\n\n")
            json_file.pop(id_book) #удаление по ключу/id
        else:
            print("Такого ID не найдено.\n"
                  "Для повторной попытки удаления книги воспользуйтесь командой delete_book\n\n")

    with open('data.txt', 'w', encoding="UTF8") as outfile: #перезапись файла
        json.dump(json_file, outfile)


def find_book():
    """
    Поиск книг по фильтрам
    :return: None
    """
    print("Выберите фильтр:\n"
          "1 - поиск по названию\n"
          "2 - поиск по автору\n"
          "3 - поиск по году издания\n"
          "(Пример: 1)\n")
    filter = input("Вводите: ")
    try:
        filter = int(filter) #проверка соответствия типа данных
    except Exception:
        print(f"Такого варианта нет!\n"
              "1 - поиск по названию\n"
              "2 - поиск по автору\n"
              "3 - поиск по году издания\n"
              "(Пример: 1)\n"
              f"Для повторной попытки поиска книги воспользуйтесь командой find_book\n\n")

    if filter == 1:
        print("Отличо, теперь введите название книги\n"
              "(Пример: Дубровский)")
        title = input("Вводите: ")
        title_book = title.lower().replace(" ", "") #приводим текстовый формат к общему виду для расширения поисковых возможностей

        text = "\n--------Результат поиска--------\n"
        with open('data.txt', encoding="UTF8") as outfile: #открываем файл для чтения
            json_file = json.load(outfile)

        for id_book in json_file:
            if json_file[id_book]["title"].lower().replace(" ", "") == title_book: #поиск по "Хранилищу"
                text += (f"ID: {id_book}\n"
                         f"Название: {json_file[str(id_book)]['title']}\n"
                         f"Автор: {json_file[str(id_book)]['author']}\n"
                         f"Год: {json_file[str(id_book)]['year']}\n"
                         f"Статус: {json_file[str(id_book)]['status']}\n\n")

        if text == "\n--------Результат поиска--------\n": #обработка в случае неудачного поиска
            print(f"Книг c названием {title} не найдено\n"
                  f"Для повторной попытки поиска книги воспользуйтесь командой find_book\n\n")
        else:
            print(text)

    elif filter == 2:
        print("Отличо, теперь введите автора книги\n"
              "(Пример: А.С.Пушкин)")
        author = input("Вводите: ")
        author_book = author.lower().replace(" ", "")#приводим текстовый формат к общему виду для расширения поисковых возможностей

        text = "\n--------Результат поиска--------\n"
        with open('data.txt', encoding="UTF8") as outfile:#открываем файл для чтения
            json_file = json.load(outfile)

        for id_book in json_file:
            if json_file[id_book]["author"].lower().replace(" ", "") == author_book: #циклом выполняем поиск по автору
                text += (f"ID: {id_book}\n"
                         f"Название: {json_file[str(id_book)]['title']}\n"
                         f"Автор: {json_file[str(id_book)]['author']}\n"
                         f"Год: {json_file[str(id_book)]['year']}\n"
                         f"Статус: {json_file[str(id_book)]['status']}\n\n")  #формируем переменную текст

        if text == "\n--------Результат поиска--------\n":
            print(f"Книг автора {author} не найдено\n"
                  f"Для повторной попытки поиска книги воспользуйтесь командой find_book\n\n")
        else:
            print(text)

    elif filter == 3:
        print("Отличо, теперь введите год издания\n"
              "(Пример: 1981)")
        year = input("Вводите: ")
        try:
            year = int(year) #проверка на соответствие типа данных
        except Exception:
            print("Год введен не корректно"
                  "(Пример: 1988)")
            return None

        text = "\n--------Результат поиска--------\n"
        with open('data.txt', encoding="UTF8") as outfile: #открываем файл для чтения
            json_file = json.load(outfile)

        for id_book in json_file:
            if int(json_file[id_book]["year"]) == year:
                text += (f"ID: {id_book}\n"
                         f"Название: {json_file[str(id_book)]['title']}\n"
                         f"Автор: {json_file[str(id_book)]['author']}\n"
                         f"Год: {json_file[str(id_book)]['year']}\n"
                         f"Статус: {json_file[str(id_book)]['status']}\n\n") #формируем переменную текст

        if text == "\n--------Результат поиска--------\n":
            print(f"Книг c годом издания {year} не найдено\n"
                  f"Для повторной попытки поиска книги воспользуйтесь командой find_book\n\n")
        else:
            print(text)
    else:
        print("Такого варианта нет!\n"
              "1 - поиск по названию\n"
              "2 - поиск по автору\n"
              "3 - поиск по году издания\n"
              "(Пример: 1)\n"
              f"Для повторной попытки поиска книги воспользуйтесь командой find_book\n\n")


def all_books():
    """
    Вывод всех книг
    :return: None
    """
    text = ""
    with open('data.txt', encoding="UTF8") as outfile: #открываем файл для чтения
        json_file = json.load(outfile)

    for id_book in json_file:
        if json_file[id_book]['status'] == True:
            status_book = 'в наличии'
        else:
            status_book = 'выдана'

        text += (f"ID:{id_book}  |Название: {json_file[id_book]['title']} "
                 f" |Автор: {json_file[id_book]['author']}  |Год: {json_file[id_book]['year']} "
                 f" |Статус: {status_book}\n") #формируем переменную text

    print(text)


def update_status_book():
    """
    Обновление статуса книги
    :return: None
    """
    print("Введите ID книги, статус которой хотите изменить\n"
          "(Пример: 1135798)\n")
    id_book = input("Вводите: ")

    try:
        id_book = int(id_book)  #проверка соответсивия типа данных
    except Exception:
        print("Значение ID книги должен состоять из цифр от 0-9\n"
              "Для повторной попытки обновления статуса книги воспользуйтесь командой update_status\n\n")
        return None

    with open('data.txt', encoding="UTF8") as outfile: #открываем файл для чтения
        json_file = json.load(outfile)

    id_book = str(id_book)
    if id_book in json_file:
        print('Отлично, теперь ввдите статус ("в наличии" или "выдана")\n'
              '(Пример: в наличии)\n')
        status = input("Вводите: ").lower().replace(" ", "") #привводим текстовое значение к единому ввиду для расширения возможностей опредления полученных данных

        if status == 'выдана':
            json_file[id_book]["status"] = False
            with open('data.txt', 'w', encoding="UTF8") as outfile: #перезапись файла
                json.dump(json_file, outfile)

            print(f'---------Статус изменен на "выдана" для ID {id_book}--------\n\n')

        elif status == 'вналичии':
            json_file[id_book]["status"] = True
            with open('data.txt', 'w', encoding="UTF8") as outfile: #перезапись файла
                json.dump(json_file, outfile)

            print(f'---------Статус изменен на "в наличии" для ID {id_book}--------\n\n')
        else:
            print("Такого статуса не существует!\n"
                  "Для повторной попытки обновления статуса книги воспользуйтесь командой update_status\n\n")
            return None
    else:
        print("Такого ID не найдено.\n"
              "Для повторной попытки обновления статуса книги воспользуйтесь командой update_status\n\n")
        return None

