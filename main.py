import os

def add_book():
    """Добавляет новую книгу в библиотеку."""
    title = input("Введите название книги: ")
    author = input("Введите автора: ")
    year = input("Введите год издания: ")
    availability = input("Книга доступна? (в наличии / выдана): ").lower()
    if availability not in ("в наличии", "выдана"):
        print("Некорректный ввод. Доступность должна быть 'в наличии' или 'выдана'.")
        return
    books.append([title, author,  year, availability])
    print("Книга успешно добавлена!")

def list_books():
    """Выводит список всех книг."""
    if not books:
        print("Библиотека пуста.")
    else:
        for i, book in enumerate(books):
            print(f"{i+1}. Название: {book[0]} - Автор: {book[1]} - Год издания:{book[2]}  - доступность: {book[3] }")

def search_book():
    """Ищет книгу по названию, автору или году."""
    search_term = input("Введите название, автора или год издания: ").lower()
    found_books = []
    for book in books:
        if search_term in book[0].lower() or search_term in book[1].lower() or search_term in book[2].lower():
            found_books.append(book)
    if found_books:
        print("Найденные книги:")
        for i, book in enumerate(found_books):
            print(f"{i+1}. Название: {book[0]} - Автор: {book[1]} - Год издания:{book[2]}  - доступность: {book[3] }")
    else:
        print("Книги не найдены.")

def mark_as_available():
    """Изменяет статус книги на "доступно". """
    list_books()
    index = int(input("Введите номер книги, которую хотите сделать доступной: ")) - 1
    if 0 <= index < len(books):
        books[index][3] = "в наличии"
        print("Книга успешно помечена как доступная!")
    else:
        print("Некорректный номер книги.")

def mark_as_unavailable():
    """Изменяет статус книги на "недоступно". """
    list_books()
    index = int(input("Введите номер книги, которую хотите сделать недоступной: ")) - 1
    if 0 <= index < len(books):
        books[index][3] = "выдана"
        print("Книга успешно помечена как недоступная!")
    else:
        print("Некорректный номер книги.")

def remove_book():
    """Удаляет книгу из библиотеки."""
    list_books()
    index = int(input("Введите номер книги, которую хотите удалить: ")) - 1
    if 0 <= index < len(books):
        del books[index]
        print("Книга успешно удалена!")
    else:
        print("Некорректный номер книги.")

def load_books():
    """Загружает данные книг из файла."""
    global books
    if os.path.exists("books.txt"):
        with open("books.txt", "r") as file:
            books = [line.strip().split(",") for line in file]
            for book in books:
                book[3] = book[3].strip()

def save_books():
    """Сохраняет данные книг в файл."""
    with open("books.txt", "w") as file:
        for book in books:
            file.write(",".join(book) + "\n")

# Загрузка данных при запуске
books = []
load_books()

# Основной цикл программы
while True:
    print("\nМеню:")
    print("1. Добавить книгу")
    print("2. Показать список книг")
    print("3. Найти книгу")
    print("4. Пометить книгу как доступную")
    print("5. Пометить книгу как недоступную")
    print("6. Удалить книгу")
    print("7. Выход")

    choice = input("Введите номер действия: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        list_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        mark_as_available()
    elif choice == "5":
        mark_as_unavailable()
    elif choice == "6":
        remove_book()
    elif choice == "7":
        save_books()
        break
    else:
        print("Некорректный ввод.")