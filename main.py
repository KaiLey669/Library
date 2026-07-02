def book_list_view(library: dict) -> None:
    if not library:
        print("Книги отсутствуют.")
        return

    print("\nКниги в библиотеке:")
    for i, (key, value) in enumerate(library.items(), 1):
        status = get_availability_status(value)
        print(f"{i}. Название - {key}; Автор - {value["author"]}; Год - {value['year']}; Статус - {status}")


def validate_book_data(title: str, author: str, year: int) -> bool:
    return isinstance(title, str) and title != "" and isinstance(author, str) and isinstance(year, int)


def add_book(books: dict, title: str, author: str, year: int | None) -> None:
    if title in books:
        input_data = input("\nКнига уже добавлена. Хотите обновить данные? (Да/Нет): ").lower().strip()
        if input_data == "да":
            books[title]["author"], books[title]["year"] = author, year
            print(f"\nДанные по книге \"{title}\" обновлены.")
        else:
            print("\nДанные не обновлены.\n")
    else:
        books[title] = {"author": author, "year": year, "availability": None}
        print(f"\nКнига \"{title}\" добавлена в библиотеку.")


def try_add_book(books: dict):
    title = get_input_title()
    author = get_input_author()
    year = get_input_year()
    add_book(books, title, author, year)


def get_input_title() -> str:
    while True:
        title = input("\nВведите название книги: ").strip()
        if title:
            return title
        else:
            print("Введена пустая строка. Повторите ввод.")


def get_input_author() -> str:
    while True:
        author = input("\nВведите автора: ").strip()
        if author:
            return author
        else:
            print("Введена пустая строка. Повторите ввод.")


def get_input_year() -> int | None:
    year = None
    while not year:
        try:
            year = int(input("\nВведите год издания: "))
            if year <= 0:
                raise ValueError
        except ValueError:
            year = None
            print("Введено неверное значение. Повторите попытку.\n")

    return year


def remove_book(books: dict, title: str) -> None:
    if title in books:
        del books[title]
        print(f"\nКнига {title} удалена.\n")
        return

    print("Книга с указанным названием не найдена.")


def try_remove_book(books: dict):
    title = input("\nВведите название книги: ").strip()
    remove_book(books, title)


def issue_book(books: dict, title: str) -> None:
    if title not in books:
        print("\nКнига отсутствует в библиотеке.")
        return

    if books[title]["availability"]:
        books[title]["availability"] = False
        print(f"\nКнига \"{title}\" успешно выдана.")
    else:
        print(f"\nКнига \"{title}\" уже выдана или еще не был проставлен статус.")


def return_book(books: dict, title: str) -> None:
    if title not in books:
        print("\nКнига отсутствует в библиотеке.")
        return

    if books[title]["availability"]:
        print(f"\nКнига {title} уже в наличии.")
    else:
        books[title]["availability"] = True
        print(f"\nКнига \"{title}\" поступила в библиотеку.")


def try_change_status(books: dict) -> None:
    title = input("\nВведите название книги: ").strip()
    if title not in books:
        print("Книга отсутствует в библиотеке")
        return

    choice = input("\nКак изменить статус? (Вернуть/Отдать): ").lower().strip()
    if choice == "вернуть":
        return_book(books, title)
    elif choice == "отдать":
        issue_book(books, title)
    else:
        print("Введено неверное значение.")


def find_book(books: dict, title: str) -> None:
    book = books.get(title)
    if book is None:
        print(f"Книга \"{title}\" отсутствует в библиотеке.")
        return

    print_book_info(book, title)


def get_availability_status(book: dict | None) -> str:
    if book["availability"] is None:
        return "Книга в библиотеке, но статус не определен"
    return "Книга доступна" if book["availability"] else "Книга выдана"


def print_book_info(book: dict | None, title: str) -> None:
    status = get_availability_status(book)
    print(f"\nИнформация по книге \"{title}\":",
          f"Автор - {book["author"]}",
          f"Год издания - {book["year"]}",
          f"Статус - {status}",
          sep="\n")


def start_library(books: dict) -> None:
    print("Приложение \"Бибилиотека\" запущено.",
          "Доступны следующие действия:",
          "1 - Вывести всю библиотеку",
          "2 - Добавить книгу.",
          "3 - Удалить книгу",
          "4 - Изменить статус книги.",
          sep="\n")

    while True:
        input_word = input("\nВведите значение: ").strip().lower()
        if input_word == "exit":
            print("\nЗавершение работы программы.")
            break
        elif input_word == "1":
            book_list_view(books)
        elif input_word == "2":
            try_add_book(books)
        elif input_word == "3":
            try_remove_book(books)
        elif input_word == "4":
            try_change_status(books)
        else:
            print("Некорректное значение. Попробуйте еще раз.\n")


books = {
    "Оно": {"author": "Стивен Кинг",
            "year": 1986,
            "availability": True}
}


start_library(books)
