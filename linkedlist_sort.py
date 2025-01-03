"""
    File: linkedlist_sort.py
    Author: Samak Gurung
    Course: CSC 120, Fall 2024
    Purpose: This code iterates through the file and
    stores the values of a file in a linked list
    it uses two objects LinkedList and Node that
    is used to store the values from file by 
    iterating through the list and creates
    a new linked list that sorts and stores the list
"""
class LinkedList:
    """
    This class represents LinkedList that stores
    the valuees in a node by node basis using class Node

    The class stores values in the form linked list
    where the every node is stored through the class
    Node. It also sorts the values inside in decending order
    """
    def __init__(self):
        self._head = None
    
    # sort the nodes in the list
    def sort(self):
        """
        Method that iterates through the Linked list and sorts
        the list by adding them to a new list

        Returns: A modified Linked list
        """
        new_l = LinkedList()
        
        while self._head != None:
            curr_element = self.remove()
            if curr_element.value() != ' ':
                if new_l._head is None:
                    new_l.add(curr_element)
                else:
                    curr_value = int(curr_element.value())
                    
                    if int(new_l._head.value()) < curr_value:
                        new_l.add(curr_element)
                    else:
                        current = new_l._head
                        prev = None
                        
                        # Finds the correct insertion poiNT
                        while current != None:
                            if int(current.value()) >= curr_value:
                                prev = current
                                current = current._next
                            else:
                                break
                            
                        if prev == None:  
                            new_l.add(curr_element)
                        else:
                            prev._next = curr_element
                            curr_element._next = current

        self._head = new_l._head
        return self

    
    
    # add a node to the head of the list
    def add(self, node):
        node._next = self._head
        self._head = node
        
    # remove a node from the head of the list and return the node
    def remove(self):
        assert self._head != None
        _node = self._head
        self._head = _node._next
        _node._next = None
        return _node
    
    # insert node2 after node1
    def insert(self, node1, node2):
        assert node1 != None
        node2._next = node1._next
        node1._next = node2
    
    def __str__(self):
        string = 'List[ '
        curr_node = self._head
        while curr_node != None:
            string += str(curr_node)
            curr_node = curr_node.next()
        string += ']'
        return string

class Node:
    """
    This class represents Nodes and the next memory
    location.

    The class stores values in the form of a singlr Node 
    where the data stored in integer and it points to None
    """
    def __init__(self, value):
        self._value = value
        self._next = None
    
    def __str__(self):
        return str(self._value) + "; "
    
    def value(self):
        return self._value
    
    def next(self):
        return self._next
def main():
    """
    Runs the fuction and iterates through the file
    """
    file = open(input())
    Link = LinkedList()
    for line in file:
        line = line.split()
        for val in line:
            node = Node(val)
            Link.add(node)
    Link_ = Link.sort()
    print(Link_)
main()
