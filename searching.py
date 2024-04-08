import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    with open("sequential.json", mode= "r") as data_file:
        data  = json.load(data_file)
    for key in data.keys():
        if field == key:
            sequential_data = data[field]
            return sequential_data
    else:
        return None

def linear_search(sequence, target):
    """
Function sequenatialy iterates over sequence and stores position and total count of matches.
    :param sequence: (list): list on numbers
    :param target: (int): number to match within sequence
    :return: (dict): {'positions': <list of indices>, 'count': <total count>,}
    """
    positions = []
    count = 0
    for i, num in enumerate(sequence):
        if num == target:
            positions.append(i)
            count += 1

    return{"positions": positions, "count": count}

def pattern_search(sequence, pattern):
    """
        Function sequenatialy iterates over sequence and stores position and total count of matches.
        :param sequence: (str): string of basis ACTG
        :param pattern: (str): string pattern to match within sequence
        :return: (dict): {'positions': <list of indices>, 'count': <total count>,}
        """
    indices = set()
    pattern_size = len(pattern)

    left_idx = 0
    right_idx = pattern_size
    while right_idx < len(sequence):
        for idx in range(pattern_size):
            if pattern[idx] != sequence[left_idx + idx]:
                break
        else:
            indices.add(left_idx + pattern_size // 2)

        left_idx += 1
        right_idx += 1

    return indices

def binary_search(sequence, number):
    """
    Function performs binary search on !!ordered!! sequence and stores position of match if found.
    :param sequence: (list): list on numbers
    :param number: (int): number to match within sequence
    :return: (int, None): index of match if found, None otherwise
    """
    left, right = (0, len(sequence) - 1)

    while left <= right:
        middle = (right + left) // 2

        if number < sequence[middle]:
            right = middle - 1
        elif number > sequence[middle]:
            left = middle + 1
        else:
            return middle
    return

def main():
   sequential_data = read_data("sequential.json", "unordered_numbers")
   print("sequential Data:", sequential_data)



if __name__ == '__main__':
    main()