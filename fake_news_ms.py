import csv
import string
import sys
"""
File: friends.py
Author: Samyak Gurung
Purpose: this code stores classes
    linked list and node that is 
    used as a helper or import file
    used in storing data about the file
"""
sys.setrecursionlimit(4000)
class Word:
    def __init__(self, word):
        self._word = word
        self._count = 1
    def word(self):
        return self._word
    def count(self):
        return self._count
    def incr(self):
        self._count += 1
    def __lt__(self, other):
        return self._count < other._count
    def __str__(self):
        return ("{}:{:d}".format(self._word, self._count))

def store(words, list_):
    """
    the function goes through the list or line
    and store the value in the linked list
    """
    for word in words:
        checker = check(word, list_)
        if checker[1] == False:
            new_word = Word(word)
            list_.append(new_word)
        list_ = checker[0]
    return list_
    
def check(word, list):
    for char in list:
        if char.word() == word:
            char.incr()
            return [list, True]
    return [list, False]

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
            result.append(word.lower())
    return result

def sort_list(List): 
    if len(List)<=1:
        return List
    else:
        mid = len(List)//2
        L1 = List[:mid]
        L2 = List[mid:]
        sortedL1 = sort_list(L1)
        sortedL2 = sort_list(L2)
        return merge_sort(sortedL1, sortedL2, [])
    
def merge_sort(L1, L2, merged):
    if not L1 or not L2:
        return merged + L1 + L2
    else:
        if L1[0] > L2[0]:
            return merge_sort(L1[1:], L2, merged + [L1[0]])
        elif L1[0] < L2[0]:
            return merge_sort(L1, L2[1:], merged + [L2[0]])
        else:
            if L1[0].word() < L2[0].word():
                return merge_sort(L1[1:], L2, merged + [L1[0]])
            else:
                return merge_sort(L1, L2[1:], merged + [L2[0]])

def get_count(list, value):
    i = 0
    for j in range(value):
        i+=1
    return list[i].count()

def main():
    """
    Calls all functions.
    """
    infilename = input('File: ')
    # word = Word()
    text = []
    new = []
    infile = open(infilename, 'r')  
    csvreader = csv.reader(infile)
    for item in csvreader:
        if item and item[0][0] != '#':
            words = split_text(item[4])
            text = text+ words
    stored = store(text, new)
    new_list = sort_list(stored)

    index = input('N: ')
    result_count = get_count(new_list, int(index))
    for i in range(len(new_list)):
        if int(new_list[i].count()) >= int(result_count):
            print("{} : {:d}".format(new_list[i].word(), new_list[i].count()))
    
    
    # value = int(input())
    # count_value = link.get_nth_highest_count(value)
    
    # link.print_upto_count(count_value)

    infile.close() 

if __name__ == "__main__":
    main()
