21 - Ducos, Janine Chrisha M.           
9 - Samat
10/15/26
Q2 FA 1 CS

class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def display_info(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")


class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.__number_of_pages = 1
        self.set_number_of_pages(number_of_pages)

    def get_number_of_pages(self):
        return self.__number_of_pages

    def set_number_of_pages(self, number_of_pages):
        if isinstance(number_of_pages, int) and number_of_pages > 0:
            self.__number_of_pages = number_of_pages
        else:
            print("The number of pages must be positive.")

    def display_info(self):
        super().display_info()
        print(f"Number of pages: {self.__number_of_pages}")


class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = 1
        self.set_issue_number(issue_number)

    def get_issue_number(self):
        return self.__issue_number

    def set_issue_number(self, issue_number):
        if isinstance(issue_number, int) and issue_number > 0:
            self.__issue_number = issue_number
        else:
            print("The issue number must be positive.")

    def display_info(self):
        super().display_info()
        print(f"Issue number: {self.__issue_number}")


# Creating objects
publication1 = Publication(
    "Journal of Experimental Psychology",
    "Ratchiff, R. & Van Dongen, H."
)
publication2 = Publication("PISAY LIFE", "Rose Canlas")

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("El Filibusterismo", "Jose Rizal", 96)

magazine1 = Magazine("National Geographic", "Various Authors", 202)
magazine2 = Magazine("The History of Lily Hill", "Sophia Cruz", 12)


# Printing Publication information
print("Publication Information:")
publication1.display_info()
print()
publication2.display_info()


# Printing Book information and testing validation
print("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()
print("Getter:", book1.get_number_of_pages())

print()
book2.display_info()
print("Getter:", book2.get_number_of_pages())


# Printing Magazine information and testing validation
print("\nMagazine Information:")
magazine1.set_issue_number(-202)
magazine1.display_info()
print("Getter:", magazine1.get_issue_number())

print()
magazine2.display_info()
print("Getter:", magazine2.get_issue_number())
