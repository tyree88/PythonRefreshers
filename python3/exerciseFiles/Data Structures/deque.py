"""
Deque is a double ended Qeueue 
can hold a collection of items 
in deques you can add items to front and back and remove from front and back
use a list to implement a deque - this is an ordered element collection
uses the FIFO and LIFO 
- any data type that can be stored in a list can be stored in a  deque 
- Limited access, because we can only access the data from either end
USE CASE 
- to check if a string is a palindrome

"""


class Deque():

    def __init__(self):
        self.items = []
        super().__init__()

    def add_front(self, item):
        """
        takes item as a parameter and inserts it into the 0th index 
        of the list that is reperesenting the Deque
        Runtime is O(n) -> linear - because everytime you enter into 
        the list the elements in the list must all shift down one
        """
        self.items.insert(0, item)

    def add_rear(self, item):
        """
        takes item as aparameter and inserts it into the last index 
        of the list that is representing the deque
        Runtime is O(1) because appending to the end of a list
        happens in constant time.

        the runtime is linear, or O(n), because when we remove an item
         from the 0th index, all the other items have to shift one index to the left.
        """
        self.items.append(item)

    def remove_front(self):
        # The 0th index in the list is the FRONT

        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop()

    def peak_front(self):
        if self.items:
            return self.items[0]
        else:
            return None

    def peak_rear(self):
        if self.items:
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []


def main():
    deck = Deque()
    deck.add_front('apple')
    deck.add_front('pickle')
    print(deck.items)
    deck.add_rear('chrwissy')
    print(deck.items)
    print(deck.remove_front())
    print(deck.items)
    print(deck.remove_rear())
    print(deck.items)


if __name__ == "__main__":
    main()
