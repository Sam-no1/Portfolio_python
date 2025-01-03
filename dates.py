"""
    File: dates.py
    Author: Samak Gurung
    Purpose: This code requests for a file name and iterates through it
    and reads its first indext which when I it stores the values in a
    dictionary using class system and R presents the dates and the
    event associated with it. It also utilizes class systems to store
    the date and the events where each date has a list with events that
    are associated with them
"""
class Date:
    """
    This class represents the Date and Event that occurs in the date

    The class defines the the objects dates and events where it stores 
    the events in alocated for the date in the form of a string and events
    in the form of list. where methods are then used to get the date and events
    as well as add the events associated with the list
    """
    def __init__(self, date, event):
        self._date = date
        self._event = [event]

    def get_event(self):
        return self._event
    
    def get_date(self):
        return self._date

    def add_event(self, event):
        self._event.append(event)

    def __str__(self):
        return "{}: {}".format(self._date, self._event)

class DateSet:
    """
    This class represents dates and their associated 
    events in the form of a dictionary.

    The class stores values in the form of dictionary 
    where the data stores its keys as the date and uses
    a seperate class Date to store the date and their
    associated events
    """
    def __init__(self):
        self._date = {}

    def add_event(self, date, event):
        """
        adds events in the dictionary
        and their associated dates
        though using add_event from the
        class Date"""
        new_d = Date(date, event)
        date_n = canonicalize_date(date)
        if date_n not in self._date.keys():
            self._date[date_n] = new_d
        else:
            self._date[date_n].add_event(event)

    def __str__(self):
        return str(self._date)

def canonicalize_date(date_str):
    """
    the function changes the date_str value
    in the required form seperated through - 
  
    Parameters: month stores the month to compare
    to present the month in integer
  
    Returns: a string in the format of date seperated
    through -
    """
    date = date_str
    month = ['Jan', 'Feb', 'Mar', 'Apr', 
             'May', 'Jun', 'Jul', 'Aug', 
             'Sep','Oct', 'Nov', 'Dec']
    if '-' in date_str:
        date = date_str.split('-')
        mm = date[1]
        dd = date[2]
        yyyy = date[0]
        return "{:d}-{:d}-{:d}".format( int(yyyy), 
                            int(mm), int(dd))
    if '/' in date_str:
        date = date_str.split('/')
        mm = date[0]
        dd = date[1]
        yyyy = date[2]
        return "{:d}-{:d}-{:d}".format( int(yyyy), 
                                int(mm), int(dd))
    else:
        date = date_str.split(' ')
        # iterates through the list to find
        # month in int format
        for i in range(len(month)):
            if month[i] == date[0]:
                mm = i+1
        dd = date[1]
        yyyy = date[2]
    return "{:d}-{:d}-{:d}".format( int(yyyy),
                            int(mm), int(dd))
  
def traverse(file_name):
    """
    iterates through file and seperates the lines through 'I' 'R' 
    and other and stores the data in data set and compares to 
    search and prints the events when 'R' is present in the list
    and incorrect if other pops up
  
    Parameters: dates establishes the class DateSet and stores 
    the values of date and event which is compared to search for
    events of the dates
  
    Returns: the dates and events that are requested through the
    file
    """
    file = open(file_name)
    dates = DateSet()
    list_ = []
    # iterates throuh the seperates the line and 
    # file and compares the value 
    # to store present or validate whether the values in
    # the file is correct or incorrect
    for line in file:
        seperator = seperate(line)
        if line[0] == 'I':
            date = line[0:seperator[0]].strip().split()
            dates.add_event(canonicalize_date(' '.join(date[1:])), 
                            line[seperator[0]+2:-1].strip())
        if line[0] == 'R':
            
            search = find(canonicalize_date(line[2:]), dates)
            represent(search)
        if line[0] != 'I' and line[0] != 'R':
            print("Error - Illegal operation.")
    file.close()
    return dates

def seperate(line):
    """
    finds the ':' and stores the index in the list which is then used to
    seprate the line
    Parameters: seperator stores index of the ':' 
  
    Returns: A list that stores index of the line required
    """
    seperator = []
    for i in range(len(line)):
        if line[i] == ':':
            seperator.append(i)
    return seperator

def find(date, dict_):
    """
    searches the key in the dict to check whether 
    the dictionary stores the date for event  
    Returns: A class date that stores the event and date
    """
    if canonicalize_date(date) in dict_._date:
        return dict_._date[canonicalize_date(date)]
    if dict_._date == None:
        return None
    
def represent(date):
    """
    prints the value  
    Returns: returns a string that 
    presents values in requested format
    """
    if date != None:
        for val in sorted(date._event):
            print("{}: {}".format(date._date, val))
    else:
        return
    
def main():
    """
    calls the functionand requests the user for file
    """
    file = input()
    dict_ = traverse(file)
main()

