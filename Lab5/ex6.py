class LibraryItem:
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return f"{self.title} has been checked out."
        else:
            return f"{self.title} is already checked out."

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            return f"{self.title} has been returned."
        else:
            return f"{self.title} is already available."

    def get_info(self):
        return f"{self.title} by {self.author} (ID: {self.item_id})"


class Book(LibraryItem):
    def __init__(self, title, author, item_id, genre):
        super().__init__(title, author, item_id)
        self.genre = genre

    def get_info(self):
        return super().get_info() + f", genre: {self.genre}"


class DVD(LibraryItem):
    def __init__(self, title, director, item_id, duration):
        super().__init__(title, director, item_id)
        self.duration = duration

    def get_info(self):
        return super().get_info() + f", duration: {self.duration} minutes"


class Magazine(LibraryItem):
    def __init__(self, title, publisher, item_id, released):
        super().__init__(title, publisher, item_id)
        self.released = released

    def get_info(self):
        return super().get_info() + f", released on: {self.released}"


book = Book("Hunger Games", "Suzanne Collins", "1", "fiction")
dvd = DVD("The Shawshank Redemption", "Frank Darabont", "2", 142)
magazine = Magazine("National Geographic", "National Geographic Society", "3", "31st October 2023")

print(book.get_info())
print(book.check_out())
print(book.return_item())

print(dvd.get_info())
print(dvd.check_out())

print(magazine.get_info())
print(magazine.return_item())
