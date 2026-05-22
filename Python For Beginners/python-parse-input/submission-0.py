from typing import List

def read_integers() -> List[int]:
    user_input =input()
    list_of_strings = user_input.split(",")
    list_of_int = []

    for string in list_of_strings:
        list_of_int.append(int(string))
    return list_of_int

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
