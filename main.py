def book_list_view(library: dict) -> None:
    if not library:
        print("Книги отсутствуют.")
        return

    print("Названия книг:")
    for i, book in enumerate(library, 1):
        print(f"{i}. {book}")
    print()


def validate_book_data(title: str, author: str, year: int):
    return False if type(title) != str or type(author) != str or type(year) != int else True


def add_book(title: str, author: str, year: int) -> None:
    if not validate_book_data(title, author, year):
        print(f"Для добавления книги использованы некорректные данные.\n")
        return

    global books
    if title in books:
        input_data = input("Книга уже добавлена. Хотите обновить данные? (Да/Нет): ").lower().strip()
        if input_data == "да":
            books[title]["author"], books[title]["year"] = author, year
            print(f"Данные по книге \"{title}\" обновлены.\n")
        elif input_data == "нет":
            print(f"Данные по книге \"{title}\" остались без изменений.\n")
        else:
            print("Введено некорректное значение. Данные не обновлены.\n")
    else:
        books[title] = {"author": author, "year": year, "availability": None}
        print(f"Книга \"{title}\" добавлена в библиотеку.\n")


books = {
    "Оно": {"author": "Стивен Кинг",
            "year": 1986,
            "availability": "В наличии"}
}

book_list_view(books)
add_book("Кэрри", "Стивен Кинг", 1974)
book_list_view(books)
add_book("Кэрри", "Стивен Кинг", 2001)
book_list_view(books)
