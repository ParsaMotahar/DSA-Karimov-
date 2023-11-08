'''Common Keys

Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.

Example:

    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 3, 'c': 4, 'd': 5}
    merge_dicts(dict1, dict2)

Output:

    {'a': 1, 'b': 5, 'c': 7, 'd': 5}'''

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    for key in dict1:
        count = 0
        if key in dict2:
            count = dict1[key] + dict2[key]
            merged_dict[key] = count
    return merged_dict
print(merge_dicts(dict1, dict2))