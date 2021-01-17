class Book:

    def __init__(self, title, new_author, genre, sub_genre, language):
        self.__title = title
        self.__genre = "{:1s}/{:1s}".format(genre, sub_genre)
        self.__language = language
        self.__author = new_author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_genre(self):
        return self.__genre

    def get_language(self):
        return self.__language

    def get_spine(self):
        auth = "{:1s} {:1s}".format(self.__author.get_first_name(), self.__author.get_last_name())
        if len(auth) > 20:
            auth = (auth[:19] + '.')
        if len(self.__title) > 55:
            title = (self.__title[:54] + '.')
        else:
            title = self.__title
        str2 = "|{:20s}:{:55s}|".format(auth.center(20), title.center(55))
        return str2

    def __str__(self):
        str1 = "Title:      {:1s}\n".format(self.__title)
        str1 += "Author:     {:1s}{:1s}\n".format(self.__author.get_first_name(), self.__author.get_last_name())
        str1 += "Language:   {:1s}\n".format(self.__language)
        str1 += "Genre:      {:1s}\n".format(self.__genre)
        return str1

