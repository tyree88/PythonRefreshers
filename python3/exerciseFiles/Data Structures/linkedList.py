class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


""" 
linked lists dont contain nodes 
- they have a head attribute and points to the head if one exists
"""


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0  # to keep track of how many nodes are in the list
        super().__init__()

    def get_count(self):
        return self.count

    def insert(self, data):
        # TODO insert a new node
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def find(self, node):
        # TODO find the first item with the given value
        item = self.head
        while(item != None):
            if item.get_data() == item.val:
                return item
            else:
                item = item.get_next()
        return None

    def deleteAt(self, index):
        # TODO delete the item at the given index
        if index > self.count-1:
            return
        if index == 0:
            self.head = self.head.get_next()
        else:
            tempIndex = 0
            node = self.head
            while tempIndex < index - 1:
                node = node.get_next()
                tempIndex += 1
            # point to the node that is after to remove the node
            node.set_next(get.next().get_next())
            self.count -= 1

    def dump_list(self):
        tempnode = self.head
        while(tempnode != None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()


# create a linked list and insert some items
itemList = LinkedList()
itemList.insert(30)
itemList.insert(31)
itemList.insert(32)
itemList.insert(32)
itemList.insert(330)
itemList.dump_list()

# exercise the list
print(f"Item count: {itemList.get_count}")
print(f'Finding item: {itemList.find(30)}')
print(f'Finding item: {itemList.find(100)}')

# delete item
itemList.deleteAt(3)
print(f'item count: {itemList.get_count()')
