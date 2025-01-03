import csv
import string

class LinkedList:
    """
    This class represents LinkedList that stores
    the words in a node by node basis using class Node

    The class stores words in the form linked list
    where the every node is stored through the class
    Node. It also sorts the values inside in decending order
    according to its occurance
    """
    def __init__(self):
        self._head = None

    def sort(self):
        if self._head is None:
            return
        
        sorted_list = LinkedList()
        current = self._head
        #loops through the code and inserts and aranges new nodes
        while current is not None:
            next_node = current._next  
            self._insert_sorted(sorted_list, current)
            current = next_node  
        
        self._head = sorted_list._head  

    def _insert_sorted(self, sorted_list, node):
        if sorted_list._head is None or sorted_list._head._count < node._count:
            node._next = sorted_list._head
            sorted_list._head = node
        else:
            current = sorted_list._head
            while current._next is not None and current._next._count >= node._count:
                current = current._next
            node._next = current._next
            current._next = node

    def update_count(self, word):
        """
        updates the count by iterating through 
        the list and adding 1
        """
        curr = self._head
        while curr is not None:
            if word == curr._word:
                curr._count += 1
                return
            curr = curr._next
        
        new_node = Node(word)
        new_node._next = self._head
        self._head = new_node

    def get_nth_highest_count(self, n):
        curr = self._head
        for i in range(n):
            print(curr.word)
            if curr is None:
                return None 
            curr = curr._next
        return curr._count if curr else None

    def print_upto_count(self, n):
        curr = self._head
        while curr is not None:
            if curr._count >= n:
                print(f"{curr._word} : {curr._count}")
            curr = curr._next

class Node:
    """
    This class represents Node that stores the 
    word its occurance
    """
    def __init__(self, word):
        self._word = word
        self._count = 1
        self._next = None
    def word(self):
        return self._word
    def count(self):
        return self._count
    def set_next(self, target):
        self._next = target
    def incr(self): 
        self._count = self._count + 1
    def __str__(self):
        return str(self._value) + "; "
    
    def word(self):
        return self._word
    
    def next(self):
        return self._next

def store(words, link):
    """
    the function goes through the list or line
    and store the value in the linked list
    """
    for word in words:
        link.update_count(word.lower())
    link.sort()

def split_text(text):
    """
    splits the text to remove punctuations
    """
    for char in string.punctuation:
        text = text.replace(char, ' ')
    
    words = text.split()
    result = []
    
    for word in words:
        if len(word) > 2:
            result.append(word)
    
    return result


def main():
    """
    calls all functions
    """
def main():
    """
    Calls all functions.
    """
    infilename = 'f.csv'
    link = LinkedList()
    
    infile = open(infilename, 'r')  
    csvreader = csv.reader(infile)
    for item in csvreader:
        if item and item[0][0] != '#':
            words = split_text(item[4])
            store(words, link)
    
    value = 10
    count_value = link.get_nth_highest_count(value)
    print(count_value)
    
    link.print_upto_count(count_value)

    infile.close() 

if __name__ == "__main__":
    main()
