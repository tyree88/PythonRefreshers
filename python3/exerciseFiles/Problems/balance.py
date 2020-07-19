class Stack:
    def __init__(self):
        self.items = []
        super().__init__()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return None

    def peek(self):
        if self.items:
            return self.items
        else:
            return None

    def is_empty(self):
        # returns None if stack is empty
        return self.items == None


def balance(symbols):
    # create a dictionary to match the opening and closing symbols
    symbolPairs = {
        "{": "}",
        "[": "]",
        "(": ")"
    }
    openers = symbolPairs.keys()
    myStack = Stack()
    myStack.push(symbols)
    print(myStack.peek())
    index = 0
    while index < len(symbols):
        symbol = symbols[index]
        if symbol in openers:
            myStack.push(symbol)
        else:  # The symbol is a closer
            # if the stack is already empty the symbol is not balanced
            if myStack.is_empty():
                return False
                # if there are still items in the stack, check for a mis-match
            else:
                topItem = myStack.pop()
                if symbol != symbolPairs[topItem]:
                    return False


def main():
    # print("data")
    data = "{"
    balance(data)


if __name__ == "__main__":
    main()
