# TODO: create a basic class
class Book:
    def __init__(self, title, author, pages, prices):
        self.author = author
        self.title = title
        self.pages = pages
        self.prices = prices

    # TODO: create instance methods

    def getPrice(self):
        if hasattr(self, "_discount"):
            return self.prices - (self.prices*self._discount)
        else:
            return self.prices

    def setDiscount(self, amount):
        self._discount = amount


# TODO: create instance of the class
b1 = Book("Book Title", "tyree", 231, 39.95)
print(b1.getPrice())
b1.setDiscount(0.25)
print(b1.getPrice())
print(b1.title)
# TODO : use type() on instance to find class
# useful to compare objects if they are the same time
print(type(b1))

# TODO: use isinstance() to compare a specific instance to a known type
# gives boolean value on if an instance
print(isinstance(b1, Book))
