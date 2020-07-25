class Node(object):  # node class for doubly linked lists
    def __init__(self, data):
        self.next = None
        self.data = data
        self.previous = None
        super().__init__()

    def __repr__(self):
        """
        repr stands for representation 
        return a printable representation for whatever object we call it on
        """
        return f'Node object: data={self.data}'

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

    def get_previous(self):
        return self.previous

    def set_previous(self, new_previous):
        """Replace existing values of the self.previous attribute with the parameter """
        self.previous = new_previous


class DoublyLinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def __repr__(self):
        return f'Doubly linked list head: {self.head}'

    def is_empty(self):
        # true if head is None or false if not None
        return self.head is None  # return self.head == None

    def insert(self, data):
        """
        create a temp variable that holds the node we want to add 
        input the node with value into temp 
        set the next pointer to node #default value is none
        replace current value of self.next to new node
        now None is now a pointer to a node
        """
        new_node = Node(data)
        new_node.set_next(self.head)  # moving None to second position
        if self.head is not None:  # if self.head is a node object we are setting the new node
            self.head.set_previous(new_node)
        self.head = new_node
        self.count += 1

    def size(self):
        """
        Represents the number of nodes in the Doubly Linked List

        Time complexity is O(n) linear -> every node in the linked list must be visted in order to calculate 
        the size of the linked list 
         """
        return self.count

    def search(self, data):
        """ Tranverses a linked list"""
        if self.head is None:
            return "Linked list is empty -> Nothing to search"
        node = self.head  # this is the Node object
        while node is not None:
            """
            Cases
            - The Nodes data matches what were looking for 
            - the nodes data doesnt match what we are looking for
            """
            if node.get_data() == data:
                return True
            else:
                node = node.get_next()
        return False  # did not find node

    def remove(self, data):  # will remove whatever node comes first with this data value
        if self.head == None:
            return "Linked List is empty no nodes to remove"
        node = self.head
        found = False
        while not found:
            if node.get_data() == data:
                found = True
            else:
                if node.get_next() is None:
                    return "Node with that value is not Present"
                else:
                    node = node.get_next()
        if node.previous is None:
            self.head == node.get_next()
        else:
            # this removes the node mid list and assigns the previous to current
            node.previous.set_next(node.get_next())
            # node past removed node points back at previous node
            node.next.set_previous(node.get_previous())

    def dump_list(self):
        tempnode = self.head
        while(tempnode != None):
            print('Node: ', tempnode.get_data())
            tempnode = tempnode.get_next()


def main():
    itemsList = DoublyLinkedList()
    itemsList.insert(1)
    itemsList.insert("word")
    itemsList.insert(17)
    itemsList.insert(15)
    itemsList.insert(13)
    itemsList.insert(13)
    itemsList.insert(2)
    print(itemsList.remove(100))
    itemsList.remove(15)
    itemsList.dump_list()


if __name__ == "__main__":
    main()
