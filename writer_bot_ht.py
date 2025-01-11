import random
import sys
"""
File: writer_bot_ht.py
Author: Samyak Gurung
Course: CSC 120, Spring 2024
Purpose: This code utilizes markovs chain method
to create random text sentence or words that are 
printed according to the given parameter. the markov
chain method is incorporated using a class Dictionary
that stores values using the hash table
"""
SEED = 8
NONWORD = '@'

class Hashtable:
    """
    The class is used to store and create the hash table
    
    The data is stored by first creating a hashtable by
    using the input variable size which is later replaced
    by lists storing a key or string and another list which
    stores values
    """
    def __init__(self, size):
        self._pairs = [None] * size
        self._size = size

    def put(self, key, value):
        """
        this method accesses the dictionary or list
        checks the probes for whether they store the key
        if they do it inserts the value to the existing probe
        else it uses a hash function to get the index and stores
        the value which if there exists a value it uses linear 
        probing by decrementing the index by 1 until it ginds 
        an empty location
        parameter: key, value are strings and self denotes the class
        return: None
        """
        hash_ = self._hash(key)
        while self._pairs[hash_] is not None:
            if self._pairs[hash_][0] == key:
                # Append the value to the existing list of suffixes
                self._pairs[hash_][1].append(value)
                return
            hash_ = (hash_ - 1) % self._size
        self._pairs[hash_] = [key, [value]]

    def get(self, key):
        """
        this method is a getter function that iterates through
        the hash table and then returns the the value associated
        with the value and if there are no keys in the hash table
        the method returns None
        parameter: self, key is a string
        return: a list or None
        """
        hash_ = self._hash(key)
        for _ in range(self._size):
            if self._pairs[hash_] is None:
                return None
            if self._pairs[hash_][0] == key:
                return self._pairs[hash_][1]
            hash_ = (hash_ - 1) % self._size
        return None

    def __contains__(self, key):
        """
        is a special method that checks whether
        the hash table has the key in the hash table
        parameter: string
        return: Boolean value
        """
        hash_ = self._hash(key)
        for _ in range(self._size):
            if self._pairs[hash_] is None:
                return False
            if self._pairs[hash_][0] == key:
                return True
            hash_ = (hash_ - 1) % self._size
        return False

    def __str__(self):
        return str(self._pairs)

    def _hash(self, key):
        p = 0
        for c in key:
            p = 31 * p + ord(c)
        return p % self._size


def build_markov_chain(file, prefix_size, table_size):
    """
    the function uses the Dictionary to store data
    in markov chain form. Similar to the writer_bot code
    adapted for hash table using class
    parameter: 2 integers and a string for file
    return: hash table or list
    """
    table = Hashtable(table_size)
    prefix = [NONWORD] * prefix_size

    with open(file, 'r') as f:
        for line in f:
            words = line.strip().split()
            for word in words:
                prefix_key = ' '.join(prefix)
                table.put(prefix_key, word)
                prefix = prefix[1:] + [word]
    return table


def generate_text(markov_chain, prefix_size, num_words):
    """
    a function that generates the text using a hash table
    similar to the writer bot and stores it in a list
    adjusted for hash table
    parameter: a list and two integer
    return a list
    """
    random.seed(SEED)
    result = []
    prefix = [NONWORD] * prefix_size
    for _ in range(num_words):
        prefix_key = ' '.join(prefix)
        if prefix_key not in markov_chain:
            break

        suffixes = markov_chain.get(prefix_key)
        if len(suffixes) == 1:
            next_word = suffixes[0]
        else:
            next_word = suffixes[random.randint(0, len(suffixes) - 1)]
        result.append(next_word)
        prefix = prefix[1:] + [next_word]
    return result


def format_output(text_list):
    """
    it iterates through the list
    then prints the elements in the list
    where each line has 10 words
    parameter: a list
    return: None
    """
    formatted_lines = []
    line = []
    for word in text_list:
        line.append(word)
        if len(line) == 10:
            formatted_lines.append(" ".join(line))
            line = []
    if line:
        formatted_lines.append(" ".join(line))
    return "\n".join(formatted_lines)


def main():
    source_file = input()
    table_size = int(input())
    prefix_size = int(input())
    num_words = int(input())

    if prefix_size < 1:
        print("ERROR: specified prefix size is less than one")
        sys.exit(0)

    if num_words < 1:
        print("ERROR: specified size of the generated text is less than one")
        sys.exit(0)

    markov_chain = build_markov_chain(source_file, prefix_size, table_size)

    text = generate_text(markov_chain, prefix_size, num_words)

    output = format_output(text)
    print(output)

main()
