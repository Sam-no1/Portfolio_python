"""
    File: pokemon.py
    Author: Samak Gurung
    Purpose: This program iteratest through the
    given file and takes in input parameter
    that iterates through the file and processes 
    the average of the pokemons given in the
    file which is then stored in a double dictionary
    and seperates it into types and then
    finding the highest average among the types.
"""

def parse(file):
    """
    iterates through the file and stores the values 
    in an initial dictionary
    Parameters: dict stores the values from file
    Returns: returns a dictionary seperated by names
    """
    f = open(file)
    dict = {}
    for line in f:
        line = line.split(',')
        dict[line[1]] = line[2:-1]
    return dict

def set_dict(dict):
    """
    seperates the values of the initial 
    dictionary and creates another dictionary 
    storing according to their stats
    Parameters: stats stores the keys to be 
    used in the dictionary of dictionary
    Returns: a dictionary of dictionary that 
    seperates types and stats according to their
      names
    """
    s = dict['Name']
    stats = []
    for elements in s:
        stats.append(elements.lower())
    for keys, values in dict.items():
        if keys!= '#':
            inner_dict = {}
            for i in range(len(values)):
                inner_dict[stats[i]] = values[i]
            dict[keys] = inner_dict
    return dict

def average(type_list):
    """
    gets the average of the list
    Parameters: avg is the variable 
    that stores the average
    Returns: average of the list
    """
    sum = 0
    avg = 0
    if sum != 0 or len(type_list) != 0:
        for vals in type_list:
            sum += vals
        avg = sum/len(type_list)
    return avg

def g_avg(dict):
    """
    gets the greatest average in the
     dictionary
    Parameters: greatest stores the 
     type of pokemon that has the 
     highest average
    Returns: a string that is they 
    key for a dictionary
    """
    great = []
    great_val = 0
    for val in dict.values():
        if great_val == 0:
            great_val = val
        if val >= great_val:
            great_val = val
    for key in dict:
        if great_val == dict[key]:
            great.append(key)
    return great

def print_greatest(dict, key):
    """
    prints the result
    """
    for value in key:
        print("{}: {}".format(value, 
            dict[value]))

def stats_list(dict):
    """
    stores the stats in list format
    Parameters: a_list stores the
    stats in the form of list
    Returns: a list containing
    stats to contain
    """
    a_list = []
    s = dict['Name']
    for keys in s:
        a_list.append(keys)
    return a_list

def types_poke(dict):
    """
    seperates and creates a new dictionary 
    that stores the key as types and pokemons
    as values
    Parameters: new_dict seperates 
    the types and the pokemons
    Returns: a new dictionary that 
    seperates the types of pokemons
    """
    new_dict = {}
    for keys, values in dict.items():
        if keys != 'Name':
            for k, v in values.items():
                if k == 'type 1':
                    if v != '':
                        if v not in new_dict:
                            new_dict[v] = [keys]
                        if v in new_dict:
                            new_dict[v].append(keys)

    for keys, values in new_dict.items():
        new = []
        for pokes in values:
            if pokes not in new:
                new.append(pokes)
        new_dict[keys] = new
    return new_dict




def just_avg(p_dict, t_dict, type):
    """
    gets the average of the types
    Parameters: s_types stores the average of
      types and seperates them
    Returns: a dictionary with sorted averages
    """
    s_types = {}
    for keys, values in t_dict.items():
        t_p_stat = []
        for vals in values:
            for key, v in p_dict.items():
                if vals == key:
                    for stat, num in v.items():
                        if stat == type:
                            t_p_stat.append(int(num))
        s_types[keys] = average(t_p_stat)
    return s_types




def main():
    """
    initiates and ends the code
    """
    file_ = input().strip()
    parse_ = parse(file_)
    poke_dict = set_dict(parse_)
    types_p = types_poke(poke_dict)
    stats_ = stats_list(poke_dict)
    
    while True:
        type_input = input().strip()
        if not type_input:
            break
        if type_input == '':
            break
        type_ = type_input.lower()
        if type_ == 'specialattack':
            type_ = 'sp. atk'
        elif type_ == 'specialdefense':
            type_ = 'sp. def'
        if type_ in stats_:
            avg_finder = just_avg(poke_dict, 
                            types_p, type_)
            greatest = sorted(g_avg(avg_finder))
            print_greatest(avg_finder, greatest)

if __name__ == "__main__":
    main()