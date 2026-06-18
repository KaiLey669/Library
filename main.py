def book_list_view(library: dict) -> None:
    if not library:
        print("Книги отсутствуют.")
        return

    print("Названия книг:")
    index = 0
    for book in library:
        index += 1
        print(f"{index}. {book}")


books = {
    "Оно": {"author": "Стивен Кинг",
            "year": 1986,
            "availability": "В наличии"}
}

book_list_view(books)
