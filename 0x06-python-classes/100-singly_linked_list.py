#!/usr/bin/python3
"""
    This class represents a node in a singly linked list.
"""


class Node:
    """
    This class represents a node in a singly linked list.
    """
    def __init__(self, data, next_node=None):
        """
        Init a new node with data and an optional reference to next node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method for the data attribute.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method for the data attribute.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method for the next_node attribute.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for the next_node attribute.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This class represents a singly linked list.
    """
    def __init__(self):
        """
        Initializes an empty singly linked list.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new node into the list in sorted order.
        """
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the list.
        """
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
