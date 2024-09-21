# Its classic node list that using like pattern
class Node:  # node for list
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:  # list of nodes
    def __init__(self):
        self.head = None  # first in list
        self.end = None  # end in list - mod for fast add new node at end

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.end = new_node  # here we just add new node by replace end node
            return

        self.end.next = new_node  # this method match faster than old
        self.end = new_node

        # old slise of code, here we need to check all nodes in list to find end - it's too long
        """current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node"""

    def append_head(self, data):  # add new node at beginning
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):  # just print all nodes of list
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> " if current_node.next else "\n")
            current_node = current_node.next


linked_list = LinkedList()
linked_list.append(123)
linked_list.append([4, 5, 6])
linked_list.append("aboba")
linked_list.print_list()
linked_list.append_head("biba")
linked_list.print_list()
