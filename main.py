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
    "Оно": ["Стивен Кинг", 1986, "В наличии"]
}

book_list_view(books)
