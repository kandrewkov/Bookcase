class Bookshelf:
    def __init__(self, owner, shelwes_number, shelwes_width):
        self.__owner = owner
        self.__shelves = []
        for i in range(shelwes_number):
            self.__shelves.append([])
            for j in range(shelwes_width):
                self.__shelves[i].append(None)


    def get_owner(self):
        return self.__owner

    def get_contents(self):
        return self.__shelves

    def get_shelf_n(self):
        return len(self.__shelves)

    def get_shelf_w(self):
        return len(self.__shelves[0])

    def is_full(self):
        for shelf in reversed(self.__shelves):
            for book in reversed(shelf):
                if book is None:
                    return False
        return True

    def add_book(self, new_book):
        if self.is_full():
            return False
        else:
            for i, shelf in enumerate(self.__shelves):
                for j, book in enumerate(shelf):
                    if book is None:
                        self.__shelves[i][j] = new_book
                        return True

    def insert_book(self, book, i, j):
        if self.__shelves[i][j] is None:
            self.__shelves[i][j] = book
            return True
        else:
            return False

    def remove_book(self, i, j):
        self.__shelves[i][j] = None

    def shelf_str(self, i, numbered=False):
        str1 = ""
        for mybook in self.__shelves[i]:
            if mybook is None:
                str1 += "|                    :                                                       |\n"
                str1 += "------------------------------------------------------------------------------\n"
                continue
            str1 += mybook.get_spine() + "\n"
            str1 += "------------------------------------------------------------------------------\n"
        return str1

    def __str__(self):
        str2 = ""

        for i in range(len(self.__shelves)):
            str2 += "shelf #" + str(i) + "\n"
            str2 += "------------------------------------------------------------------------------\n"
            str2 += self.shelf_str(i)
        return str2
S