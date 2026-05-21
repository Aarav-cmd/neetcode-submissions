def remove_fourth_character(word: str) -> str:
    char_before_fourth = word[:3]
    char_after_fourth = word[4:]
    new_word = char_before_fourth + char_after_fourth
    return new_word


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
