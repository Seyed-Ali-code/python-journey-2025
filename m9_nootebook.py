def phonebook(entries):
    phonebook_dict = {}
    for name, number in entries:
        phonebook_dict[name] = number
    return phonebook_dict
entries = [('Alice', '123-4567'), ('Bob', '987-6543'), ('Charlie', '555-0000')]
print(phonebook(entries))