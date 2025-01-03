"""
    File: word_search.py
    Author: Samyak Gurung
    Purpose: This program processes two files one file
    containing words to check and compare and the other the grid that is used to 
    find or search through its element to find a word that is present in the word file
"""
def get_word_list(word_file):
    """
    opens the word file and stores it in a list
    Parameters: word_list is a list that stores the words from word file
    Returns: A list that stores the words from the word file
    """
    file = open(word_file, 'r')
    word_list = []
    for word in file:
        word_list.append(word.strip('\n'))
    file.close()
    return word_list




def read_letter_list(file):
    """
    opens the grid file and stores it in a list
    Parameters: grid is a list that stores the words from word file
    Returns: A list that stores the letters from the grid file
    """
    f = open(file, 'r')
    grid = []
    for line in f:
        row = line.split()
        grid.append(row)
    f.close()
    return grid




def diagonal_elements(grid):
    """
    Seperates the grid file and iterates through the diagonal elements
    Parameters: diagonal is a list that stores diagonal elements
    Returns: A list that stores the diagonal elements from the grid
    """
    diagonal = []
    d = []
    for i in range(len(grid)):
        d.append(grid[i][i])
    diagonal.append(d)
    for i in range(1, len(grid)):
        x, y = 0, i
        b = []
        while x < len(grid) and y < len(grid):
            b.append(grid[x][y])
            x += 1
            y += 1
        diagonal.append(b)
    for i in range(1, len(grid)):
        x, y = i, 0
        b = []
        while x < len(grid) and y < len(grid):
            b.append(grid[x][y])
            x += 1
            y += 1
        diagonal.append(b)
    return diagonal




def vertical_elements(grid):
    """
    Seperates the grid file and iterates through the vertical elements
    Parameters: diagonal is a list that stores vertical elements
    Returns: A list that stores the vertical elements from the grid
    """
    vertical_grid = []
    for i in range(len(grid)):
        vertical_list = []
        for j in range(len(grid[i])):
            vertical_list.append(grid[j][i])
        vertical_grid.append(vertical_list)
    return vertical_grid

def list_string(grid):
    """
    concactinates the elements of the row into a single string
    Parameters: n is the new list that stores the concactinated list
    Returns: a list that stores the concactinated string
    """
    n = []
    for list in grid:
        n.append(''.join(list))
    return n

def check_grid(lists, word_list):
    """
    loops throught the lists and checks through each word
    Parameters: words is a string that stores the words that are checked
    Returns: a list that stores the words found in the grid
    """
    words = []
    for list_ in lists:
        w = []
        for string in list_:
            w = occurs_in(string, word_list)
            words = words+w
    return words
def print_this(lists):
    """
    iterates through the list and prints the words
    """
    l = sorted(lists)
    for i in l:
        print(i)
        

def occurs_in(substr, word_list):
    """
    iterates through the provided string and sends the word found in the list
    Parameters: words stores the words found when compairing it with the word_list
    Returns: a list of strings that has checked words
    """
    words = []
    length = len(substr)
    for i in range(length):
        for j in range(i + 3, length + 1): 
            sub = substr[i:j]
            if sub in word_list:
                words.append(sub)

    r_substr = substr[::-1]
    for i in range(len(r_substr)):
        for j in range(i + 3, len(r_substr) + 1): 
            sub = r_substr[i:j]
            if sub in word_list:
                words.append(sub)
    return words



def main():
    word_file = input()
    grid_file = input()
    word_list = get_word_list(word_file)
    grid_list = read_letter_list(grid_file)
    if grid_list == []:
        return None
    else:
        normal = list_string(grid_list)
        vertical = list_string(vertical_elements(grid_list))
        diagonal = list_string(diagonal_elements(grid_list))
        checking_list = [normal, vertical, diagonal]
        go_through = check_grid(checking_list, word_list)
        print_this(go_through)
if __name__ == "__main__":
    main()
