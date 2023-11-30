from lector import get_all_books
from libro import Libro

def main():
    books = get_all_books()
    for book in books:
        libro = Libro(*book)
        libro.visualizarlibro()

if __name__ == "__main__":
    main()