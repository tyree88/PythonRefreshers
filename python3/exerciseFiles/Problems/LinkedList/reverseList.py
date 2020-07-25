"""
Do a linked list reverse function both iteratively and recurvsively
"""


class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

    def get_data(self):
        return self.data
        super().__init__()

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = count
        super().__init__()

    def insert(self, data):
        node = Node(data)
        node.set_next(self.head)
        self.head = node
        self.count += 1

    def reverseLinkedList(self, head):
        """
        Keep 2 pointers ,1 to the previous elements and 1 to the current elements

        """
        prev = null
        curr = self.head
        while(curr != None):
            """
            Another common pattern - preserver the pointer to the next node in the list. 
            preserve the pointer to the next object in memory that we want to visit -> in a reference variable
            """
            preservedNextNode = curr.next
            curr.next = prev
            prev = curr
            curr = preservedNextNode
        """
        Using pointer to rename things to make it clear what is happening
        prev is pointing to the last element wheb the above iteration ends
        ->this is the head of the new reversed linkedlist
        """
        reversedLinkedListHead = prev

        return reversedLinkedListHead(me.next)

    def reversedListRecursive(self, me):
        if (me == null or me.next == null):
            return me

        """
        We need to preserve the reference to the last node in the original
        linked list since it will be the head of the new reversed linked list.

        We "bubble" that value up in our calls to the root caller by recursing
        deep first to get reference to the last node (and in the process creating
        n stack frames on the call stack, each with reference to a node)
        """
        headOfReversedList = Node(me.next)
        """
        when the base case hit and returns, we will return to 1 node before the final node
        in thel list. Then we point to the node 'nodeToMyRight' to 'me' node.

        then we cut off 'me'.next node because 'me' may be the last nodei n the reserved linked list
        """
        nodeToMyRight = Node(me.next)
        nodeToMyRight.next = me
        me.next = null
        return headOfReversedList


def main():
    data =


if __name__ == "__main__":
    main()
