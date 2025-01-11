"""
    File: writer_bot.py
    Author: Samyak Gurung
    Course: CSC 120, Spring 2024
    Purpose: this code uses huffman method to present
    data where the data is initially sorted using 
    a two data information in preorder and postorder
    method and return the requested data given in binary
    or human and a postordered values
"""
class BinaryTree:
    """
    the class represents a Binary tree holding three
    initial place holders the value and two children
    
    Where the value node is contains an integer and the
    left and right node contians None which later can hole
    Binary tree class or integers if they are a leaf node
    and whether they are leaf or parent node.
    """
    def __init__(self, value):
        self._node = value
        self._left = None
        self._right = None

    def node(self):
        return self._node

    def left(self):
        return self._left

    def right(self):
        return self._right

    def add(self, value):
        if value < self._node:
            if self._left is None:
                self._left = BinaryTree(value)
            else:
                self._left.add(value)
        else:
            if self._right is None:
                self._right = BinaryTree(value)
            else:
                self._right.add(value)

def sort(list1, list2, tree):
    """
    is a function that sorts the
    the elements in a tree using the
    two lists
    parameter: two lists containing integers
    and an object initially containing none
    return: Object containing sorted binary
    tree
    """
    if not list2:
        return tree
    else:
        node_index = mid_helper(list1, list2, 0)
        node_value = list2[node_index]

        if tree is None:
            tree = BinaryTree(int(node_value)) 

        left = list2[:node_index]
        left1 = side(list1, left, [])
        right = list2[node_index + 1:]
        right1 = side(list1, right, [])

        tree._left = sort(left1, left, tree.left())
        tree._right = sort(right1, right, tree.right())

        return tree

def side(list1, compare, new):
    """
    returns seperated list
    """
    if not list1:
        return new
    if list1[0] in compare:
        new.append(list1[0])
    return side(list1[1:], compare, new)

def mid_helper(list1, list2, counter):
    """
    gets the node from the list
    parameter: 2 lists and integer counter
    return: integer
    """
    if list1[0] == list2[0]:
        return counter
    else:
        return mid_helper(list1, list2[1:], counter + 1)

def decode(tree, binary, result):
    """
    sends the requested result
    parameter: object, list and list
    return: list containing the result
    """
    current = tree
    for val in binary: 
        if val == '0':
            current = current.left()
        else:
            current = current.right()

        if not current.left() and not current.right():
            result.append(current.node())
            current = tree 
    return result

def postorder(tree, post):
    """
    stores the values from the binary tree
    to postorder in a list
    parameter: empty list and a binarytree
    return: list containing postorder set
    elements
    """
    if tree is None:
        return post
    post = postorder(tree.left(), post)
    post = postorder(tree.right(), post)
    post += str(tree.node()) + " "
    return post

def main():
    file = open(input('Input file:'))
    lines = []
    for line in file:
        lines.append(line.strip())
    file.close()

    list1 = []
    for x in lines[0].split():
        list1.append(int(x))

    list2 = []
    for x in lines[1].split():
        list2.append(int(x))

    binary = lines[2]  

    tree = sort(list1, list2, None)
    decoder = decode(tree, binary, [])
    finale = []
    for val in decoder:
        finale.append(str(val))
    print(postorder(tree, ''))
    print(''.join(finale))
main()
