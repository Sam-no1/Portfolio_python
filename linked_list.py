"""
File: friends.py
Author: Samyak Gurung
Course: CSC 120, Fall 2024
Purpose: this code stores classes
    linked list and node that is 
    used as a helper or import file
    used in storing data about the file
"""
class LinkedList:
    """
    This class represents LinkedList that stores
    the Names in a node by node basis using class Node

    The class stores values in the form linked list
    where the every node is stored through the class
    Node. It also sorts the values inside in decending order
    """
    def __init__(self):
        self._head = None

    def add(self, target):
        if self.find(target._name) is None:
            target._next = self._head
            self._head = target

    def find(self, name):
        curr = self._head
        while curr is not None:
            if curr._name == name:
                return curr
            curr = curr._next
        return None

    def is_empty(self):
        return self._head is None

    def remove(self):
        if self._head is None:
            return None
        removed_node = self._head
        self._head = self._head._next
        removed_node._next = None
        return removed_node

    def insert_sorted(self, node):
        """
        Inserts a node in alphabetical order by name.
        """
        if self._head is None or node._name < self._head._name:
            node._next = self._head
            self._head = node
        else:
            current = self._head
            while current._next is not None and current._next._name < node._name:
                current = current._next
            node._next = current._next
            current._next = node

    def sort(self):
        """
        Sorts the linked list alphabetically by name.
        """
        sorted_list = LinkedList()
        while self._head is not None:
            node = self.remove()
            if node and node._name.strip():  # Ignore empty values
                sorted_list.insert_sorted(node)
        self._head = sorted_list._head
        return self

    def __str__(self):
        result = " "
        curr_node = self._head
        while curr_node is not None:
            result += str(curr_node) + " , "
            curr_node = curr_node._next
        return result + "None"


class Node:
    """
    This class represents Names or nodes that stores
    the valuees in a node by node basis using class Node

    """
    def __init__(self, name):
        self._name = name
        self._linked_list = LinkedList()
        self._next = None

    def add_friend(self, friend):
        if self._linked_list.find(friend._name) is None:
            self._linked_list.add(Node(friend._name))

    def friends(self):
        return self._linked_list

    def value(self):
        return self._name

    def __str__(self):
        return self._name
