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


books = {
    "Оно": {"author": "Стивен Кинг",
            "year": 1986,
            "availability": "В наличии"}
}

book_list_view(books)
add_book(books,"Кэрри", "Стивен Кинг", 1974)
book_list_view(books)
add_book(books,"Кэрри", "Стивен Кинг", 2001)
book_list_view(books)
