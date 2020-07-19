from collections import deque


class Queue:
    def __init__(self):
        self.items = []
        super().__init__()

    def enqueue(self, item):
        """
        takes in item and inserts into the 0th index of the list 
        that is representing the Queue

        the runtime is o(n), or linear, because inserting into the 0th
         index of a list forces all the other items in the list to move
          one index to the right
        """
        self.items.insert(0, item)

    def dequeue(self):
        """
        REturns and removes the front most item of the queue 
        this is the last itme of the list. 

        Runtime is O(1) -> constant. cause indexing to the endo f a list happens in constant time.
        """
        if self.items:
            self.items.pop()
        else:
            return None

    def peak(self):
        if self.items:
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == None


# TODO create a new empty deque object that will function as a queue
queue = deque()
my_q = Queue()

# TODO add some items to the queue
my_q.enqueue(1)
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

# TODO print out the queue
print(queue)

# TODO pop off the fron of the queue
queue.popleft()  # this is the front of the deque
print(queue)
