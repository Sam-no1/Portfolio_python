"""
File: street.py
Author: Samyak Gurung
Purpose: this code uses classes to
    to store the the width and heights
    of building stores the the width and
    leaf for park and width and trash for
    empty lot that stores and calls the values
    which is then stored and used to print the
    required image.
"""
class Building:
    """
    this class stores the width height and its
    which is then used to level by level print each
    line
    the class also has at_height method that presents
    the string with the associated level of strings
    at that height
    """
    def __init__(self, width, height, brick):
        self._width = width
        self._height = height
        self._brick = brick

    def at_height(self, height):
        if height <= self._height:
            return self._brick*self._width
        if height > self._height:
            return ' '*self._width
        
class Park:
    """
    this class stores the width and its foliage
    which is used as parameters for the image of the park
    accorrding to its parameters

    the class also has at_height method that presents
    the string with the associated level of strings
    at that height
    """
    def __init__(self, width, leaf):
        self._width = width
        self._leaf = leaf

    def at_height(self, height):
        if height <= 2:
            sides = self._width//2
            return ' '*sides + '|' + ' '*sides
        if height > 2:
            sides = self._width//2
            if height == 3:
                return ' '*(sides-2) + self._leaf*5 + ' '*(sides-2)
            if height == 4:
                return ' '*(sides-1) + self._leaf*3 + ' '*(sides-1)
            if height == 5:
                return ' '*sides + self._leaf + ' '*sides
            else:
                return ' '*self._width
            
class EmptyLot:
    """
    this class stores the width and foliage/trash
    which is  used to print the empty lot area
    
    the class also has at_height method that presents
    the string with the associated level of strings
    at that height
    """
    def __init__(self, width, trash):
        self._width = width
        corrected = correct(trash)
        self._trash = corrected

    def at_height(self, height):
        if height == 1:
            if self._width%len(self._trash) != 0:
                return self.trash_line()
            else:
                return self._trash*(self._width//len(self._trash))
        else:
            return ' '*self._width
        
    def trash_line(self):
        repitition = self._width//len(self._trash)
        extra = self._width - len(self._trash)*repitition 
        return self._trash*repitition + self._trash[0:extra]

def correct(text):
    """
    this function checks the string for the empty
    lot to prink blank spaces in the empty lot and 
    returns space in the areas for underscore
    Parameter: text a string that stores the foliage
    for empty lot
    Return: string which has _ replaced with a space
    """
    if len(text) == 0:
        return ''
    elif text[0] == '_':
        return ' ' + correct(text[1:])
    else:
        return text[0] + correct(text[1:])

def print_at_height(thing, height, width):
    """
    This function prints the result for the
    whole code using helper functions
    Parameter: thing is the list of class, height
    and width are integers
    Return: Nothing
    """
    print('+'+'-'*width +'+')
    helper(thing, height)
    print('+'+'-'*width +'+')
    return

def helper(thing, height):
    """
    recursive helper function used to print the image for the
    user using a helper function to print the objects together

    Parameter: thing is a list of class/object which is used to print
    the image, height is an integer that indicates which level
    to print
    Return: a recursive call
    """
    if height != 0:
        print('|'+ print_things(thing, height) +'|')
        return helper(thing, height-1)
    return

def print_things(thing, level):
    """
    the function is a recursive helper function for the 
    helper function that returns the string that incompasses 
    all the objects at the given level or height
    Parameter: thing is a list of the classes storing the
    required classes from above to print each at theri level,
    level is the requested height
    Return: a string containing the objects at the level
    """
    if thing == []:
        return ''
    if thing != []:
        return thing[0].at_height(level) + print_things(thing[1:], level)
    return

def break_down(street):
    """
    function that seperates the inputs
    stores them in a class and returns a list
    that has classes with the requested parameters
    Parameter: street a list with parameters for class
    Returns: a list containing the requested objects
    """
    new = []
    helper_street(street, new)
    return new

def helper_street(street, list):
    """
    the recursive function is a helper function
    that stores the values
    Parameter: street is liset that
    contains the users parameters and list is the
    list that stores the objects according to 
    users request
    Return:
    """
    if street == []:
        return ''
    
    if street[0][0] == 'b':
        parameters = street[0][2:].split(',')
        width = int(parameters[0])
        height = int(parameters[1])
        brick = parameters[2]
        building = Building(width, height, brick)
        list.append(building) 
        return helper_street(street[1:], list)
    
    if street[0][0] == 'p':
        parameters = street[0][2:].split(',')
        width = int(parameters[0])
        leaf = parameters[1]
        park = Park(width, leaf)
        list.append(park) 
        return helper_street(street[1:], list)

    if street[0][0] == 'e':
        parameters = street[0][2:].split(',')
        width = int(parameters[0])
        trash = parameters[1]
        trash = EmptyLot(width, trash)
        list.append(trash) 
        return helper_street(street[1:], list)
    
def height_width(street, h_height, total_width):
    """
    the recursive function stores the total
    width of the objects and the highest height among
    the objects
    Parameters: street is a list that stores the users
    input, h_hieght is initially 9 as well as the
    total width are both integers
    Return: h_height, total_width integers for the total
    width and the highest height
    """
    if street == []:
        return [h_height, total_width]
    if street[0][0] == 'b':
        parameters = street[0][2:].split(',')
        width = int(parameters[0])
        height = int(parameters[1])
        n_width = total_width + width
        if h_height < height+1:
            return height_width(street[1:], height+1, n_width)
        return height_width(street[1:], h_height, n_width)

    if street[0][0] == 'p':
        parameters = street[0][2:].split(',')
        width = int(parameters[0])
        leaf = parameters[1]
        n_width = total_width + width

        if h_height < 6:
            return height_width(street[1:], 6, n_width)
        return height_width(street[1:], h_height, n_width)

    if street[0][0] == 'e':
        parameters = street[0][2:].split(',')
        width = int(parameters[0])
        n_width = total_width + width
        if h_height < 2:
            return height_width(street[1:], 2, n_width)
        return height_width(street[1:], h_height, n_width)

def main():
    street = input('Street:')
    street = street.split()
    break_ = break_down(street)
    dimension = height_width(street, 0, 0)
    height = dimension[0]
    width = dimension[1]
    print_at_height(break_, height,width)
main()
        
