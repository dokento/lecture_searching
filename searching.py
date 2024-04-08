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
def main():
   sequential_data = read_data("sequential.json", "unordered_numbers")
   print("sequential Data:", sequential_data)



if __name__ == '__main__':
    main()