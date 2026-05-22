from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    dict_1 = {}
    for char in word:
        if char  in dict_1:
            dict_1[char] += 1
        else:
            dict_1[char] = 1
    return dict_1






# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
