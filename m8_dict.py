def word_length(words):
    lengths = {}
    for word in words:
        lengths[word] = len(word)
    return lengths
names = ['apple', 'banana', 'cherry', 'date']
print(word_length(names))