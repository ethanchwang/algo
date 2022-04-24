# problem: find the shortest substring within a given string that contains all the elements of a given list
# e.g. given ['x','y','z'] and 'zxzxyzyxzyz' return 'zxy'
# return an empty string if none exists

def is_string_valid(input_list, input_substring):
    for index_of_character in range(len(input_substring)):
        if input_substring[index_of_character] in input_list:
            del input_substring[index_of_character]
    if len(input_list) == 0:
        return True
    else:
        return False
            

def find_shortest_substring(input_list, input_string):
