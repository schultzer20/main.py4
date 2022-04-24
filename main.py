'''Class Template for a singly linked list Head -> Tail convention
Exercise Part starts at line 40'''

# class for holding the data, defaults to empty node if no data is given


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None  # pointer to the next node

# Class for managing the list and nodes


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)

        if self.head is None:  # if the node is empty, the new node is the head
            self.head = node
        else:  # if not empty iterate through items and append new node at the end (tail)
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self.size += 1  # always update the size to prevent costly iterations to get the size

    # defining iteration function to make iterating over nodes in the list possible
    def __iter__(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def get_size(self):
        return self.size

    '''
    Exercise Part 1,2 and 3:

    Implement the given methods below according to the requirements in the exercise sheet.
    return the correct data types and values
    '''

    def clear(self):
        while self.head is not None:
            temp = self.head
            self.head = self.head.next
            temp = None
            return

    def get_data(self, data):
        for node in self.__iter__():
            if data == node:
                return data
        return False

    def delete(self, data):
        temp = self.head
        if temp is not None:
            if temp.data == data:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == data:
                break
            previous = temp
            temp = temp.next
        if temp is None:
            return
        previous.next = temp.next
        temp = None
        return


'''Exercise Part 4: Copy the code from the singly linked list implementation and rewrite it
    to implement a doubly linked list according to the exercise sheet. Dont forget to change the names of the classes
    in the code to reflect the new class name (NodeDLL instead of Node).
    '''


class NodeDLL:
    def __init__(self, data=None):
        self.data = data
        self.next = None  # pointer to the next node
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        newnode = NodeDLL(data)
        newnode.next = None

        if self.head == None:  # if the node is empty, the new node is the head
            newnode.previous = None
            self.head = newnode
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = newnode
        newnode.previous = last
        self.size += 1  # always update the size to prevent costly iterations to get the size
        return

    # defining iteration function to make iterating over nodes in the list possible
    def __iter__(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def get_size(self):
        return self.size

    '''Exercise Part 5 and 6:
    Complete the classes below to implement a stack and queue data structure. You are free to use built-in
    methods but you have to complete all methods below. Always return the correct data type according
    to the exercise sheet'''


class MyStack:
    def __init__(self):
        self.elements = []

    def push(self, data):
        self.elements.append(data)
        return

    def pop(self):
        if len(self.elements) > 0:
            return self.elements.pop()

    def top(self):
        if len(self.elements) > 0:
            return self.elements[-1]

    def size(self):
        return len(self.elements)


class MyQueue:
    def __init__(self):
        self.elements = []

    def push(self, data):
        self.elements.append(data)
        return

    def pop(self):
        if len(self.elements) > 0:
            return self.elements.pop(0)

    def show_left(self):
        if len(self.elements) > 0:
            return self.elements[0]

    def show_right(self):
        if len(self.elements) > 0:
            return self.elements[-1]

    def size(self):
        return len(self.elements)
