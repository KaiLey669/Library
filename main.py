def book_list_view(library: dict) -> None:
    if not library:
        print("Книги отсутствуют.")
        return

    print("Названия книг:")
    for i, book in enumerate(library, 1):
        print(f"{i}. {book}")


def validate_book_data(title: str, author: str, year: int) -> bool:
    return isinstance(title, str) and isinstance(author, str) and isinstance(year, int)


def add_book(books: dict, title: str, author: str, year: int) -> None:
    if not validate_book_data(title, author, year):
        print(f"\nДля добавления книги использованы некорректные данные.\n")
        return

    if title in books:
        input_data = input("\nКнига уже добавлена. Хотите обновить данные? (Да/Нет): ").lower().strip()
        if input_data == "да":
            books[title]["author"], books[title]["year"] = author, year
            print(f"\nДанные по книге \"{title}\" обновлены.\n")
        else:
            print("\nДанные не обновлены.\n")
    else:
        books[title] = {"author": author, "year": year, "availability": None}
        print(f"\nКнига \"{title}\" добавлена в библиотеку.\n")


def remove_book(books: dict, title: str) -> None:
    if title in books:
        del books[title]
        print(f"\nКнига {title} удалена.\n")
        return

    print("\nКнига с указанным названием не найдена.\n")


def issue_book(books: dict, title: str) -> None:
    if title not in books:
        print("\nКнига отсутствует в библиотеке.\n")
        return

    if books[title]["availability"]:
        books[title]["availability"] = False
        print(f"\nКнига {title} успешно выдана.\n")
    else:
        print(f"\nКнига {title} уже выдана или еще не был проставлен статус.\n")


def return_book(books: dict, title: str) -> None:
    if title not in books:
        print("\nКнига отсутствует в библиотеке.\n")
        return

    if books[title]["availability"]:
        print(f"\nКнига {title} уже в наличии.\n")
    else:
        books[title]["availability"] = True
        print(f"\nКнига {title} поступила в библиотеку.\n")


books = {
    "Оно": {"author": "Стивен Кинг",
            "year": 1986,
            "availability": True}
}

book_list_view(books)
issue_book(books, "Оно")
add_book(books,"Кэрри", "Стивен Кинг", 1974)
book_list_view(books)
return_book(books, "Кэрри")
return_book(books, "Кэрри")
issue_book(books, "Кэрри")
issue_book(books, "Кзрри")
return_book(books, "Кэрри")
