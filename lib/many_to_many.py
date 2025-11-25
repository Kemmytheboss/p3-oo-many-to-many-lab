class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise Exception("Name must be a valid string.")
        self._name = value

    # Return all contracts linked to this author
    def contracts(self):
        return [c for c in Contract.all if c.author == self]

    # Return all books linked to this author (via contracts)
    def books(self):
        return [c.book for c in self.contracts()]

    # Sign a new contract
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    # Sum of royalties percentages across all contracts
    def total_royalties(self):
        return sum(c.royalties for c in self.contracts())


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise Exception("Title must be a valid string.")
        self._title = value

    # Return all contracts linked to this book
    def contracts(self):
        return [c for c in Contract.all if c.book == self]

    # NEW: Return all authors linked to this book
    def authors(self):
        return [c.author for c in self.contracts()]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    # --- AUTHOR SETTER ---
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be an instance of Author class.")
        self._author = value

    # --- BOOK SETTER ---
    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("Book must be an instance of Book class.")
        self._book = value

    # --- DATE SETTER ---
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("Date must be a string.")
        self._date = value

    # --- ROYALTIES SETTER ---
    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("Royalties must be an integer.")
        self._royalties = value

    # CLASS METHOD: return all contracts for a given date
    @classmethod
    def contracts_by_date(cls, date):
        return [c for c in cls.all if c.date == date]
