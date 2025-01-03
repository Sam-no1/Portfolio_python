from linked_list import LinkedList, Node
"""
File: friends.py
Author: Samyak Gurung
Course: CSC 120, Fall 2024
Purpose: This code uses Linked list and node which
    is used to store name of people and their friends
    which is then stored and which the request user
    for input used to find common friends between two 
    people
"""
def name_placer(line, people):
    """
    compares and stores the names
    in the linked list and adds nodes
    to the inner linked list

    parameter: line is a section from a file and
    people is the linked list class
    """
    name1 = find_or_add(line[0], people)
    name2 = find_or_add(line[1], people)

    name1.add_friend(name2)
    name2.add_friend(name1)

def find_or_add(name, people):
    """
    Finds a node by name or adds a new node if it does not exist.
    parameters: name is a string and people is the linked list
    class
    """
    # Check if the node already exists
    curr = people._head
    while curr is not None:
        if curr._name == name:
            return curr
        curr = curr._next  

    new_node = Node(name)
    people.add(new_node)
    return new_node

def compare(people):
    """
    Compares friends of nodes and creates 
    a new linked list with friends.
    parameter: people is linked lis class
    """
    name_1 = input('Name 1:')
    name_2 = input('Name 2:')
    person1 = node_finder(name_1, people)
    person2 = node_finder(name_2, people)

    if person1 is None:
        return "ERROR: Unknown person " + name_1

    if person2 is None:
        return "ERROR: Unknown person " + name_2

    curr = person1._linked_list._head
    new = LinkedList()
    # checks for common friends
    while curr is not None:
        current = person2._linked_list._head  
        while current is not None:
            if curr._name == current._name:
                if new.find(curr._name) is None:
                    new.add(Node(curr._name))
            current = current._next
        curr = curr._next
    return new

def print_list(comp):
    """
    Prints the the content in the list
    parameter: comp linked list class
    """
    curr = comp._head
    if curr != None:
        print('Friends in common:')
        while curr != None:
            print(curr._name)
            curr = curr._next

def node_finder(name, people):
    """
    searches whether the
    node existsin the linked list
    parameter: string and class
    """
    curr = people._head
    while curr != None:
        if curr._name == name:
            return curr
        curr = curr._next
    return None

def main():
    file = open(input('Input file:' ))
    people = LinkedList()
    for line in file:
        line = line.split()
        name_placer(line, people)    
    comp = compare(people)
    if type(comp) == str:
        print(comp)
    else:
        comp.sort()
        print_list(comp)
    file.close()
main()