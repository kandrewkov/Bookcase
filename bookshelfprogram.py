from author import Author
from bookshelf import Bookshelf
from book import Book

def menu():
    print("Menu")
    print("0 - Exit")
    print("1 - Add a book to the next available spot")
    print("2 - Insert a book into a specific spot")
    print("3 - Look at the info of a book")
    print("4 - Remove a book")
    print("5 - Print the bookshelf")
    key = int(input())
    return key


def f0(my_bookshelf):
    return 0


def f1(my_bookshelf):
    print("Enter the book information as requested.")
    title = input("Enter the title:\n")
    author_name = input("Enter the author:\n")
    genre = input("Enter the genre of the book:\n")
    subgenre = input("Enter the subgenre of the book:\n")
    lang = input("Enter the language of the book:\n")
    author_name.strip()
    last_name, first_name = tuple(author_name.split(","))
    new_author = Author(last_name, first_name)
    new_book = Book(title, new_author, genre, subgenre, lang)
    if my_bookshelf.add_book(new_book):
        print("Adding the book was successful")
    else:
        print("Adding error")
    return 1


def f2(my_bookshelf):
    i = int(input("Which shelf?"))
    print(my_bookshelf.shelf_str(i, numbered=True))
    j = int(input("Which slot?\n"))
    if my_bookshelf.get_contents()[i][j] is not None:
        print("This slot already contains a book")
        return 1
    print("Enter the book information as requested.")
    title = input("Enter the title:\n")
    author_name = input("Enter the author:\n")
    genre = input("Enter the genre of the book:\n")
    subgenre = input("Enter the subgenre of the book:\n")
    lang = input("Enter the language of the book:\n")
    author_name.strip()
    last_name, first_name = tuple(author_name.split(","))
    new_author = Author(last_name, first_name)
    new_book = Book(title, new_author, genre, subgenre, lang)
    if my_bookshelf.insert_book(new_book, i, j):
        print("Inserting the book was successful")
    return 1


def f3(my_bookshelf):
    i = int(input("Which shelf?\n"))
    print(my_bookshelf.shelf_str(i, numbered=True))
    j = int(input("Which slot?\n"))
    print(my_bookshelf.get_contents()[i][j])
    return 1


def f4(my_bookshelf):
    i = int(input("Which shelf?\n"))
    print(my_bookshelf.shelf_str(i, numbered=True))
    j = int(input("Which slot?\n"))
    if my_bookshelf.get_contents()[i][j] is None:
        print("Already is empty")
    elif my_bookshelf.remove_book(i, j):
        print("Removing the book was successful")
    return 1


def f5(my_bookshelf):
    print(my_bookshelf)
    return 1


def main():
    functions = [f0, f1, f2, f3, f4, f5]
    # filename = input("Enter the name of the file containing the book data:\n")
    filename = "book_data1.csv"
    try:
        book_count = 0
        file = open(filename, "r")
        my_name = input("What is your name?\n")
        my_name = "Mike"
        num = int(input("How many shelves do you have in your bookshelf?\n"))
        width = int(input("How many books fit onto one shelf?\n"))
        my_bookshelf = Bookshelf(my_name, num, width)
        c = num * width                # how many slots
        for line in file:
            line = line.rstrip()
            row = tuple(line.split(","))
            # Structure of the file
            # The book information is stored in a csv-file so that the info of one book is on one line.
            # The information contains the books title, author's last name and first name(s),
            # the language, genre and subgenre of the book. The information is separated by commas.
            if len(row) != 6:
                print("Error in line: {:1s}".format(line))
            else:
                title, last_name, first_name, lang, genre, sub_genre = row
                new_author = Author(last_name, first_name)
                new_book = Book(title, new_author, genre, sub_genre, lang)
                my_bookshelf.add_book(new_book)
                book_count += 1         # how many books add to bookshelf
        print(my_bookshelf)
        if book_count > c:
            print("The bookshelf did not fit all the books in the file.")
            print("The bookshelf is now full with the first {:1d} books.".format(c))
        else:
            print("Added {:1d} books into the bookshelf from file.".format(book_count))

            while True:
                if functions[menu()](my_bookshelf) == 0:
                    return print("Program ends.")
    except OSError:
        print("ERROR in reading the file.")
        print("Program ends.")


main()
