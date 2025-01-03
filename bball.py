"""
    File: bball.py
    Author: Samak Gurung
    Purpose: This code iterates through the file and
    creates classes Team, Confrence and ConfrenceSet
    that stores the the team object in Confrences
    which is then stored in the ConfrenceSet that
    stores the highes value and then presents it
"""

class Team:
    """
    This class represents team and its associated
    confrence and win ratio.

    The class stores values in the form of integers and
    strings where the data stores its values as name of the
    team, confrence and win ration using the information
    from line
    """

    def __init__(self, line) : 
        """
        seperates the line into different segments and then uses
        the data from the line to store the name, confrence and
        calculate the win ratio

        Parameters: line is a string of words segmented to utilize
        the information
        """
        self._line = line
        list_ = []
        elem = []
        index_l = line
        line = line.strip().split()
        index_1 = []
        index_2 = []
        new_ = ' '.join(line)
        # finds the indexe with (
        for i in range(len(new_)):
            if new_[i] == '(':
                index_1.append(i)
        # finds inex of with the element )
        for i in range(len(new_)):
            if new_[i] == ')':
                index_2.append(i)
        elem.append(' '.join(list_))
        elem = elem[-1].split('(')
        self._name = line[0]
        self._conf = new_[index_1[-1]+1:index_2[-1]]
        self._win_ratio_str = int(line[-2])/(int(line[-1])+int(line[-2]))

    def name(self): 
        return self._name
    
    def conf(self): 
        return self._conf
    
    def win_ratio(self):   
        return self._win_ratio_str
    
    def __str__(self): 
        return "{} : {}".format(self._name, str(self._win_ratio_str))
    
class Conference:
    """
    This class represents the confences and the average
    win ratio associated teams stored in the form of a list.

    The class stores values in the form of lists, strings
    and integers  uses a seperate class Team to store the
    team and win ratio used to get its associated win ratio
    """
    def __init__(self, conf):
        self._name = conf
        self._teams = []
        self._win_ratio_avg = 0

    def __contains__(self, team) :
        return team in self._teams
    
    def name(self): 
        return self._name
    
    def add(self, team):
        self._teams.append(team)

    def win_ratio_avg(self):
        """
        Returns the average win ratio of the confrence
        using the team objects data
        Parameters: Team self object.

        Returns: total average win ratio
        """
        sum = 0
        num = len(self._teams)
        for val in self._teams:
            sum += val.win_ratio()
        self._win_ratio_avg = sum/num
        return self._win_ratio_avg
    
    def __str__(self):
        return "{} : {}".format(self._name, str(self._win_ratio_avg))

class ConferenceSet:
    """
    This class represents the overall confrences and their associated 
    win ratios in the form of a dictionary.

    The class stores values in the form of dictionary 
    where the confrence stores its keys as the name of each confrence
    and uses their associated average win ratios
    """
    def __init__(self):
        self._set = {}

    def add(self, team) :
        """
        Adds a new team to the confrence list

        Parameters: team is an object that is from class Team
        """
        conference = Conference(team.conf())
        if team.conf() not in self._set:
            conference.add(team)
            self._set[team.conf()] = conference
        else:
            self._set[team.conf()].add(team)

    def __repr__(self):
        return self._set
    
    def best(self):
        """
        Compares the win ratios and the 
        stores it in the greates variable and
        stores its name greates

        Returns: the confrence with the highest 
        average win ratio and name in the confrence set
        """
        greatest = 0
        great_key = []
        # iterates the class to get the greatest win ratio
        for key, value in self._set.items():
            if value.win_ratio_avg() >= greatest:
                greatest = value.win_ratio_avg()
        for k,v in self._set.items():
            if v.win_ratio_avg() == greatest:
                great_key.append(k)
        for val in sorted(great_key):
            print("{} : {}".format(val, str(greatest)))
        
def main():
    """
    Iterates through the file 
    and utilizes the classes
    to print the highes avg win ratio
    """
    file = open(input())
    Conf_ = ConferenceSet()
    for line in file:
        if line[0] != '#':
            team = Team(line)
            Conf_.add(team)
    Conf_.best()
main()
     