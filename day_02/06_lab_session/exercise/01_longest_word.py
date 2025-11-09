def get_longest_word(text):
    """TODO: Add decoding process"""
    # For each word in the sentence, check length/len. If longest, store, then print.
    words = text.split()
    return max(words, key=len) if words else""




# "The quick brown fox jumps" -> "quick"
print(get_longest_word("The quick brown fox jumps"))

# "I love programming in Python!" -> "programming"
print(get_longest_word("I love programming in Python!"))

# "" -> ""
print(get_longest_word(""))




