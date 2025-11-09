from pygments.lexer import words


def get_longest_word(text):
    """TODO: Add decoding process"""
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word


# "The quick brown fox jumps" -> "quick"
print(get_longest_word("The quick brown fox jumps"))


# "I love programming in Python!" -> "programming"
print(get_longest_word("I love programming in Python!"))

# "" -> ""
print(get_longest_word(""))
