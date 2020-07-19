class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        """
        Accepts an item as a parameter and appends it to the end of the list (The right is the end of the list). 
        continues to insert into right.
        this returns nothing

        Runtime: the runtime for the push is O(1) -> constant time, 
        because appending to the end of the list happens in constant time.
        """
        self.items.append(item)

    def pop(self):
        # TODO create a new empty stack
        """
        Removes and returns the last item for the list
        this is considered the TOP of the list -> this is the right of the list

        the runtime here is O(1) -> because all it does is index to the last 
        items of the list
        Create to condition to make sure there is a item in the stack
        """
        if self.items:
            return self.items.pop()
        else:
            return None

    def peek(self):
        """
        This method runs in constant time because indexing into a list is O(n)
        """
        if self.items:
            return self.items[-1]
        else:
            return None

    def size(self):
        # This method runs in constant time
        # finding length of list depends on list len n -> O(n)
        return len(self.items)

    def isEmpty(self):
        # If not equal to an empty list it will return false.
        return self.items == None


def main():
    itemsList = Stack()
    # TODOpush item onto the stack
    itemsList.push(1)
    itemsList.push("apple")
    itemsList.push('milk')
    print(itemsList.peek())
    print(itemsList.size())
    # TODOprint stack elements

    # TODOpop off stack elements
    itemsList.pop()
    itemsList.pop()
    # Check if empty
    print(itemsList.isEmpty())


if __name__ == "__main__":
    main()
